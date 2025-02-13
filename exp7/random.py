import random
import string

hex_color = "#{:06x}".format(random.randint(0, 0xFFFFFF))
alphabetical_string = ''.join(random.choice(string.ascii_letters) for _ in range(10))
random_value = random.randint(10, 50)
random_multiple_of_7 = random.randint(0, 10) * 7

print("Random Hex Color:", hex_color)
print("Random Alphabetical String:", alphabetical_string)
print("Random Value:", random_value)
print("Random Multiple of 7:", random_multiple_of_7)
