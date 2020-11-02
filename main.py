import numpy as np
from math import gcd

# base 행과 target 행에서 해당 인덱스 값의 최소 공배수로 만들어 해당 target의 인덱스를 0으로 만들음
def operation__(matrix, base, target, idx):
    if matrix[target][idx]==0 :
        return 0
    gcd_v = gcd(int(matrix[base][idx]), int(matrix[target][idx]))
    if gcd_v == 0:
        return 0
    matrix[target] = matrix[target] * (int(matrix[base][idx]/gcd_v)) - matrix[base] * (
               int(matrix[target][idx])/gcd_v)

# fromIdx 밑으로 compareidx를 기준으로 역순으로 정렬
def sort_by_idx(matrix, fromidx, compareidx):
    tmp = matrix[fromidx:]
    matrix[fromidx:] = tmp[tmp[:, compareidx].argsort()[::-1]]

# 행의 컴포넌트들의 최대 공약수를 구함
def array_gcd (arr):
    res = arr[0]
    for c in arr:
        res = gcd(res,c)
    return res

if __name__ == "__main__":
    row = int(input("행을 입력해주세요: "))
    col = int(input("열을 입력해주세요: "))
    entries = list(map(int, input("component를 일렬로 space로 구별하여 입력해주세요(정수만): ").split()))

    matrix = np.array(entries).reshape(row, col)
    print(matrix)
    start = 0

    # 역순으로 정렬하였을때 첫번째 값이 0일 경우 해당 col은 모두 0이므로 다시 다음 col을 기준으로 정렬
    while(1):
        sort_by_idx(matrix, 0, start)
        if matrix[0][0] == 0:
            start += 1
            if start == col:
                break
        else:
            break
    # 어디까지 0을 만들어야 upper triangle form으로 변하는지 (row와 col중 더 작은 수 -1)
    ctr = min(row, col)
    ctr -= 1

    # to upper triangular form
    for j in range(start, ctr):
        base = row - ctr + j-1
        sort_by_idx(matrix,base+1,j)
        for i in range(base+1, row):
            print (matrix)
            operation__(matrix, base, i, j)


    # 행렬의 각 행마다 각 행의 컴포넌트의 gcd로 나눠지는 체크하고 나줘서 깔끔한 형태로 변환
    for i in range(0,row):
        div = array_gcd(matrix[i])
        if div == 0 or div == 1:
            continue
        else:
            matrix[i] = matrix[i]/div

    print("result:")
    print(matrix)