#!/usr/bin/env python
def get_ent_agents():
    """
    calls the te api to get a list of enterprise agent ids in a json dictionary format
    :return: list of enterprise agents in a dictionary
    """

    token = os.getenv('TE_OATHTOKEN')
    url = "https://api.thousandeyes.com/v6/agents.json"
    payload={}
    headers = {'Authorization': 'Bearer ' + token}
    agent_response = requests.request("GET", url, headers=headers, data=payload)

    agent_list_json = agent_response.json()
    agent_list = agent_list_json['agents']
    list_of_dictionaries = agent_list
    sought_value = "Enterprise"
    found_values = []
    for dictionary in list_of_dictionaries:
        if (dictionary["agentType"] == "Enterprise"):
            found_values.append(dictionary)
    print(found_values)

    empty_list=[]
    for item in found_values:
        agentId=item['agentId']
        print(agentId)
        empty_list.append({'agentId': agentId})
    return(empty_list)





