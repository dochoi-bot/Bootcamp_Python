import sys 

index = len(sys.argv) - 1
if len(sys.argv) != 2:
    print("ERROR")
else:
    try:
        if (int)(sys.argv[1]) == 0:
            print("I'm Zero.")
        elif (int)(sys.argv[1]) % 2 == 0:
            print("I'm Even.")
        else:
            print("I'm Odd.")
    except:
        print("ERROR")
