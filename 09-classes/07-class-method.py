class Person:
    population = 0

    def __init__(self, name):
        self.name = name
        Person.increse_population() # 클래스 메서드 호출은 클래스가 하는 거임

    @classmethod
    def increse_population(cls):
        cls.population += 1

person1 = Person('Alice')
person2 = Person('Bob')
print(Person.population)  #2 #인스턴스가 생성될 떄 마다 1씩 증가하므로 2임

