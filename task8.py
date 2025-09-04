ricxevebi = input("შეიყვანე რიცხვები : ")
ricxvebi = [int(x) for x in ricxevebi.split()]


pyramid = [ricxvebi]

while len(pyramid[-1]) > 1:
    prev_row = pyramid[-1]
    new_row = []
    for i in range(len(prev_row) - 1):
        new_row.append(prev_row[i] + prev_row[i+1])
    pyramid.append(new_row)

for row in pyramid:
    print(" ".join(str(x) for x in row))
