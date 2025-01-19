# List of dictionaries representing different pets
pets = [
    {"animal": "dog", "name": "Ruso", "owner": "Qanabawi"},
    {"animal": "cat", "name": "Coco", "owner": "Himothy"},
    {"animal": "parrot", "name": "Roro", "owner": "Bartholomew"},
    {"animal": "rabbit", "name": "Beto", "owner": "Kashmiri"},
    {"animal": "hamster", "name": "Loko", "owner": "Ismail"}
]

# Loop through the list and print details about each pet
for pet in pets:
    print(f"\nPet Details:")
    print(f"Animal: {pet['animal'].title()}")
    print(f"Name: {pet['name']}")
    print(f"Owner: {pet['owner']}")