import json
from functools import reduce

path = "C:\\Users\\Bruno Cardoso\\Instituto Gerando Falcões\\Repositório Bruno Cardoso - Documentos\\2022\\Python\\projects_python\\9_aquarium\\"

f = open(path + "aquarium.json", encoding="utf8")

data_aquarium = json.load(f)
animals = data_aquarium['data']

def pick_animal_type(animal):
    return animal['type'], 1


def reducer(acc, val):
    if val[0] not in acc.keys():
        acc[val[0]] = 0 + val[1]
    else:
        acc[val[0]] = acc[val[0]] + val[1]
    return acc


type_animals = list(map(pick_animal_type, animals))

print(type_animals)

animal_type_count = reduce(reducer, type_animals, {})
print(animal_type_count)