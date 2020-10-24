class Zoo:
	__animals = 0

	def __init__(self, name):
		self.name = name
		self.mammal = []
		self.fish = []
		self.bird = []

	def add_animal(self, species, name):
		if species == 'mammal':
			self.mammal.append(name)
		elif species == 'fish':
			self.fish.append(name)
		elif species == 'bird':
			self.bird.append(name)
		self.__animals += 1

	def get_info(self, species):
		species_name = []
		test_name = ''
		zoo_name = self.name
		if species == 'mammal':
			test_name = 'Mammals'
			species_name = self.mammal
		elif species == 'fish':
			test_name = 'Fishes'
			species_name = self.fish
		elif species == 'bird':
			test_name = 'Birds'
			species_name = self.bird
		names = ', '.join(species_name)
		return f'{test_name} in {zoo_name}: {names}'

	def get_total(self):
		return f'Total animals: {self.__animals}'

zoo_name = input()
zoo = Zoo(zoo_name)

n = int(input())
for _ in range(n):
	species, name = input().split()
	zoo.add_animal(species, name)

species = input()

print(zoo.get_info(species))
print(zoo.get_total())