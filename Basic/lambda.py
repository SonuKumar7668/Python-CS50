people = [
    {"name": "harry","house":"gryffindor"},
    {"name": "cho","house":"ravenclow"},
    {"name": "draco","house":"slytherin"},
]
def f(person):
    return person["house"]

people.sort(key=f)
print(people)