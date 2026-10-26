def find_max_sum_window(arr, m):
    if not arr or m <= 0 or m> len(arr):
      current_sum = sum(arr[:m])
      max_sum = current_sum
      for i in range(m, len(arr)):
      current_sum += arr[i] - arr[i - m]
        if current_sum> max_sum:
          max_sum = current_sum
  return max_sum
my_array = [1.5, 2.0, -1.0, 3.0, 4.5,0.5]
m = 3
result = find_max_sum_window(my_array, m)
print(f"Максимальная сумма отрезка из {m} чисел: {result}")
