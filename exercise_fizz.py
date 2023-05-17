def fizzbuzz(number: int):
    if number % 3 == 0 and number % 5 == 0:
        return "FizzBuzz"
    elif number % 3 == 0:
        return "Fizz"
    elif number % 5 == 0:
        return "Buzz"
    return str(number)


# x = int(input("Please enter number: "))
# a = fizzbuzz(x)
# print(a)
