
# ==================================================
# 1. Fizz Buzz (1 to 50)
# ==================================================
def fizz_buzz():
    for i in range(1, 51):
        if i % 15 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

print("----- Fizz Buzz -----")
fizz_buzz()


# ==================================================
# 2. Factorial of a Number
# ==================================================
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

print("\n----- Factorial -----")
print(factorial(5))
print(factorial(7))


# ==================================================
# 3. Prime Number Check
# ==================================================
def is_prime(n):
    if n <= 1:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True

print("\n----- Prime Number Check -----")
print(is_prime(11))
print(is_prime(15))


# ==================================================
# 4. Reverse a String (Without Built-in Reverse)
# ==================================================
def reverse_string(text):
    reversed_text = ""

    for char in text:
        reversed_text = char + reversed_text

    return reversed_text

print("\n----- Reverse String -----")
print(reverse_string("Python"))
print(reverse_string("Data"))


# ==================================================
# 5. Palindrome Check
# ==================================================
def palindrome_check(text):
    reversed_text = reverse_string(text)

    if text == reversed_text:
        return True

    return False

print("\n----- Palindrome Check -----")
print(palindrome_check("madam"))
print(palindrome_check("hello"))


# ==================================================
# 6. Word Count of a Sentence
# ==================================================
def word_count(sentence):
    words = sentence.split()
    return len(words)

print("\n----- Word Count -----")
print(word_count("Python is easy"))
print(word_count("Data Analyst Training Program"))


# ==================================================
# 7. Character Frequency of a Word
# ==================================================
def character_frequency(word):
    freq = {}

    for char in word:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1

    return freq

print("\n----- Character Frequency -----")
print(character_frequency("banana"))
print(character_frequency("python"))


# ==================================================
# 8. Remove Duplicates from a List (Keep Order)
# ==================================================
def remove_duplicates(lst):
    result = []

    for item in lst:
        if item not in result:
            result.append(item)

    return result

print("\n----- Remove Duplicates -----")
print(remove_duplicates([1, 2, 2, 3, 4, 4, 5]))
print(remove_duplicates([10, 10, 20, 30, 20]))


# ==================================================
# 9. Find Max and Min in a List (Without max/min)
# ==================================================
def find_max_min(lst):
    maximum = lst[0]
    minimum = lst[0]

    for num in lst:
        if num > maximum:
            maximum = num

        if num < minimum:
            minimum = num

    return maximum, minimum

print("\n----- Max and Min -----")
print(find_max_min([4, 8, 2, 9, 1]))
print(find_max_min([50, 20, 90, 10]))


# ==================================================
# 10. Sum of Even Numbers from 1 to N
# ==================================================
def sum_even_numbers(n):
    total = 0

    for i in range(1, n + 1):
        if i % 2 == 0:
            total += i

    return total

print("\n----- Sum of Even Numbers -----")
print(sum_even_numbers(10))
print(sum_even_numbers(20))


# ==================================================
# 11. Build Dictionary from Two Lists
# ==================================================
def build_dictionary(keys, values):
    result = {}

    for i in range(len(keys)):
        result[keys[i]] = values[i]

    return result

print("\n----- Dictionary from Lists -----")
print(build_dictionary(["a", "b", "c"], [1, 2, 3]))
print(build_dictionary(["name", "age"], ["Manju", 25]))


# ==================================================
# 12. Count Vowels in a String
# ==================================================
def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0

    for char in text:
        if char in vowels:
            count += 1

    return count

print("\n----- Count Vowels -----")
print(count_vowels("education"))
print(count_vowels("python programming"))


# ==================================================
# 13. Celsius ↔ Fahrenheit Converter
# ==================================================
def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

print("\n----- Temperature Converter -----")
print(celsius_to_fahrenheit(25))
print(celsius_to_fahrenheit(40))

print(fahrenheit_to_celsius(98.6))
print(fahrenheit_to_celsius(212))


# ==================================================
# 14. Grade Calculator
# ==================================================
def calculate_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

print("\n----- Grade Calculator -----")
print(calculate_grade(95))
print(calculate_grade(72))


# ==================================================
# 15. Simple Calculator
# ==================================================
def simple_calculator(num1, num2, operator):

    if operator == "+":
        return num1 + num2

    elif operator == "-":
        return num1 - num2

    elif operator == "*":
        return num1 * num2

    elif operator == "/":
        if num2 == 0:
            return "Error: Division by zero"
        return num1 / num2

    else:
        return "Invalid Operator"

print("\n----- Simple Calculator -----")
print(simple_calculator(10, 5, "+"))
print(simple_calculator(20, 4, "/"))
print(simple_calculator(10, 0, "/"))