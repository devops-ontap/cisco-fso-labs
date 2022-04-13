#!/bin/bash
# Installer for the ThousandEyes Agent/BrowserBot (www.thousandeyes.com)
#
# (C) 2020 ThousandEyes, Inc.
#

################################################################################
# Configuration parameters
################################################################################

DEBIAN_REPOSITORY="https://apt.thousandeyes.com"
DEBIAN_PUBLIC_KEY_FILE="thousandeyes-apt-key.pub"
REDHAT_REPOSITORY="https://yum.thousandeyes.com"
REDHAT_PUBLIC_KEY_FILE="RPM-GPG-KEY-thousandeyes"
PACKAGE_NAME="te-agent"

PUBLIC_KEY="-----BEGIN PGP PUBLIC KEY BLOCK-----
Version: GnuPG v1.4.11 (GNU/Linux)

mQENBFApO8oBCACxHESumhIcqUTvpIA+q9yIWQQL2nE1twF1T92xIJ9kgOF/5ali
iEqtNm0Vm2lpZy/LBcTG/UJY5rsKZVVWaepzXsNABeqzEE8t1CMGJ3hqtaZu59nd
VglzwuNuNL+qTjtgX3taPQrO9SQNwMq7lpQeTgBKAM8PjjKMdjezHl2rdtEdG2Km
VtN9qYDmb4ysCwq+ifCwOsZ4AM97r1M1+KwjNIa9EqA86qBixp2WqxaZ0ba4S3TG
wxwEa9Zcm+OXYKcU3TBug+S1OMp14E3PlfSCuS1T7xvbV0KgQRSOsMgPYQLcvw8u
r/uyONvdrx2+/oKrnd/ePZu2ha83msqOR+3vABEBAAG0KVRob3VzYW5kRXllcyA8
YnVpbGR1c2VyQHRob3VzYW5kZXllcy5jb20+iQE4BBMBAgAiBQJQKTvKAhsDBgsJ
CAcDAgYVCAIJCgsEFgIDAQIeAQIXgAAKCRDJmhX1vnGJAKdFB/44WXjZvtirSNzn
Z9vDdxk/zXiWCyR/19znf+piIYCbRBqtoVGRxsxMS0FFHZZ4W6SlieklWJX3WShh
/17EaxC596Aegp4MuwTTQ3hMdEtyB1hDd1e1XQUQULaW/0+4u+dD9n6pHYnKF4Zx
DOQhJ5uXgKTaGZ5Z01JG92R9FxQJMre4j2N4F+EYd6pR9Cr2eBk5CVdnvw8njSak
PhmtmIjhf9faCsWf+mJGQuYggSKk8DJcobIjT3TqLoUlRYwhre1cnB/0mGTph/P1
xFCSpCMGU51jwpyUy1t2bHYeSVAba4PNqOOlITwRfDkKQxB9frI8ycGyx2S+eKFD
Qty56ztU
=p3tN
-----END PGP PUBLIC KEY BLOCK-----"

TE_AGENT_CFG_LOCATION=${TE_AGENT_CFG_LOCATION-/etc/te-agent.cfg}

################################################################################
# Terminal output helpers
################################################################################

# echo_title() outputs a title padded by =, in yellow.
echo_title() {
    TITLE=$1
    NCOLS=$(tput cols)
    NEQUALS=$(((NCOLS-${#TITLE})/2-1))
    EQUALS=$(printf '=%.0s' $(seq 1 $NEQUALS))
    tput setaf 3  # 3 = yellow
    echo "$EQUALS $TITLE $EQUALS"
    tput sgr0  # reset terminal
}

# echo_step() outputs a step collored in cyan, without outputing a newline.
echo_step() {
    tput setaf 6  # 6 = cyan
    echo -n "$1"
    tput sgr0  # reset terminal
}

# echo_step_info() outputs additional step info in cyan, without a newline.
echo_step_info() {
    tput setaf 6  # 6 = cyan
    echo -n " ($1)"
    tput sgr0  # reset terminal
}

# echo_right() outputs a string at the rightmost side of the screen.
echo_right() {
    TEXT=$1
    echo
    tput cuu1
    tput cuf "$(tput cols)"
    tput cub ${#TEXT}
    echo "$TEXT"
}

# echo_failure() outputs [ FAILED ] in red, at the rightmost side of the screen.
echo_failure() {
    tput setaf 1  # 1 = red
    echo_right "[ FAILED ]"
    tput sgr0  # reset terminal
}

# echo_success() outputs [ OK ] in green, at the rightmost side of the screen.
echo_success() {
    tput setaf 2  # 2 = green
    echo_right "[ OK ]"
    tput sgr0  # reset terminal
}

echo_warning() {
    tput setaf 3  # 3 = yellow
    echo_right "[ WARNING ]"
    tput sgr0  # reset terminal
    echo "    ($1)"
}

# exit_with_message() outputs and logs a message before exiting the script.
exit_with_message() {
    echo -e "\n$1" | tee -a "$INSTALL_LOG"
    if [[ $INSTALL_LOG && "$2" -eq 1 ]]; then
        echo "For additional information, check the ThousandEyes install log: $INSTALL_LOG"
    fi
    echo
    debug_variables
    echo
    exit 1
}

# exit_with_failure() calls echo_failure() and exit_with_message().
exit_with_failure() {
    echo_failure
    exit_with_message "FAILURE: $1" 1
}

unsupported_os() {
    exit_with_failure "This machine's operating system is unsupported by ThousandEyes. Refer to https://docs.thousandeyes.com/product-documentation/enterprise-agents/supported-enterprise-agent-operating-systems for more details."
}

browserbot_unsupported_os() {
    exit_with_failure "This machine's operating system is unsupported by BrowserBot.  Refer to https://docs.thousandeyes.com/product-documentation/enterprise-agents/supported-enterprise-agent-operating-systems for more details."
}

################################################################################
# Other helpers
################################################################################

log_command() {
    echo "$1" >> $INSTALL_LOG
    eval "$1"
}

# start_service() starts a service
start_service() {
    log_command "systemctl start $1 >> $INSTALL_LOG 2>&1"
}

# stop_service() stops a service
stop_service() {
    log_command "systemctl stop $1 >> $INSTALL_LOG 2>&1"
}

# service_is_running() returns true if a service is running
service_is_running() {
    systemctl is-active $1 > /dev/null
}

################################################################################
# Installation steps
################################################################################

# check_if_root_or_die() verifies if the script is being run as root and exits
# otherwise (i.e. die).
check_if_root_or_die() {
    echo_step "Checking installation privileges"

    SCRIPT_UID=$(log_command "id -u")

    if [ "$SCRIPT_UID" != 0 ]; then
        exit_with_failure "Installer must be run as root"
    fi
    echo_success
}

# detect_operating_system() obtains the operating system and exits if it's not
# one of: Ubuntu, RedHat, CentOs.
detect_operating_system() {
    echo_step "Detecting operating system"

    if log_command "test -f /etc/debian_version"; then
        echo_step_info "Debian/Ubuntu"
        OPERATING_SYSTEM="DEBIAN"
    elif log_command "test -f /etc/redhat-release || test -f /etc/system-release-cpe"; then
        echo_step_info "RedHat/CentOS"
        OPERATING_SYSTEM="REDHAT"
    else
        unsupported_os
    fi
    echo_success
    export OPERATING_SYSTEM
}

# detect_architecture() obtains the system architecture and exits if it's not x86_64.
detect_architecture() {
    echo_step "Detecting architecture"

    ARCHITECTURE=$(log_command "uname -m")

    if [ "$ARCHITECTURE" == "x86_64" ] || [ "$ARCHITECTURE" == "aarch64" ]; then
        echo_step_info "$ARCHITECTURE"
        echo_success
    else
        exit_with_failure "Unsupported architecture ($ARCHITECTURE)"
    fi
}

update_package_index() {
    for i in `seq 1 $1`; do
        echo -n " "
    done

    echo_step "Updating package index"
    # apt-get doesn't set an error value for a warning, and failing to fetch
    # data from a repository is a warning.
    APTGET_OUTPUT=$(log_command "apt-get -qq update 2>&1")
    APTGET_STATUS=$?

    # we also want to dump this into the install log
    echo "$APTGET_OUTPUT" >>"$INSTALL_LOG"

    APTGET_FAILED=$(echo "$APTGET_OUTPUT" | grep Failed | grep "$INSTALL_REPOSITORY")
    if [ "$APTGET_STATUS" != 0 ] || [ -n "$APTGET_FAILED" ]; then
        exit_with_failure "Failed running 'apt-get update'"
    else
        echo_success
    fi
}

# install_debian() installs ThousandEyes into a Debian/Ubuntu system.
install_debian() {
    echo_step "Installing ThousandEyes (Debian)";
    echo

    #
    # Check for repo override
    #
    if [ -n "$OVERRIDE_REPOSITORY" ]; then
        INSTALL_REPOSITORY="$OVERRIDE_REPOSITORY"
    else
        INSTALL_REPOSITORY="$DEBIAN_REPOSITORY"
    fi

    #
    # Check Debian flavor.
    #
    echo_step "  Detecting Debian flavor"
    if command_exists lsb_release; then
        CODENAME=$(log_command "lsb_release -s -c")
    fi
    if [ -z "$CODENAME" ] && [ -f /etc/lsb-release ]; then
        CODENAME=$(log_command "grep \"^DISTRIB_CODENAME=\" /etc/lsb-release | cut -f2 -d=")
    fi
    if [ -z "$CODENAME" ] && [ -f /etc/debian_version ]; then
        CODENAME=$(log_command "cut -d. -f1 /etc/debian_version")
    fi

    FLAVOR="Ubuntu"

    echo_step_info "$FLAVOR/$CODENAME"
    check_if_supported "$FLAVOR" "$CODENAME" "" && echo_success

    #
    # Check installation tools.
    #
    echo_step "  Checking installation tools"
    command_exists apt-get || exit_with_failure "Command 'apt-get' not found"
    command_exists apt-key || exit_with_failure "Command 'apt-key' not found"
    command_exists systemctl || exit_with_failure "Command 'systemctl' not found"
    echo_success

    stop_if_running

    #
    # Check if apt-transport-https is installed. If not, install it.
    #
    apt_transport_https_installed=$(dpkg-query -W --showformat='${Status}\n' apt-transport-https|grep "install ok installed")
    echo_step "  Checking for apt-transport-https: ${apt_transport_https_installed}"

    if [ "" == "$apt_transport_https_installed" ]; then
        echo_step "  apt-transport-https not found. Installing it."
        if ! log_command "apt-get -qq --force-yes --yes install apt-transport-https >> $INSTALL_LOG 2>&1"; then
            exit_with_failure "Failed installing apt-transport-https"
        else
            echo_success
        fi
    else
        echo_success
    fi

    if [ "$SKIP_REPO_CREATION" = false ]; then
        #
        # Add apt-get source.
        #
        echo_step "  Adding repository"
        if [ -d /etc/apt/sources.list.d ]; then
            cd /etc/apt/sources.list.d
            rm -f thousandeyes.list
            echo "deb $INSTALL_REPOSITORY $CODENAME main" > thousandeyes.list
            chmod 644 thousandeyes.list
        else
            exit_with_failure "Package resource directory not found"
        fi
        echo_success

        rm -f ${DEBIAN_PUBLIC_KEY_FILE}
        echo "$PUBLIC_KEY" > ${DEBIAN_PUBLIC_KEY_FILE}
        if [ -s "$DEBIAN_PUBLIC_KEY_FILE" ]; then
            echo_step "  Installing the ThousandEyes public key"
            log_command "apt-key --keyring ./${DEBIAN_PUBLIC_KEY_FILE}.gpg add ${DEBIAN_PUBLIC_KEY_FILE} >> $INSTALL_LOG 2>&1"
            if [ ! -d "/etc/apt/trusted.gpg.d" ]; then
                mkdir -p /etc/apt/trusted.gpg.d
            fi
            mv ${DEBIAN_PUBLIC_KEY_FILE}.gpg /etc/apt/trusted.gpg.d/${DEBIAN_PUBLIC_KEY_FILE}.gpg
            chmod 644 /etc/apt/trusted.gpg.d/${DEBIAN_PUBLIC_KEY_FILE}.gpg
            # apt-key leaves a gpg~ file
            rm -f ${DEBIAN_PUBLIC_KEY_FILE} ${DEBIAN_PUBLIC_KEY_FILE}.gpg~
            cd - >/dev/null  # get out of /etc/apt/sources.list.d
            echo_success
        else
            echo_warning "Failed creating public key file"
        fi
    fi

    update_package_index 2

    #
    # Install the ThousandEyes Agent
    #
    echo_step "  Installing the ThousandEyes Agent"

    if [ -z "$AGENT_VERSION" ]
    then
        INSTALLATION_PACKAGE=$PACKAGE_NAME
    else
        INSTALLATION_PACKAGE="$PACKAGE_NAME=$AGENT_VERSION~$CODENAME"
    fi

    if log_command "apt-get -qq -y install $INSTALLATION_PACKAGE >> $INSTALL_LOG"; then
        echo_success
    else
        exit_with_failure "Failed installing the ThousandEyes Agent"
    fi
}

do_choice() {
    tput smcup
    echo_title "ThousandEyes"

    if [[ "$1" != "" ]]; then
        echo -e "$1"
    fi

    while true; do
        read -r -p "$2 [y/N] "
        if [[ "$REPLY" =~ ^[Yy]$ ]]; then
            CHOICE=1
            break
        elif [[ "$REPLY" =~ ^[nN]$ ]] || [[ "$REPLY" == "" ]]; then
            CHOICE=0
            break
        fi
    done

    tput rmcup

    if [[ $3 == 1 && $CHOICE == 0 ]]; then
        exit_with_failure "Installation aborted"
    fi

    return $CHOICE
}

install_browserbot_debian() {
    echo_step "  Installing ThousandEyes' BrowserBot (Package required for Page Load and Transaction tests)"

    if log_command "apt-get -qq -y install te-browserbot >> $INSTALL_LOG 2>&1"; then
        echo_success
    else
        echo_warning "Failed installing ThousandEyes' BrowserBot"
    fi

    if [ "$INSTALL_BROWSERBOT_WITHOUT_REC_PKGS" = false ]; then
        if log_command "apt-get -qq -y install te-xvfb >> $INSTALL_LOG 2>&1"; then
            echo_success
        else
            echo_warning "Failed installing one of BrowserBot's recommended packages: te-xvfb"
        fi
    fi
}

install_intl_languages_debian() {
    echo_step "  Installing international language support packages"

    if log_command "apt-get -qq -y install te-intl-fonts >> $INSTALL_LOG 2>&1"; then
        echo_success
    else
        echo_warning "Failed installing international language support packages"
    fi
}

# install_redhat() installs ThousandEyes into a RedHat/CentOS system.
install_redhat() {
    echo_step "Installing ThousandEyes (RedHat)"; echo

    #
    # Check for repo override
    #
    if [ -n "$OVERRIDE_REPOSITORY" ]; then
        INSTALL_REPOSITORY="$OVERRIDE_REPOSITORY"
    else
        INSTALL_REPOSITORY="$REDHAT_REPOSITORY"
    fi

    #
    # Check RedHat flavor.
    #
    echo_step "  Detecting RedHat flavor"
    if grep -q "^CentOS release " /etc/redhat-release 2>/dev/null; then
        FLAVOR="CentOS"
        REDHAT_VERSION=$(log_command "cut -f3 -d' ' /etc/redhat-release 2>/dev/null")
    elif grep -q "^CentOS Linux " /etc/redhat-release 2>/dev/null; then
        FLAVOR="CentOS"
        REDHAT_VERSION=$(log_command "cut -f4 -d' ' /etc/redhat-release 2>/dev/null")
    elif grep -q "^Red Hat Enterprise Linux " /etc/redhat-release 2>/dev/null; then
        FLAVOR="RHEL"
        REDHAT_VERSION=$(log_command "grep -oE '[0-9]\.[0-9][0-9]?' /etc/redhat-release 2>/dev/null")
    elif grep -q "^NAME=\"Amazon Linux\"" /etc/os-release 2>/dev/null; then
        FLAVOR="Amazon"
        REDHAT_VERSION=$(log_command "grep \"^VERSION=\" /etc/os-release | cut -f2 -d= | cut -f2 -d\\\"")
    else
        exit_with_failure "Unable to detect RedHat flavor"
    fi

    CODENAME=$(echo $REDHAT_VERSION | cut -f1 -d.)
    REDHAT_MINOR=$(echo $REDHAT_VERSION | cut -f2 -d.)

    echo_step_info "$FLAVOR/$CODENAME"
    check_if_supported "$FLAVOR" "$CODENAME" "$REDHAT_MINOR" && echo_success

    #
    # Check installation tools.
    #
    echo_step "  Checking installation tools"
    command_exists yum || exit_with_failure "Command 'yum' not found"
    command_exists chkconfig || exit_with_failure "Command 'chkconfig' not found"
    command_exists systemctl || exit_with_failure "Command 'systemctl' not found"
    echo_success

    stop_if_running

    if [ "$SKIP_REPO_CREATION" = false ]; then
        #
        # Add yum source.
        #
        echo_step "  Adding repository"
        if [ -d /etc/yum.repos.d ]; then
            cat > /etc/yum.repos.d/thousandeyes.repo <<EOF
[thousandeyes]
name=ThousandEyes
baseurl=${INSTALL_REPOSITORY}/${FLAVOR}/${CODENAME}/${ARCHITECTURE}
gpgkey=file:///etc/pki/rpm-gpg/${REDHAT_PUBLIC_KEY_FILE}
gpgcheck=1
EOF
        else
            exit_with_failure "Package resource directory not found"
        fi
        echo_success

        echo "$PUBLIC_KEY" > ${REDHAT_PUBLIC_KEY_FILE}
        if [ -s "$REDHAT_PUBLIC_KEY_FILE" ]; then
            echo_step "  Installing the ThousandEyes public key"
            mkdir -p /etc/pki/rpm-gpg
            mv ${REDHAT_PUBLIC_KEY_FILE} /etc/pki/rpm-gpg/
            log_command "rpm --import /etc/pki/rpm-gpg/${REDHAT_PUBLIC_KEY_FILE} >> $INSTALL_LOG 2>&1"
            echo_success
        else
            exit_with_failure "Failed creating public key file"
        fi
    fi


    if [ $CODENAME == 8 ]; then
        #
        # Install Epel Repository
        #
        echo_step "  Installing Epel Repository"
        log_command "yum -y -q install epel-release >> $INSTALL_LOG 2>&1"
    fi

    #
    # Install the ThousandEyes Agent
    #
    echo_step "  Installing the ThousandEyes Agent"

    if [ -z "$AGENT_VERSION" ]
    then
        INSTALLATION_PACKAGE=$PACKAGE_NAME
    else
        INSTALLATION_PACKAGE="$PACKAGE_NAME-$AGENT_VERSION"
    fi

    log_command "yum -y -q clean metadata >> $INSTALL_LOG 2>&1"
    if ! log_command "yum -y -q install $INSTALLATION_PACKAGE >> $INSTALL_LOG 2>&1"; then
        exit_with_failure "Failed installing the ThousandEyes Agent"
    else
        echo_success
    fi
}

install_browserbot_redhat() {
    echo_step "Installing Add-ons (RedHat)"; echo

    if [ $CODENAME == 7 ]; then
        if [ -f /etc/oracle-release ]; then
            REPO_CMD="yum-config-manager -q -y --enable ol7_addons"
            REPO_DISPLAY_NAME="Oracle7 Addons"
        elif [ $FLAVOR = "RHEL" ]; then
            REPO_CMD="subscription-manager repos --enable=rhel-7-server-extras-rpms"
            REPO_DISPLAY_NAME="RHEL7 Extras"
        fi
    fi

    if [ ! -z "$REPO_CMD" ]; then
        echo_step  "  Enabling $REPO_DISPLAY_NAME repository"
        if ! log_command "$REPO_CMD >> $INSTALL_LOG 2>&1"; then
            echo_warning "Failed to enable $REPO_DISPLAY_NAME repository"
        else
            echo_success
        fi
    fi

    echo_step "  Installing ThousandEyes' BrowserBot (Package required for Page Load and Transaction tests)"
    if ! log_command "yum -y -q install te-browserbot >> $INSTALL_LOG 2>&1"; then
        echo_warning "Failed installing ThousandEyes' BrowserBot"
    else
        echo_success
    fi

    if [ "$INSTALL_BROWSERBOT_WITHOUT_REC_PKGS" = false ]; then
        if ! log_command "yum -y -q install te-xvfb >> $INSTALL_LOG 2>&1"; then
            echo_warning "Failed installing one of BrowserBot's recommended packages: te-xvfb"
        else
            echo_success
        fi
    fi
}

install_intl_languages_redhat() {
    echo_step "  Installing international language support packages"
    if ! log_command "yum -y -q install te-intl-fonts >> $INSTALL_LOG 2>&1"; then
        echo_warning "Failed installing international language support packages"
    else
        echo_success
    fi
}

# configure_agent() sets up configuration files and startup.
configure_agent() {
    # If we are installing, we are (re)configuring the agent - always.
    cp /etc/te-agent.cfg.sample $TE_AGENT_CFG_LOCATION
    echo_step "Configuring ThousandEyes"; echo
    #
    # Log path selection
    #
    DEFAULT_LOG_PATH=/var/log
    echo_step "  Selecting log path"
    if [ -n "$CMD_LOG_LOCATION" ]; then
        TEAGENT_LOG=$CMD_LOG_LOCATION
    elif [ "$BATCH_MODE" = true ]; then
        TEAGENT_LOG=$DEFAULT_LOG_PATH
    else
        TEAGENT_LOG=$DEFAULT_LOG_PATH
        CHOICE_MADE=""
        tput smcup
        echo_title "ThousandEyes"
        while [ ! -n "$CHOICE_MADE" ]; do
            read -r -p "The default log path is ${DEFAULT_LOG_PATH}. Do you want to change it [y/N]? "
            if [[ "$REPLY" =~ ^[Yy][Ee][Ss]$|^[Yy]$ ]]; then
                while true; do
                    read -r -p "Please enter new log path: " LOCATION
                    if [[ -d $LOCATION ]]; then
                        # if the location is a directory, the choice has been made. Add
                        TEAGENT_LOG=$LOCATION
                        # the log filename to it.
                        CHOICE_MADE=yes
                        break
                    else
                        echo -n "$LOCATION is not a valid path. "
                    fi
                done
            elif [[ "$REPLY" =~ ^[Nn][Oo]$|^[Nn]$ ]] || [[ "$REPLY" = "" ]]; then
                # Answering no (or pressing enter, i.e., default) breaks the cycle.
                break
            fi
        done
        tput rmcup
    fi
    echo_step_info "$TEAGENT_LOG"
    echo_success
    #
    # Proxy selection
    #
    if [ -n "$CMD_PROXY_TYPE" ]; then
        echo_step "  Selecting proxy type"
        echo_step_info "$CMD_PROXY_TYPE"
        echo_success
    fi
    if [ -n "$CMD_PROXY_AUTH_TYPE" ]; then
        echo_step "  Selecting proxy auth type"
        echo_step_info "$CMD_PROXY_AUTH_TYPE"
        echo_success
    fi
    if [ -n "$CMD_PROXY_LOCATION" ]; then
        echo_step "  Selecting proxy location"
        echo_step_info "$CMD_PROXY_LOCATION"
        echo_success
    fi
    if [ -n "$CMD_PROXY_USER" ]; then
        echo_step "  Selecting proxy user"
        echo_step_info "$CMD_PROXY_USER"
        echo_success
    fi
    if [ -n "$CMD_PROXY_PASS" ]; then
        echo_step "  Selecting proxy pass"
        echo_step_info "$CMD_PROXY_PASS"
        echo_success
    fi

    #
    # Configuration file creation
    #
    echo_step "  Creating configuration file"

    if ! (
            set -e # If one sed fails, all seds fail.
            # The sed doesn't like /s.
            ESCAPED_TEAGENT_LOG=$(echo "$TEAGENT_LOG" | sed 's/\//\\\//g')
            ESCAPED_ACCOUNT_TOKEN=$(echo "$ACCOUNT_TOKEN" | sed 's/\//\\\//g')
            sed -i "s/log-path=\/var\/log/log-path=${ESCAPED_TEAGENT_LOG}/" $TE_AGENT_CFG_LOCATION
            sed -i "s/<account-token>/${ESCAPED_ACCOUNT_TOKEN}/" $TE_AGENT_CFG_LOCATION
            if [ -n "$CMD_PROXY_TYPE" ]; then
                if grep -q "^proxy-type=" $TE_AGENT_CFG_LOCATION 2>/dev/null; then
                    sed -i "s/proxy-type=.*/proxy-type=${CMD_PROXY_TYPE}/" $TE_AGENT_CFG_LOCATION
                else
                    # proxy-type is currently not in the packaged config file, so we need to add it
                    echo "proxy-type=${CMD_PROXY_TYPE}" >> $TE_AGENT_CFG_LOCATION
                fi
            fi
            if [ -n "$CMD_PROXY_LOCATION" ] || [ "$CMD_PROXY_TYPE" == "DIRECT" ]; then
                # set proxy-location if one was specified OR the proxy type was direct
                # NOTE: if the type is DIRECT, the location is ensured to be
                # empty
                ESCAPED_PROXY_LOCATION=$(echo "$CMD_PROXY_LOCATION" | sed 's/\//\\\//g')
                if grep -q "^proxy-location=" $TE_AGENT_CFG_LOCATION 2>/dev/null; then
                    sed -i "s/proxy-location=.*/proxy-location=${ESCAPED_PROXY_LOCATION}/" $TE_AGENT_CFG_LOCATION
                else
                    # proxy-location is currently not in the packaged config file, so we need to add it
                    # NOTE: don't escape this one!
                    echo "proxy-location=${CMD_PROXY_LOCATION}" >> $TE_AGENT_CFG_LOCATION
                fi
            fi
            if [ -n "$CMD_PROXY_USER" ]; then
                ESCAPED_PROXY_USER=$(echo "$CMD_PROXY_USER" | sed 's/\//\\\//g')
                sed -i "s/proxy-user=.*/proxy-user=${ESCAPED_PROXY_USER}/" $TE_AGENT_CFG_LOCATION
            fi
            if [ -n "$CMD_PROXY_PASS" ]; then
                ESCAPED_PROXY_PASS=$(echo "$CMD_PROXY_PASS" | sed 's/\//\\\//g')
                sed -i "s/proxy-pass=.*/proxy-pass=${ESCAPED_PROXY_PASS}/" $TE_AGENT_CFG_LOCATION
            fi
            if [ -n "$CMD_PROXY_AUTH_TYPE" ]; then
                if grep -q "^proxy-auth-type=" $TE_AGENT_CFG_LOCATION 2>/dev/null; then
                    sed -i "s/proxy-auth-type=.*/proxy-auth-type=${CMD_PROXY_AUTH_TYPE}/" $TE_AGENT_CFG_LOCATION
                else
                    # proxy-auth-type is currently not in the packaged config file, so we need to add it
                    echo "proxy-auth-type=${CMD_PROXY_TYPE}" >> $TE_AGENT_CFG_LOCATION
                fi
            fi
         ); then
        exit_with_failure "Failed creating configuration file"
    else
        echo_success
    fi
}

start_services() {
    echo_step "Starting ThousandEyes"; echo
    if [ "$INSTALL_BROWSERBOT" = true ]; then
        echo_step "  Starting ThousandEyes' BrowserBot"
        if ! service_is_running "te-browserbot"; then
            # If the te-browserbot post-install script did not start the service
            # (i.e. because this is not the first time te-browserbot is installed)
            # we have to start it manually.
            start_service "te-browserbot"
        fi
        if [ "$INSTALL_BROWSERBOT_WITHOUT_REC_PKGS" = false ] && ! service_is_running "te-xvfb"; then
            # If the te-xvfb post-install script did not start the service
            # (i.e. because this is not the first time te-xvfb is installed)
            # we have to start it manually.
            start_service "te-xvfb"
        fi
        if service_is_running "te-browserbot"; then
            echo_success
        else
            echo_warning "Failed starting ThousandEyes' BrowserBot"
        fi
    fi
    echo_step "  Starting the ThousandEyes Agent"
    start_service "te-agent"
    sleep 2
    if service_is_running "te-agent"; then
        echo_success
    else
        exit_with_failure "Failed starting the ThousandEyes Agent. Please check $TEAGENT_LOG."
    fi
}

stop_if_running() {
    if service_is_running "te-agent"; then
        echo_step "Stopping the ThousandEyes Agent"
        if ! stop_service "te-agent"; then
            echo_warning "Failed stopping the ThousandEyes Agent"
        else
            echo_success
        fi
    fi
    if service_is_running "te-browserbot"; then
        echo_step "Stopping ThousandEyes' BrowserBot"
        if ! stop_service "te-browserbot"; then
            echo_warning "Failed stopping ThousandEyes' BrowserBot"
        else
            echo_success
        fi
    fi
}

################################################################################
# Other helpers
################################################################################

# debug_variables() print all script global variables to ease debugging
debug_variables() {
    echo "ACCOUNT_TOKEN: $ACCOUNT_TOKEN"
    echo "ARCHITECTURE: $ARCHITECTURE"
    echo "OPERATING_SYSTEM: $OPERATING_SYSTEM"
    echo "FLAVOR/CODENAME: $FLAVOR/$CODENAME"
    echo "BROWSERBOT: $INSTALL_BROWSERBOT"
    echo "EXCLUDE BROWSERBOT'S RECOMMENDED PKGS: $INSTALL_BROWSERBOT_WITHOUT_REC_PKGS"
}

# check_if_supported() verifies if an operating system $FLAVOR/$CODENAME
# is supported and exits otherwise.
check_if_supported() {
    local FLAVOR=$1
    local DISTRO_VERSION=$2
    local REDHAT_MINOR=$3

    case $FLAVOR in
        Ubuntu)
            case $DISTRO_VERSION in
                bionic|focal)
                ;;
                *)
                    unsupported_os
                ;;
            esac
        ;;
        CentOS)
            case $DISTRO_VERSION in
                7)
                    if [[ $REDHAT_MINOR -lt 8 ]]; then
                        unsupported_os
                    fi
                ;;
                *)
                    unsupported_os
                ;;
            esac
            ;;
        RHEL)
            case $DISTRO_VERSION in
                7)
                    if [[ $REDHAT_MINOR -lt 8 ]]; then
                        unsupported_os
                    fi
                ;;
                8)
                    if [[ $REDHAT_MINOR -lt 2 ]]; then
                        unsupported_os
                    fi
                ;;
                *)
                    unsupported_os
                ;;
            esac
        ;;
        Amazon)
            case $DISTRO_VERSION in
                2)
                ;;
                *)
                    unsupported_os
                ;;
            esac
            if [[ "$INSTALL_BROWSERBOT" = true ]]; then
                browserbot_unsupported_os
            fi
        ;;
        *)
            unsupported_os
        ;;
    esac

    if [ "$ARCHITECTURE" == "aarch64" ] && [ "$DISTRO_VERSION" != "bionic" ]; then
        exit_with_failure "Unsupported architecture ($ARCHITECTURE) for $FLAVOR $DISTRO_VERSION"
    fi
}

# command_exists() tells if a given command exists.
command_exists() {
    command -v "$1" >/dev/null 2>&1
}

# bash native function for URI encoding
urlencode() {
    # urlencode <string>
    local length="${#1}"
    for (( i = 0; i < length; i++ )); do
        local c="${1:i:1}"
        case $c in
            [a-zA-Z0-9.~_-]) printf "%s" "$c";;
            *) printf '%%%02X' "'$c"
        esac
    done
}

# use the given INSTALL_LOG or set it to a random file in /tmp
set_install_log() {
    if [[ ! $INSTALL_LOG ]]; then
        command_exists tr || exit_with_failure "Command 'tr' not found. Use -I to set the INSTALL_LOG."
        command_exists head || exit_with_failure "Command 'head' not found. Use -I to set the INSTALL_LOG."
        LOG_HASH=$(< /dev/urandom tr -dc A-Z-a-z-0-9 | head -c"${1:-10}";echo;)
        export INSTALL_LOG="/tmp/install_thousandeyes_$LOG_HASH.log"
    fi
}

usage() {
    cat << EOF
Usage: $0 [-b [-L] [-W]] [-f] [-h] [-I INSTALL_LOG] [-l LOG_PATH] [-t PROXY_TYPE -P PROXY_LOCATION [-U PROXY_USER -u PROXY_PASS]] [-r REPO] [-s] [-v AGENT_VERSION] [-O] ACCOUNT_TOKEN
  -b                     Also install BrowserBot, an agent component that collects
                         Page Load and Transaction test data using an instance
                         of the Chromium browser
  -L                     Also install international language packages for BrowserBot (requires -b)
  -W                     Install BrowserBot without its recommended packages (e.g. te-xvfb) (requires -b)
  -f                     Force batch mode
  -h                     Print this message
  -I <INSTALL_LOG>       Set the install log location to INSTALL_LOG
  -l <LOG_PATH>          Set the log path to LOG_PATH
  -t <PROXY_TYPE>        Set the proxy type: DIRECT (default, no proxy), STATIC, or PAC
  -P <PROXY_LOCATION>    Set the proxy location, format depends on PROXY_TYPE
                           DIRECT
                             PROXY_LOCATION is an invalid option for DIRECT
                           STATIC
                             host:port for hostname or IPv4 address
                             [IPv6 IP]:port for IPv6 address
                           PAC
                             URL where PAC file can be found
  -U <PROXY_USER>        Set the proxy user to PROXY_USER
  -u <PROXY_PASS>        Set the proxy password to PROXY_PASS
  -a <PROXY_AUTH_TYPE>   Set the proxy authentication type: BASIC (default), NTLM
  -r <REPO>              Force the installer to install from REPO (overriding original ones)
  -s                     Skip the repository creation
  -v <AGENT_VERSION>     Specify agent version
  -O                     Install the agent, but do not start the agent services
EOF
    exit 1
}

urlencode() {
    # urlencode <string>
    local length="${#1}"
    for (( i = 0; i < length; i++ )); do
        local c="${1:i:1}"
        case $c in
            [a-zA-Z0-9.~_-]) printf "%s" "$c" ;;
            *) printf '%%%02X' "'$c"
        esac
    done
}

# main()

INSTALL_BROWSERBOT=false
INSTALL_BROWSERBOT_WITHOUT_REC_PKGS=false
BATCH_MODE=false
INTL_LANG_SUPPORT=false
SKIP_REPO_CREATION=false
CMD_PROXY_TYPE="DIRECT"
INSTALL_ONLY_FLAG=false

while getopts ":hbWLOI:l:ft:P:r:v:sU:u:a:" OPTIONS; do
    case ${OPTIONS} in
        h) usage;;
        b)
            INSTALL_BROWSERBOT=true
        ;;
        W)
            INSTALL_BROWSERBOT_WITHOUT_REC_PKGS=true
        ;;
        I)
            INSTALL_LOG=$OPTARG
        ;;
        l)
            CMD_LOG_LOCATION=$OPTARG
        ;;
        f)
            BATCH_MODE=true
        ;;
        t)
            CMD_PROXY_TYPE=$OPTARG
        ;;
        P)
            CMD_PROXY_LOCATION=$OPTARG
        ;;
        U)
            CMD_PROXY_USER=$OPTARG
        ;;
        u)
            CMD_PROXY_PASS=$OPTARG
        ;;
        a)
            CMD_PROXY_AUTH_TYPE=$OPTARG
        ;;
        r)
            OVERRIDE_REPOSITORY=$OPTARG
        ;;
        v)
            AGENT_VERSION=$OPTARG
        ;;
        s)
            SKIP_REPO_CREATION=true
        ;;
        L)
            INTL_LANG_SUPPORT=true
        ;;
        O)
            INSTALL_ONLY_FLAG=true
        ;;
        \?) usage;;
    esac
done

shift $((OPTIND-1))

if [ "$#" != "1" ]; then
    usage
elif [ "$CMD_PROXY_TYPE" != "STATIC" ] && [ "$CMD_PROXY_TYPE" != "PAC" ] && [ "$CMD_PROXY_TYPE" != "DIRECT" ]; then
    echo "Proxy type must be DIRECT, STATIC, or PAC"
    usage
elif [ "$CMD_PROXY_TYPE" != "DIRECT" ] && [ -z "$CMD_PROXY_LOCATION" ]; then
    echo "Proxy type was $CMD_PROXY_TYPE but no proxy location was set"
    usage
elif [ "$CMD_PROXY_TYPE" == "DIRECT" ] && [ "$CMD_PROXY_LOCATION" ]; then
    echo "Proxy type was DIRECT but proxy location was set"
    usage
elif [ -n "$CMD_PROXY_PASS" ] && [ -z "$CMD_PROXY_USER" ]; then
    echo "Proxy password specified but no proxy user was set"
    usage
elif [ -n "$CMD_PROXY_USER" ] && [ -z "$CMD_PROXY_PASS" ]; then
    echo "Proxy user specified but no proxy password was set"
    usage
elif [ -n "$CMD_PROXY_AUTH_TYPE" ]; then
    if [ "$CMD_PROXY_AUTH_TYPE" != "BASIC" ] && [ "$CMD_PROXY_AUTH_TYPE" != "NTLM" ]; then
        echo "Proxy auth type must be BASIC or NTLM"
        usage
    fi
    if [ -z "$CMD_PROXY_LOCATION" ] || [ -z "$CMD_PROXY_USER" ] || [ -z "$CMD_PROXY_PASS" ]; then
        echo "Proxy auth type specified without location, user or pass"
        usage
    fi
elif [ "$INTL_LANG_SUPPORT" = true ] && [ "$INSTALL_BROWSERBOT" = false ] ; then
    echo "International language support specified but BrowserBot is not to be installed"
    usage
elif [ "$INSTALL_BROWSERBOT_WITHOUT_REC_PKGS" = true ] && [ "$INSTALL_BROWSERBOT" = false ] ; then
    echo "Installation without Browserbot's recommended packages is specified but BrowserBot is not to be installed"
    usage
fi

if [ -n "$CMD_PROXY_LOCATION" ] && [ -n "$CMD_PROXY_USER" ] && [ -n "$CMD_PROXY_PASS" ]; then
    # We have a valid proxy config, default PROXY_AUTH_METHOD to BASIC if unset
    CMD_PROXY_AUTH_TYPE=${CMD_PROXY_AUTH_TYPE-BASIC}
fi

ACCOUNT_TOKEN="$1"

set_install_log

echo_title "Welcome to ThousandEyes"
check_if_root_or_die
detect_architecture
detect_operating_system

case $OPERATING_SYSTEM in
    DEBIAN)
        install_debian
    ;;
    REDHAT)
        install_redhat
    ;;
esac

configure_agent

if [ "$INSTALL_BROWSERBOT" = true ]; then
    case $OPERATING_SYSTEM in
        DEBIAN)
            install_browserbot_debian
        ;;
        REDHAT)
            install_browserbot_redhat
        ;;
    esac
fi

if [ "$INTL_LANG_SUPPORT" = true ]; then
    case $OPERATING_SYSTEM in
        DEBIAN)
            install_intl_languages_debian
        ;;
        REDHAT)
            install_intl_languages_redhat
        ;;
    esac
fi

if [ "$INSTALL_ONLY_FLAG" = true ]; then
    echo "Install only flag is set, agent installed without starting the agent services"
else
    start_services
fi
