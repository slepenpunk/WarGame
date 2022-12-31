class Cat:
    def __init__(self, age, color):
        self.validate_age(age)

        self.__age = age
        self.__color = color

    @classmethod
    def validate_age(cls, age):
        if type(age) != int or age not in range(0, 10):
            raise TypeError

    @property
    def age(self):
        return self.__age

    @property
    def color(self):
        return self.__color

    @age.setter
    def age(self, new_age):
        self.validate_age(new_age)
        self.__age = new_age

    def __str__(self):
        rep = f'Age - {self.age}\n' \
              f'Color - {self.color}'
        return rep


c1 = Cat(4, 'Green')
print(c1)
c1.age = 11
print(c1)
