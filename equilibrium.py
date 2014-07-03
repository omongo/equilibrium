def solution(A):
    left_sum = 0
    right_sum = sum(A)
    for i in range(len(A)):
        right_sum -= A[i]
        if left_sum == right_sum:
            return i
        left_sum += A[i]
    return -1

A = [-7, 1, 5, 2, -4, 3, 0]
print(solution(A))
