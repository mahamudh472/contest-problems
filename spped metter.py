for _ in range(int(input())):
    w, x, y, z = map(int, input().split())
    alice_speed = w / x
    bob_speed = y / z
    if alice_speed > bob_speed:
        print("Alice")
    elif alice_speed == bob_speed:
        print("Equal")
    else:
        print("Bob")