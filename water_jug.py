def water_jug_problem():
    jug1_capacity = 4
    jug2_capacity = 3
    target = 2
    jug1 = 0
    jug2 = 0
    path = []

    while jug1 != target and jug2 != target:
        if jug1 == 0:
            jug1 = jug1_capacity
            path.append((jug1, jug2))
        elif jug2 == jug2_capacity:
            jug2 = 0
            path.append((jug1, jug2))
        elif jug1 > 0 and jug2 < jug2_capacity:
            pour_amount = min(jug1, jug2_capacity - jug2)
            jug1 -= pour_amount
            jug2 += pour_amount
            path.append((jug1, jug2))
        elif jug2 > 0:
            jug2 = 0
            path.append((jug1, jug2))

    return path

solution = water_jug_problem()
for state in solution:
    print(state)