# 🌀 Python Iterators — Educational Examples

This repository explains **Iterators** in Python based on **W3Schools** with clear comments and examples for students.

---

## 🧠 What is an Iterator?

An **iterator** is an object that contains a countable number of values.  
It can be iterated upon, meaning you can traverse through all the values.

In Python, an iterator must implement two methods:

```python
__iter__()  # Returns the iterator object itself
__next__()  # Returns the next value from the sequence
```

---

## 🧩 Examples and Explanations

### 🔹 Example 1 — Basic Iterator
```python
fruits = ["apple", "banana", "cherry"]
my_iterator = iter(fruits)
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))
```
**Explanation:**  
`iter()` returns an iterator object, and `next()` retrieves items one by one.

---

### 🔹 Example 2 — Iterator in a For Loop
```python
fruits = ("apple", "banana", "cherry")
for fruit in fruits:
    print(fruit)
```
**Explanation:**  
All loops in Python use iterators behind the scenes.

---

### 🔹 Example 3 — Custom Iterator Class
```python
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

myclass = MyNumbers()
myiter = iter(myclass)
for x in myiter:
    print(x)
```
**Explanation:**  
Defines a class that generates numbers 1 to 5 using custom iterator methods.

---

### 🔹 Example 4 — StopIteration Example
```python
class CountDown:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= 0:
            raise StopIteration
        else:
            num = self.current
            self.current -= 1
            return num

for num in CountDown(5):
    print(num)
```
**Explanation:**  
Stops iteration manually when reaching 0 using `StopIteration`.

---

### 🔹 Example 5 — String Iterator
```python
text = "AI"
text_iter = iter(text)
print(next(text_iter))
print(next(text_iter))
```
**Explanation:**  
Strings are iterable too — each character can be accessed using `next()`.

---
## 📎 Author
👩‍💻 **Created by:** Rezvan Panah  
📅 **Year:** 2025  
💬 **Language:** Python 3.10  
🎯 **Purpose:** Teaching Python functions in a clear and beginner-friendly way.

---

## 💖 Support & Feedback
If this repository helped you, please consider:
- ⭐ **Starring** the repo  
- 🗨️ **Commenting** your thoughts  
- 📢 **Sharing** it with others learning Python  

Your feedback motivates more free educational content!

---

## 🧑‍💻 Author
**Rezvan Panah** — Educational version for teaching Python Iterators.
