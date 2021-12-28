def sum_two_smallest_numbers(numbers):
    return sum(sorted(numbers)[:2])


print(sum_two_smallest_numbers([3,6,8,9,11,55,234, 7, 1]))