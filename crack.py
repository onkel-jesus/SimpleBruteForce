from string import ascii_letters, digits
from itertools import product

for passcode in product(ascii_letters + digits, repeat=4):
    print(passcode)
