import json

path = "C:\\Users\\Bruno Cardoso\\Instituto Gerando Falcões\\Repositório Bruno Cardoso - Documentos\\2022\\Python\\projects_python\\9_aquarium\\"

f = open(path + "aquarium.json", encoding="utf8")

# Load quando estamos trabalhando com um arquivo JSON
# Loads quando estamos trabalhando com uma variável JSON no código
data_aquarium = json.load(f)
animals = data_aquarium['data']

######## FILTER ######

# 1º Forma de filtrar
def verify_fish(animal):
    if animal["type"] == "fish":
        return True
    return False

######## FILTER LAMBDA ######
# 2º Forma de filtrar
animals_fish = list(filter(lambda animal: (animal["type"] == "fish"), animals))

# Preview das def acima
animals_fish = list(filter(verify_fish, animals))
#print(animals_fish)

######## MAP ######

# Captar uma única informação
def animal_name(animal):
    return animal['name']

animals_fish_name = list(map(animal_name, animals_fish))
#print(animals_fish_name)

def assign_to_tank(animals, names_selected, new_tank_number):
    def cange_tank_number(animal):
        if animal["name"] in names_selected:
            animal["tank_number"] = new_tank_number
        return animal
    return list(map(cange_tank_number, animals))

new_aquarium = assign_to_tank(animals, animals_fish_name, 42)
print(new_aquarium)