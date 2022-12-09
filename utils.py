import json


# load all of our candidates
def load_candidates_from_json(path) -> list[dict]:
    return json.load(open(path, encoding='utf8'))


# load information on id about candidate
def get_candidate(candidate_id) -> dict:
    return [candidate for candidate in load_candidates_from_json('candidates.json') if candidate['id'] == candidate_id][0]


# load list with candidates by name
def get_candidates_by_name(candidate_name) -> list[dict]:
    return [i for i in load_candidates_from_json('candidates.json') if candidate_name.lower() in i["name"].lower()]


# load list with candidates by skill
def get_candidates_by_skill(skill_name) -> list[dict]:
    return [i for i in load_candidates_from_json('candidates.json') if skill_name.lower() in i["skills"].lower()]
