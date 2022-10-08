import json

def load_candidates():

    with open('candidates.json', 'r', encoding='utf-8') as file:
        return json.load(file)

  #  return candidates_json

def get_all():
    return load_candidates()

def get_by_pk(pk):
    for i in load_candidates():
        if i["pk"] == pk:
            return i
    return 'Not found'

def get_by_skill(skill_name):
    result = []
    for i in load_candidates():
        if skill_name.lower() in i["skills"].lower().split(', '):
            result.append(i)
    return result