class Animal:
    # __init__ methods are where you initialize each instance of the class Animal
    # while initializing each instance, you set that Animal's attributes
    def __init__(self, name, species, noise, hp, jump_height, step_height, attack):
        """
        Class Animal contains important attributes about each declared animal.
        - name: The animal's name (e.g. "Kevin")
        - species: The animal's species (e.g. "cat")
        - noise: The noise the animal makes (e.g. "meow")
        - hp: The animal's hit points
        - jump_height: How high the animal can jump in feet (e.g. 10)
        - step_height: How high the animal can step in feet (e.g. 1)
        - attack: The damage given to opponents if an attack is successful (e.g. 5)
        """
        # after passing in attributes, we assign them to "self"
        # think of "self" as "this particular Animal"
        self.name = name
        self.species = species
        self.noise = noise
        self.hp = hp
        self.jump_height = jump_height
        self.step_height = step_height
        self.attack = attack
    
    def make_noise(self):
        print(self.noise)
    
    def introduction(self):
        """
        Docstrings can be added to any Class method
        """
        vowels = ['a','e','i','o','u']

        # this commented-out chunk of code does the same thing as the conditional expression in line 42

        # species_first_letter = self.species[0].lower()
        # if species_first_letter in vowels:
        #     article = 'an'
        # else:
        #     article = 'a'

        print(f'{self.noise}! My name is {self.name} and I am {"an" if self.species[0].lower() in vowels else "a"} {self.species}. I have {self.hp} hp.')
    
    def get_up(self, height):
        print(f'{self} is trying to get on a surface {height} {"foot" if height == 1 else "feet"} tall.')

        if height <= self.step_height:
            print(f'{self.name} stepped onto the surface.')
            return True
        elif height <= self.jump_height:
            print(f'{self.name} jumped onto the surface.')
            return True
        else:
            damage = self.jump_height * .5
            self.hp -= damage
            print(f'Ouch! {self.name} tried to jump but failed. They took {damage} points of damage and have {self.hp} hp remaining.')
            return False

    def fight(self,opponent,height):
        if not self.get_up(height):
            print(f'{self.name} couldn\'t get into the ring and forfeited the fight.')
            return # using return to break out of the method
        if not opponent.get_up(height):
            print(f'{opponent.name} couldn\'t get into the ring and forfeited the fight.')
            return # using return to break out of the method
        
        from random import random

        if random() > 0.5:
            print(f'{self}\'s attack was successful!')
            opponent.hp -= self.attack
            print(f'\n{opponent} took {self.attack} points of damage and has {opponent.hp} hp remaining. \n\n')
        else:
            print(f'{opponent}\'s attack was successful!')
            self.hp -= opponent.attack
            print(f'\n{self} took {opponent.attack} points of damage and has {self.hp} hp remaining. \n\n')

    
    def __str__(self):
        return self.name


# matt = Animal('Matt','human','talking')

# excited_matt = matt.name + '!'
# print(matt.noise)
# print(excited_matt)

# matt.make_noise()

# print(matt)


# print(kevin)

# kevin.introduction()
# erin.introduction()
# import random
# kevin.get_up(random.randint(0,40))
# kevin.get_up(random.randint(50,99))

if __name__ == '__main__':
    kevin = Animal('Kevin','cat','meow',9*9,40,1,10)
    erin = Animal('Erin','echidna','arf',49,12,.5,20)

    from time import sleep

    i = 0

    while True:
        if i % 2 == 0:
            fighter1 = kevin
            fighter2 = erin
        else:
            fighter1 = erin
            fighter2 = kevin
        
        fighter1.fight(fighter2,10)

        if kevin.hp <= 0:
            print(f'{kevin} has been incapacitated. {erin} has won the fight with {erin.hp} hp remaining!')
            break
        elif erin.hp <= 0:
            print(f'{erin} has been incapacitated. {kevin} has won the fight with {kevin.hp} hp remaining!')
            break

        i += 1
        sleep(2)
