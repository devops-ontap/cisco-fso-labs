def get_agent_ids():
    """
    This function will find the agentIds
    :param agentType: The type of Agent, ie) Enterprise
    :return: the agentId
    """
    oath_token = os.getenv('TE_OATHTOKEN')
    agents_file = 'agents.json'
    TE_URL = 'https://api.thousandeyes.com'
    room_id = None
    room_id_list = []
    url = TE_URL + '/v6/agents.json'
    header = {'content-type': 'application/json', 'authorization': oath_token}
    space_response = requests.get(url, headers=header, verify=False)
    space_list_json = space_response.json()
    space_list = space_list_json['agents']
    for spaces in space_list:
        room_id = spaces['id']
        room_id_list.append(room_id)
    return room_id_list


'''
 def get_room_ids():
    """
    This function will find the Webex Teams space ids
    Call to Webex Teams - /rooms
    :param room_name: The Webex Teams room name
    :return: the Webex Teams room Id
    """
    room_id = None
    room_id_list = []
    url = WEBEX_TEAMS_URL + '/v1/rooms' + '?sortBy=lastactivity&max=1000'
    header = {'content-type': 'application/json', 'authorization': WHATSOP_BOT_AUTH}
    space_response = requests.get(url, headers=header, verify=False)
    space_list_json = space_response.json()
    space_list = space_list_json['items']
    for spaces in space_list:
        room_id = spaces['id']
        room_id_list.append(room_id)
    return room_id_list


def post_room_message_all(room_ids_list, message):
    """
    This function will post the {message} to the Webex Teams space with the {space_name}
    Call to function get_space_id(space_name) to find the space_id
    Followed by API call /messages
    :param space_name: the Webex Teams space name
    :param message: the text of the message to be posted in the space
    :return: API call response
    """
    for ids in room_ids_list:
        payload = {'roomId': ids, 'text': message}
        url = WEBEX_TEAMS_URL + '/v1/messages'
        header = {'content-type': 'application/json', 'authorization': WHATSOP_BOT_AUTH}
        response = requests.post(url, data=json.dumps(payload), headers=header, verify=False)
        return response 


'''