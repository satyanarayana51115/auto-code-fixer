def calculate_average(numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)


if __name__ == "__main__":
    # Correct case
    numbers_list = [10, 20, 30, 40, 50]
    avg = calculate_average(numbers_list)
    print(f"The average is: {avg}")

    # Case triggering the bug
    empty_list = []
    print("Attempting to calculate average of an empty list...")
    avg_empty = calculate_average(empty_list)
    print(f"The average is: {avg_empty}")