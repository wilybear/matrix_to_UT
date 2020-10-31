import numpy as np
from math import gcd

#fraction사용해보자
def operation__(matrix, base, target, idx):
    gcd_v = gcd(float(matrix[base][idx]), float(matrix[target][idx]))
    if gcd_v == 0:
        return 0
    matrix[target] = matrix[target] * (float(matrix[base][idx]/gcd_v)) - matrix[base] * (
               float(matrix[target][idx])/gcd_v)
    print("------------------")
    print(matrix)


if __name__ == "__main__":
    row = int(input("행을 입력해주세요: "))
    col = int(input("열을 입력해주세요: "))
    entries = list(map(float, input("component를 space로 구별하여 입력해주세요: ").split()))

    matrix = np.array(entries).reshape(row, col)
    print(matrix)

    ctr = row
    if col < row:
        ctr = col
    ctr -= 1

    for j in range(0, ctr):
        for i in range(row - ctr + j, row):
            operation__(matrix, row - ctr + j-1, i, j)
    print(matrix)
