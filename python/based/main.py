                    #  start

# print("hellp world")



# if 5 > 2:
#     print("five is greater then two")


# x = 5
# y = "John"
# print(x)
# print(y)


# A -- B -- C
# |    |    |
# D -- E -- F



# a = int(input())
# b = int(input())
# for i in range(a,b+1):
#     print(i)


# my_list=[1,2,3,4,5,6,7,8,9]
# print(max(my_list))
# print(min(my_list))

# a = int(input("Enter the value of a: "))
# b = int(input("Enter the value of b: "))

# if a < b:
#     print("a is less than b")
# elif a > b:
#     print("a is greater than b")
# else:
#     print("a is equal to b")

# x = 5
# x += 3
# print(x)


# i = 1
# while i < 6:
#   print(i)
#   i += 1

# # Исходный список с числами
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# # Используем списковое включение для создания нового списка, исключая нечетные числа
# filtered_numbers = [num for num in numbers if num % 2 == 0]

# # Вывод результата
# print(filtered_numbers)



# my_list = [12, 3, 6, 77, 99, 36]
# my_list.reverse()

# print(my_list)


# def factorial_iterative(n):
#     result = 1
#     for i in range(1, n + 1):
#         result *= i
#     return result

# # Пример использования:
# number = 6
# result = factorial_iterative(number)
# print(f"Факториал числа {number} равен {result}")


 # Assuming a starting value for 'i'

# while i <= 50:
#     if i % i == 0 and i % 2 != 0:
#         print(i)
#     i += 1


# my_list = [1, 2, 3, 4, 5, 6]

# new_list = [x for x in my_list if x % 2 == 0]

# print(new_list)

def two_sum(nums, target):
    # Create a dictionary to store the indices of elements
    indices = {}

    for i, num in enumerate(nums):
        complement = target - num
        # Check if the complement exists in the dictionary
        if complement in indices:
            # Return the indices of the two numbers that add up to the target
            return [indices[complement], i]
        # Store the current element and its index in the dictionary
        indices[num] = i

    # If no solution is found, return an empty list or raise an exception
    return []

# Example usage:
nums = [2, 7, 11, 15]
target = 18
result = two_sum(nums, target)
print(result)  # Output: [0, 1]

