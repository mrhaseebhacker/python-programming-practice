import random
num = random.randint(1,10)
print(num)

import time
def manual_random():
    current_time = int(time.time()* 1000)
    random_num = current_time % 10
    return random_num
print("Random number is :",manual_random())