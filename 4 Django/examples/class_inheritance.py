class Animal:
    def __init__(self, is_friendly):
        self.is_friendly = is_friendly


class Pet(Animal):  # Pet now inherits all of the methods and attributes of Animal
    def __init__(self, name, noise):
        # overriding the init method because I want different parameters
        self.noise = noise
        self.name = name
        # hard coding is_friendly for all pets
        # the parameter no longer needed in constructor
        self.is_friendly = True

    def speak(self):
        print(self.noise)

    def __str__(self):
        return f'pet named {self.name}'


class Dog(Pet):
    def __init__(self, name, noise, best_friend):
        # Pet.__init__(self, name, noise)
        super().__init__(name, noise)  # calling the parent init method
        self.best_friend = best_friend
        self.name = f'best boy ever named {name}'  # overriding this attribute


class Cat(Pet):
    # no need to change the init or attributes from the superclass
    def speak(self):  # just overriding the speak() method
        print('Viva la revolution')


fido = Dog('Fido', 'yap yap', 'Granny')
fido.speak()
print(fido.best_friend)
# print(fido.is_friendly)

# snowball = Cat('Snowball', 'meow')
# snowball.speak()
