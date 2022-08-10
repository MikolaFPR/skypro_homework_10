class Candidate:
    """Класс для простоты работы с данными"""
    def __init__(self, pk, name, position, skills, picture):
        self.pk = pk
        self.name = name
        self.position = position
        self.skills = skills
        self.picture = picture

    def __repr__(self):
        """Строковое представление класса"""
        return f'Имя кандидата - {self.name}\nПозиция кандидата - {self.position}\nНавыки - {self.skills}\n'
