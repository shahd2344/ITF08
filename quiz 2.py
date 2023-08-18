

def find_min_max(numbers):
    numbers.sort()
    smallest = numbers[0]
    largest = numbers[-1]
    return smallest, largest


num_list = [5, 6, 55, 24, 5, 67]
min_num, max_num = find_min_max(num_list)
print("Smallest:", min_num)
print("Largest:", max_num)