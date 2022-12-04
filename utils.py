
import json

filename = "candidates.json"

def load_candidates(filename):
    """загрузит данные из файла"""

    with open(filename, "r", encoding="utf-8") as file:

        return json.load(file)


def get_all():
    """покажет всех кандидатов"""

    return load_candidates(filename)


def get_by_pk(pk):
    """вернет кандидата по pk"""

    for candidate in load_candidates(filename):
        if candidate["pk"] == int(pk):
            return candidate
    return



def get_by_skill(skill_name):
    """вернет кандидатов по навыку"""

    candidates_with_skill = []

    for candidate in load_candidates(filename):
        if skill_name.lower() in candidate["skills"].lower().split(", "):
            candidates_with_skill.append(candidate)
    return candidates_with_skill



print(get_by_skill("python"))