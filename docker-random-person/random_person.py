import random

# Open the text file containing the list of people
with open('people.txt', 'r') as file:
    people_list = file.read().splitlines()

# Randomly select a person from the list
random_person = random.choice(people_list)

# Print the randomly selected person
print(f"The randomly selected person is: {random_person}")
