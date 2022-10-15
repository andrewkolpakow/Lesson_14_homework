import json

def load_candidates():
    with open('candidates.json', 'r', encoding = 'utf-8') as file:
        return json.load(file)

def get_candidate(pk):
    for candidate in load_candidates():
        if candidate['id'] == pk:
            return candidate
    #return {}

def get_candidate_by_name(candidate_name):
    result = []
    for candidate in load_candidates():
        if candidate_name.lower() in candidate['name'].lower().split():
            result.append(candidate)
    return result

def get_candidates_by_skill(skill_name):
    result = []
    for candidate in load_candidates():
        if skill_name.lower() in candidate["skills"].lower().split(', '):
            result.append(candidate)
    return result

