import sys 

index = len(sys.argv) - 1
while index > 0:
    print(sys.argv[index][::-1], end='')
    if (index != 1):
        print(end=' ')
    index -= 1
