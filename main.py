import random
import time


def execute(data):
    if len(data) // 2 == 0:
        return data

    data_a, data_b = divide(data)

    data_a = execute(data_a)
    data_b = execute(data_b)

    return merge(data_a, data_b)


def divide(data):
    split_point = len(data) // 2
    data_a = data[:split_point]
    data_b = data[split_point:]

    return data_a, data_b


def merge(data_a, data_b):
    result = []
    a_index, b_index = 0, 0

    while a_index < len(data_a) and b_index < len(data_b):
        if data_a[a_index] < data_b[b_index]:
            result.append(data_a[a_index])
            a_index += 1
        else:
            result.append(data_b[b_index])
            b_index += 1

    # Append any remaining elements
    result.extend(data_a[a_index:])
    result.extend(data_b[b_index:])

    return result


# Prompt the user for the length of the list
def generate_list():
    try:
        list_length = int(input("Enter the length of the list: "))
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
        exit(1)

# Generate a list of random integers
    random_list = [random.randint(1, 100) for _ in range(list_length)]

# Display the generated list
    print(f"Generated list of length {list_length}:")
    print(random_list)
    return random_list


def main():
    data = generate_list()
    start_time = time.time()
    sorted_data = execute(data)
    end_time = time.time()
    execution_time = end_time - start_time

    print(sorted_data)

    print(f"Execution time: {execution_time:.6f} seconds")

    return len(sorted_data), execution_time


if __name__ == '__main__':
    main()