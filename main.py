# #                     #  start

# # # print("hellp world")



# # # if 5 > 2:
# # #     print("five is greater then two")


# # # x = 5
# # # y = "John"
# # # print(x)
# # # print(y)


# # # A -- B -- C
# # # |    |    |
# # # D -- E -- F



# # # a = int(input())
# # # b = int(input())
# # # for i in range(a,b+1):
# # #     print(i)


# # # my_list=[1,2,3,4,5,6,7,8,9]
# # # print(max(my_list))
# # # print(min(my_list))

# # # a = int(input("Enter the value of a: "))
# # # b = int(input("Enter the value of b: "))

# # # if a < b:
# # #     print("a is less than b")
# # # elif a > b:
# # #     print("a is greater than b")
# # # else:
# # #     print("a is equal to b")

# # # x = 5
# # # x += 3
# # # print(x)


# # # i = 1
# # # while i < 6:
# # #   print(i)
# # #   i += 1

# # # # Исходный список с числами
# # # numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# # # # Используем списковое включение для создания нового списка, исключая нечетные числа
# # # filtered_numbers = [num for num in numbers if num % 2 == 0]

# # # # Вывод результата
# # # print(filtered_numbers)



# # # my_list = [12, 3, 6, 77, 99, 36]
# # # my_list.reverse()

# # # print(my_list)


# # # def factorial_iterative(n):
# # #     result = 1
# # #     for i in range(1, n + 1):
# # #         result *= i
# # #     return result

# # # # Пример использования:
# # # number = 6
# # # result = factorial_iterative(number)
# # # print(f"Факториал числа {number} равен {result}")


# #  # Assuming a starting value for 'i'

# # # while i <= 50:
# # #     if i % i == 0 and i % 2 != 0:
# # #         print(i)
# # #     i += 1


# # # my_list = [1, 2, 3, 4, 5, 6]

# # # new_list = [x for x in my_list if x % 2 == 0]

# # # print(new_list)

# # # def two_sum(nums, target):
# # #     # Create a dictionary to store the indices of elements
# # #     indices = {}

# # #     for i, num in enumerate(nums):
# # #         complement = target - num
# # #         # Check if the complement exists in the dictionary
# # #         if complement in indices:
# # #             # Return the indices of the two numbers that add up to the target
# # #             return [indices[complement], i]
# # #         # Store the current element and its index in the dictionary
# # #         indices[num] = i

# # #     # If no solution is found, return an empty list or raise an exception
# # #     return []

# # # # Example usage:
# # # nums = [2, 7, 11, 15]
# # # # target = 18
# # # # result = two_sum(nums, target)
# # # # print(result)  # Output: [0, 1]


# # # class Solution:
# # #     def twoSum(self, nums, target):
# # #         indices = {}

# # #         for i, num in enumerate(nums):
# # #             complement = target - num
# # #             if complement in indices:
# # #                 return [indices[complement], i]
# # #             indices[num] = i

# # #         return []

# # # # Example usage:
# # # nums = [2, 7, 11, 15]
# # # target = 9

# # # # Create an instance of the Solution class
# # # solution_instance = Solution()

# # # # Call the twoSum method on the instance
# # # result = solution_instance.twoSum(nums, target)

# # # print(result)





# # class Solution:
# #     def romanToInt(self, s: str) -> int:
# #         lookup = {
# #             "I": 1,
# #             "V": 5,
# #             "X": 10,
# #             "L": 50,
# #             "C": 100,
# #             "D": 500,
# #             "M": 1000
# #         }

# #         N = len(s)
# #         i = N - 1
# #         output = 0
# #         while i >= 0:
# #             if i < N - 1 and lookup[s[i]] < lookup[s[i + 1]]:
# #                 output -= lookup[s[i]]
# #             else:
# #                 output += lookup[s[i]]
# #             i -= 1

# #         return output


# def longestCommonPrefix(strs):
#     if not strs:
#         return ""

#     # Find the minimum length string in the list
#     min_len = min(len(s) for s in strs)

#     # Iterate over the characters up to the minimum length
#     for i in range(min_len):
#         # Check if all characters at the current position are the same
#         if all(s[i] == strs[0][i] for s in strs):
#             continue
#         else:
#             # If characters are different, return the prefix up to this point
#             return strs[0][:i]

#     # If all characters match up to the minimum length, return the entire prefix
#     return strs[0][:min_len]

# # Example usage:
# strs1 = ["flower", "flow", "flight"]
# print(longestCommonPrefix(strs1))  # Output: "fl"

# strs2 = ["dog", "racecar", "car"]
# print(longestCommonPrefix(strs2))  # Output: ""

# def isValid(s):
#     stack = []
#     mapping = {')': '(', '}': '{', ']': '['}

#     for char in s:
#         if char in mapping:
#             top_element = stack.pop() if stack else '#'
#             if mapping[char] != top_element:
#                 return False
#         else:
#             stack.append(char)

#     return not stack

# # Example usage:
# print(isValid("()"))        # Output: True
# print(isValid("()[]{}"))    # Output: True
# print(isValid("(]"))         # Output: False
# print(isValid("([)]"))       # Output: False
# print(isValid("{[]}"))       # Output: True



# fruits = {"apple", "banana", "cherry"}
# more_fruits = ["orange", "mango", "grapes"]
# fruits.update(more_fruits)

# print(fruits)



# fruits = {"apple", "banana", "cherry"}
# fruits.append("append")


# fruits = {"apple", "banana", "cherry"}


x = 41

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")