import sys
try:
    data = sys.stdin.read()
    print(data)
    print("Executed!")
    for line in sys.stdin:
        print(line.rstrip())
except EOFError:
    print(sys.exc_info())