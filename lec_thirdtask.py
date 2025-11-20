class Puppy:
    states = {0: 'Болеет', 1: 'Выздоравливает', 2: 'Здоров'}

    def __init__(self, index):
        self.index = index
        self.state_key = 0
        self.state = Puppy.states[self.state_key]

    def get_treatment(self):
        self.state_key = self.state_key + 1
        if self.state_key > 2:
            self.state_key = 2

        self.state = Puppy.states[self.state_key]

    def is_healthy(self):
        return self.state_key == 2


class Dog:
    def __init__(self, puppies_count):
        self.puppies_count = puppies_count
        self.puppies = []
        for i in range(self.puppies_count):
            self.puppies.append(Puppy(i))

    def heal_all(self):
        for Ф in self.puppies:
            puppy.get_treatment()

    def all_are_healthy(self):
        for puppy in self.puppies:
            if not puppy.is_healthy():
                return False
        return True

    def give_away_all(self):
        self.puppies.clear()


class Vet:
    def __init__(self, name, plant):
        self.name = name
        self.plant = plant

    def work(self):
        self.plant.heal_all()

    def care(self):
        if self.plant.all_are_healthy():
            self.plant.give_away_all()
        else:
            print("Не все щенки здоровы")

    def knowledge_base(self):
        for puppy in self.plant.puppies:
            print(f'Щенок № {puppy.index} {puppy.state}')


dog = Dog(5)
vet = Vet("Вася", dog)
vet.knowledge_base()
vet.work()
vet.knowledge_base()
vet.work()
vet.knowledge_base()