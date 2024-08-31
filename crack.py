from string import ascii_letters, digits, punctuation
from itertools import product
import time

start_time = time.time()

for passcode in product(ascii_letters + digits + punctuation, repeat=4):
    print(passcode)

print("[ %s seconds ]" % (time.time() - start_time))
