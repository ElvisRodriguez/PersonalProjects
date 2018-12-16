import sys
import random

with open(sys.argv[0], "a") as file:
    file.write("\nwith open(sys.argv[0], 'a') as file:")
    file.write("\n\tfile.write('\\nprint(random.randint(1,1000))')")
    file.close()
