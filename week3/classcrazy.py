class animal:
    def hasBlood(self):
        return True

class mammal(animal):
    def hasFur(self):
        return True

    @classmethod
    def animalType(cls):
        return 'Mammal'

class lizard(animal):
    def hasFur(self):
        return False

print(__name__)

if __name__ == '__main__':
    kitty = mammal()
    print(kitty.hasFur()) # True
    print(kitty.hasBlood())

    dragon = lizard()
    print(dragon.hasFur()) # False
    print(dragon.hasBlood())
    # dragon = mammal()
    # print(dragon.hasFur())

    #hasFur() # ERROR!

    print(mammal.hasFur(kitty))
    print(mammal.animalType())
    print(kitty.animalType())
