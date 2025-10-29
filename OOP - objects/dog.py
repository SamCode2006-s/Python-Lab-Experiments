class Dog:
    species="German Shepard"
    def __init__(self, name, age):
        self.name=name
        self.age=age
    def bark(self):
        print(f"{self.name} barks: Woof! Woof!")
    def get_info(self):
        return f"{self.name} is a {self.age}-year-old {self.species}."

if __name__=="__main__":
    dog1=Dog("Buddy",3)
    dog2=Dog("Lucy",5)
    print(f"Dog 1's name is {dog1.name} and age is {dog1.age}.")
    print(f"Dog 2's name is {dog2.name} and age is {dog2.age}.")
    print(f"Both dogs are of species: {Dog.species}")
    print("\n--- Calling Methods ---")
    dog1.bark()
    dog2.bark()
    print("\n--- Object Information ---")
    print(dog1.get_info())
    print(dog2.get_info())