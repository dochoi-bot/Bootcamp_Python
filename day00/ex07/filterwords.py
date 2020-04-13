
from string import punctuation
import sys

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("ERROR")
    else:
        if sys.argv[2].isdecimal() and not sys.argv[1].isdecimal():
            s = sys.argv[1].strip(punctuation).split()
            s2 = []
            for part in s:
                if len(part) > (int)(sys.argv[2]):
                    s2.append(part)
            print(s2)
        else:
            print("ERROR")