class Cat:
    def __init__(self, name, bark, age=None, person_age=None):
        self.name = name
        self.bark = bark
        self.age = age
        self.person_age = person_age

    def __repr__(self):
        return repr(f"{self.name} says {self.bark}")

    def __eq__(self, other):
        # сравнение двух прямоугольников

        print(self.age == other)
        # иначе возвращаем NotImplemented
        return NotImplemented


my_cat = Cat("Sharik", "WOOF!",12)

print(my_cat)
my_cat.__eq__(12)
