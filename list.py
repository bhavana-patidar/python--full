# list 
# 1 . list are ordered collection of data items.
# 2 . they are multiple items in a single variable
# 3. list items are separated by commas and enclosed within square brackets[].
# 4. list are changeable meaning we can alter them after creation.
# list mutable hoti hai.


# 1. List mein kai values ek saath rakhte hain, square brackets [ ] mein, comma se alag karke.
# 2. Index bilkul string jaisa: ginti 0 se shuru, fruits[0] = "apple".
# 3. Negative index bhi chalta hai: fruits[-1] = "banana".
# 4 .Slicing bhi chalti hai: fruits[0:2] = ["apple", "mango"].
# 5. len(fruits) = 3.
# 6 . Loop se items nikal sakte ho: for i in fruits: print(i).
# 7. String ke ulat, list ko badal sakte hain: fruits[1] = "kiwi".


marks = [3, 5, 6 , "Harry" , True]
# print(marks)
print(type(marks))
print(marks[0])
print(marks[1])
print(marks[2])

print(marks[-3])
print(marks[len(marks)-3])
print(marks[5-3])
print(marks[2])


if "Harry" in marks:
    print("yes")
else:
    print("No")


#same thing applies for strings as well!
if "Ha" in "Harry":
  print("Yes")

print(marks)
print(marks[1:])
print(marks[1:-1])  # -1 = [len(marks)-1]

# jump index
print(marks[1:4:2])



# List comprehension = list comprehesion are used for creating new list from other iterables like list , tuples , dictionary , sets , and even in array and string.

lst = [i*i for i in range(10)]
print(lst)
lst = [i*i for i in range(10) if i%2==0]
print(lst)


# practice

# 1.
marks = [45, 60, 72, 88, 91]
print(marks)

# 2.
marks = [45, 60, 72, 88, 91]
print(marks[0])
print(marks[4])

# 3.
marks = [45, 60, 72, 88, 91]
print(len(marks))


# 4.
marks = [45, 60, 72, 88, 91]
print(marks[1:4])


# 5.
marks = [45, 60, 72, 88, 91]
for i in marks:
        print(i)


# 6.
marks = [45, 60, 72, 88, 91]
marks[2] = 80
print(marks)



# 7. 
marks = [45, 60, 72, 88, 91]
print(marks[-2])
print(marks[:4])


    