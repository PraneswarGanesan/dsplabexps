import random
import string

random_character = random.choice(string.ascii_letters)
random_string = ''.join(random.choice(string.ascii_letters) for _ in range(random.randint(5, 15)))
fixed_length_string = ''.join(random.choice(string.ascii_letters) for _ in range(10))

print("Random Alphabetical Character:", random_character)
print("Random Alphabetical String:", random_string)
print("Fixed Length Alphabetical String:", fixed_length_string)
