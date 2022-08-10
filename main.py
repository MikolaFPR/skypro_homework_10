from flask import Flask
from functions import get_all, load_condidates, get_by_pk, get_by_skill

# Обозначение констант и важных переменных
FILENAME = "candidates.json"
data = get_all(load_condidates(FILENAME))
app = Flask(__name__)


# Создание маршрутов
# / - корень
# /candidates/цифра - поиск кандитата по номеру
# /skills/название скила - поиск кандидатов по запрашиваемому скилу
@app.route('/')
def index():
    output = '<pre>'
    for i in data:
        output += f'{i}\n'
    output += '</pre>'
    return output


@app.route('/candidates/<int:pk>')
def get_user(pk):
    user = get_by_pk(pk, data)
    if user:
        output = f'<img src = "{user.picture}">'
        output += f'<pre>{user}</pre>'
    else:
        output = "NOT FOUND"
    return output


@app.route('/skills/<skill_name>')
def get_skills(skill_name):
    skill_name = skill_name.lower()
    skill = get_by_skill(skill_name, data)
    if skill:
        output = '<pre>'
        for i in skill:
            output += f'{i}\n'
        output += '</pre>'
    else:
        output = "NOT FOUND"
    return output


if __name__ == '__main__':
    app.run(port=5000)
