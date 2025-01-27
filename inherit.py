# method overriding

# class Animal:
#     def __init__(self,name):
#         self.name=name
#     def speak(self):
#         print(f'{self.name} makes a sound.')

# class Dog(Animal):
#     def speak(self):
#         print(f'{self.name} barks.')

# animal=Animal('Generic Animal')
# animal.speak()

# dog=Dog('Buddy')
# dog.speak()
# -----------------------------------------------------------------------------------
# constructor overloading(same name)

# class Animal:
#     def __init__(self,name):
#         self.name=name
#     def speak(self):
#         print(f'{self.name} makes a sound.')

# class Dog(Animal):
#     def __init__(self):
#         self.behaviour='friendly'
#     def speak(self):
#         print(f'{self.name} barks. He is very {self.behaviour}')

# animal=Animal('Generic Animal')
# animal.speak()

# dog=Dog()
# dog.speak()


# ---------------------------------------------------------------------------

class Animal:
    def __init__(self):
        self.name='Buddy'
    def speak(self):
        print(f'{self.name} makes a sound.')

class Dog(Animal):
    def __init__(self,breed):
        super().__init__()# cancel the base class init() constructor
        self.breed=breed
    def speak(self):
        super().speak()# call the base class
        print(f'{self.name} barks. It is a {self.breed}')


dog=Dog('Golden Retriever')
dog.speak()