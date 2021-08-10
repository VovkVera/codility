def solution(A, K):
    old = A
    new = [0] * len(A)
    for i in range(K):
        new[0] = old[-1]
        new[1:] = old[:-1]
        old = new.copy()
        
    return new


if __name__ == '__main__':
    A = [3, 8, 9, 7, 6]
    K = 3
    print(solution(A, K))
