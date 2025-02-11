def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list
    total = sum(numbers)
    average = total / len(numbers)
    return average

my_list = [10, 20, 30, 40, 50]
average = calculate_average(my_list)
print(f"The average is: {average}")

my_empty_list = []
average = calculate_average(my_empty_list) #this will return 0 because it handles an empty list
print(f"The average is: {average}")

my_list = [10,20,30,40,50, 'a']
average = calculate_average(my_list) #this will give an error because of type mismatch