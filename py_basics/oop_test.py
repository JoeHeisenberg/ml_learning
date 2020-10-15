import os


class Object():
    pass


class Teacher(Object):
    def run(self):
        print('Start!!!')


class Student(Object):
    def __init__(self, name, score, age):
        self.name = name
        self.score = score
        self.__age = age

    def get_age(self):
        return self.__age

    def print(self):
        print('%s:%s:%s' % (self.name, self.score, self.__age))

    def run(self):
        print('start....run')


def runT(student):
    student.run()


if __name__ == '__main__':
    p = Student("haha", 97, 23)
    p.print()
