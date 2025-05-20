#!/usr/bin/env python3

APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

class Dog:
    def __init__(self, name="Fido", breed="Beagle"):
        self.name = name
        self.breed = breed

    # -------- Name Property --------
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and 1 <= len(value) <= 25:
            self._name = value
        else:
            print("Name must be string between 1 and 25 characters.")

    # -------- Breed Property --------
    @property
    def breed(self):
        return self._breed

    @breed.setter
    def breed(self, value):
        if value in APPROVED_BREEDS:
            self._breed = value
        else:
            print("Breed must be in list of approved breeds.")



dog1 = Dog(name="Rex", breed="Corgi")
print(dog1.name)   # Rex
print(dog1.breed)  # Corgi

dog2 = Dog(name="", breed="Dinosaur")
# => Name must be string between 1 and 25 characters.
# => Breed must be in list of approved breeds.

dog2.name = "Fluff"
dog2.breed = "Pug"
print(dog2.name)   # Fluff
print(dog2.breed)  # Pug