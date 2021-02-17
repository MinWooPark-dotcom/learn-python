class Student:
    def study(self):
        print('공부합니다.')


class Teacher:
    def teach(self):
        print('가르칩니다')


classroom = [Student(), Student(), Teacher(), Student(), Student()]

for person in classroom:
    if isinstance(person, Student):
        person.study()
    elif isinstance(person, Teacher):
        person.teach()

# 공부합니다.
# 공부합니다.
# 가르칩니다
# 공부합니다.
# 공부합니다.
