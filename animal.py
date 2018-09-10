class Animal:
    def __init__(self, name, health):
        self.name = name
        self.health = health
    def walk(self):
        self.health -= 1
        return self
    def run(self):
        self.health -= 5
        return self
    def display_health(self):
        print("Health:", self.health)
        return self

# animal1 = Animal("Cat")
# animal1.display_health().walk().walk().walk().run().run().display_health()

class Dog(Animal):
    def __init__(self):
        super().__init__("dog", 150)
    def pet(self):
        self.health += 5
        return self

# Dog().display_health().walk().walk().walk().run().run().pet().display_health()

class Dragon(Animal):
    def __init__(self):
        super().__init__("dragon", 170)
    def fly(self):
        self.health -= 10
        return self
    def display_health(self):
        print("Health:", self.health)
        print("I am a Dragon")
        return self

# Dragon().fly().display_health()

animal2 = Animal("Bird", 50)
animal2.walk().display_health()

# Dog().fly()