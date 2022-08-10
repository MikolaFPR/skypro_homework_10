import json
from candidate import Candidate


def load_condidates(file):
    """Выгружает данные из файла в языке python"""
    with open(file, 'r', encoding="UTF-8") as f:
        profile = json.load(f)
    return profile


def get_all(file):
    """Показывает имена всех кондидатов (Имя, должность, скилы)"""
    candidates = []
    for i in file:
        person = Candidate(i['pk'], i['name'], i['position'], i['skills'].lower(), i['picture'])
        candidates.append(person)
    return candidates


def get_by_skill(skill_name, candidates):
    """Возвращает списко студентов по нужному скиллу"""
    student = []
    for i in candidates:
        if skill_name in i.skills:
            student.append(i)
    return student


def get_by_pk(pk, candidates):
    """Возвращает информацию о студенте по номеру его pk"""
    for i in candidates:
        if i.pk == pk:
            return i
