import time 
import os

delay = int(input("Enter delay time: "))
repeat_times = int(input("How many repeats: "))

pattern = ["o", " o", "  o", "   o", "    o", "     o", "      o", "     o", "    o", "   o", "  o", " o", "o"]
for x in range(repeat_times):
    for line in pattern:
        print(line)
        os.system('cls')
        time.sleep(delay)
        
