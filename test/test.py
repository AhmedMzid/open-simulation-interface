
import sys

state = 0

with open("osi_environment.proto", "rt") as fin:
    i = 0
    for line in fin:
        i = i + 1
        if line.find("\t") != -1:
            state = 1
            print(str(i) + ": tab insted of spaces found")




sys.exit(state)
