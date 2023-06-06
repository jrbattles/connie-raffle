import random
import time

# Open the text file containing the list of people
with open('people.txt', 'r') as file:
    people_list = file.read().splitlines()

print()
print("ACTIVATING CONNIE ", end='', flush=True)
for _ in range(3):
    print("*", end='', flush=True)
    time.sleep(1)  # Add a delay of 1 second for suspense
print()
print()


# Print "thinking..." to create suspense
print("Hi, I am Connie the Containerized Tech Crusader.")

print("I am scrambling the list of attendees now.", end='', flush=True)
for _ in range(3):
    print(".", end='', flush=True)
    time.sleep(1)  # Add a delay of 1 second for suspense

# time.sleep(2)  # Add a delay of 3 seconds for suspense
print("ok")

# time.sleep(3)  # Add a delay of 3 seconds for suspense
print("And I am randomizing again based on quantum conditions.", end='', flush=True)
for _ in range(3):
    print(".", end='', flush=True)
    time.sleep(1)  # Add a delay of 1 second for suspense

print("ok")
# time.sleep(3)  # Add a delay of 3 seconds for suspense
# print("The winner of the Tech Crusaders Raffle is...")
# time.sleep(3)  # Add a delay of 3 seconds for suspense

# Print "thinking..." to create suspense
print("Thinking.", end='', flush=True)
time.sleep(1)  # Add a delay of 1 second for suspense

for _ in range(3):
    print(".", end='', flush=True)
    time.sleep(1)  # Add a delay of 1 second for suspense

print("ok")

print("The randomly selected person is.", end='', flush=True)
time.sleep(1)  # Add a delay of 1 second for suspense

for _ in range(3):
    print(".", end='', flush=True)
    time.sleep(1)  # Add a delay of 1 second for suspense
# Randomly select a person from the list

random_person = random.choice(people_list)

# Print the randomly selected person
print(f"{random_person}")
