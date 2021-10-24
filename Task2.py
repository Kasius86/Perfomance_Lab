def position_point_relative_circle(file_1, file_2):
    
    file1 = open(file_1)
    file2 = open(file_2)
    for row in file1:
        if ' ' in row:
            centr_circ = row.split()
        else:
            r = int(row)

    for j in file2:
        x = j.split()
        position_point = (float(x[0]) - float(centr_circ[0])) ** 2 + (float(x[1]) - float(centr_circ[1])) ** 2
        if position_point == r ** 2:
            print(0)
        elif position_point < r ** 2:
            print(1)
        else:
            print(2)

position_point_relative_circle(input(), input())
