num_test_cases = int(input())

for _ in range(num_test_cases):
    length_of_array = int(input())
    input_array = list(map(int, input().split()))

    total_sum = 0
    current_index = 0

    while current_index < length_of_array:
        current_subsequence = []

        if input_array[current_index] < 0:
            while current_index < length_of_array and input_array[current_index] < 0:
                current_subsequence.append(input_array[current_index])
                current_index += 1
        else:
            while current_index < length_of_array and input_array[current_index] > 0:
                current_subsequence.append(input_array[current_index])
                current_index += 1

        if current_subsequence:
            total_sum += max(current_subsequence)

    print(total_sum)