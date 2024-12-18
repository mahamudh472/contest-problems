for _ in range(int(input())):
    m, a, b, c = map(int, input().split())
    a_can_occupy = a if a<m else m
    b_can_occupy = b if b<m else m
    seats_left = m*2-(a_can_occupy+b_can_occupy)
    c_can_occupy = c if c<seats_left else seats_left
    print(a_can_occupy+b_can_occupy+c_can_occupy)