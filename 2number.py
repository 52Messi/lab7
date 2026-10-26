def max_segment_sum(arr, m):
    current_sum = sum(arr[:m])
    max_sum = current_sum
    for i in range(m, len(arr)):
        current_sum += arr[i] - arr[i-m]
        if current_sum> max_sum:
            max_sum = current_sum
    return max_sum
arr = [1.5, 2.0,-1.0, 3.0, 4.5,0.5]
m = 3
print(max_segment_sum(arr, m))
