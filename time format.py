inp = input()
result = str(int(inp[:2]) + 12) + inp[2:-2]
print(inp[:-2]) if inp[-2:] == "AM" else print(result)