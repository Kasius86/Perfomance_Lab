a = []

def minimum_number_moves(file):
    data_file = open(file)
    for i in data_file:
        a.append(int(i))
    mdn = sorted(a)[len(a) // 2]
    sum_steps = 0
    for item in a:
        sum_steps += abs(item-mdn)
    print(sum_steps)



minimum_number_moves(input())
