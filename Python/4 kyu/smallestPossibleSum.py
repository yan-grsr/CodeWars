# https://www.codewars.com/kata/52f677797c461daaf7000740/train/python

def solution(X):
    loop = 1
    while loop:
        if X.count(X[0]) == len(X):
            break
        for j in range(len(X)):
            for i in range(len(X)):
                if X[i] > X[j]:
                    X[i] = X[i] - X[j]
    return sum(X)

if __name__ == '__main__':
    print(solution([6, 9, 21]))