# ==============================================
# Python Iterators — Educational Examples
# Source: W3Schools + Educational Enhancements
# Author: Rezvan Panah
# ==============================================

# Example 1: Simple iterator using iter() and next()
# --------------------------------------------------
# The iter() function returns an iterator object.
# The next() function retrieves items one by one.
# def example1():
#     fruits = ["apple", "banana", "cherry"]
#     my_iterator = iter(fruits)
#     print(next(my_iterator))  # apple
#     print(next(my_iterator))  # banana
#     print(next(my_iterator))  # cherry
# example1()

# Example 2: Iterator in a for loop
# ---------------------------------
# for loops automatically use iterators internally.
# def example2():
#     fruits = ("apple", "banana", "cherry")
#     for fruit in fruits:
#         print(fruit)
# example2()
# Output: apple, banana, cherry


# Example 3: Create a custom iterator class
# -----------------------------------------
# To create an iterator, a class must implement __iter__() and __next__().
class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= 5:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration


def example3():
    myclass = MyNumbers()
    myiter = iter(myclass)
    for x in myiter:
        print(x)
example3()  
# Output: 1 2 3 4 5


# Example 4: Iterator that stops manually
# ---------------------------------------
# Using StopIteration allows control over iteration limits.
# def example4():
#     class CountDown:
#         def __init__(self, start):
#             self.current = start

#         def __iter__(self):
#             return self

#         def __next__(self):
#             if self.current <= 0:
#                 raise StopIteration
#             else:
#                 num = self.current
#                 self.current -= 1
#                 return num

#     for num in CountDown(5):
#         print(num)
# Output: 5 4 3 2 1


# Example 5: Using iterator with strings
# --------------------------------------
# def example5():
#     text = "AI"
#     text_iter = iter(text)
#     print(next(text_iter))  # A
#     print(next(text_iter))  # I
    
# example5()
