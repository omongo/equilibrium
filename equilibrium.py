def solution(A):
    left_sum = 0
    right_sum = sum(A)
    for i in range(1, len(A) - 1):
        left_sum += A[i - 1]
        if left_sum == right_sum - A[i] - left_sum:
            return i
    return -1

A = [-7, 1, 5, 2, -4, 3, 0]
print(solution(A))
