# string are immutable
a = "!!!Harry!!!!!!!!!!Harry"
print(len(a))
print(a)
print(a.upper())
print(a.lower())
print(a.rstrip("!"))
print(a.replace("Harry","john"))
print(a.split(" "))

blogHeading = "introduction to js"
print(blogHeading.capitalize())

str1 = "Welcome to the Console!!!"
print(len(str1))
print(len(str1.center(50)))
print(a.count("Harry"))

str1 = "Welcome to the Console!!!"
print(str1.endswith("to",4,10))

str1 = "Welcome to the Console!!!"
print(str1.endswith("!!!"))

str1 = "He's name is Dan. He is an honest man."
print(str1.find("is"))
print(str1.index("is"))

str1 = "WelcomeToTheConsole"
print(str1.isalnum())
str1 = "Welcome"
print(str1.isalpha())

str1 = "hello world"
print(str1.islower())

str1 = "We wish you a Merry christmas"
print(str1)
print(str1.isprintable())
str1 = "   "  #using # a = "abc123"

print(str1.isspace())
str2 = "    "    #using tab
print(str2.isspace())


str1 = "World Health Organization"
print(str1.istitle())

str1 = "python is a Interpreted Language"
print(str1.startswith("python"))

str1="He's name is Dan. Dan is an honest man."
print(str1.title())


#kuch or methods
# strip(): dono taraf se space hatata hai
# lstrip(): sirf left se hatata hai
# swapcase(): capital ko small, small ko capital
# isdigit(): sirf numbers hain ya nahi
# isupper(): sab capital hain ya nahi
# zfill(5): aage zero lagata hai
# join(): list ko string mein jodta hai (ye aage lists ke baad)



# practice
# 1
a = "hello"
print(len(a))
print(a.upper())
print(a.capitalize())

# 2
a = "PYTHON"
print(a.lower())

# 3
a = "I like tea"
print(a.replace("tea","coffee"))

# 4
a = "banana"
print(a.count("a"))
print(a.find("n"))

# 5
a = "hello!!!"
print(a.strip("!"))

# 6
a = "python is fun"
print(a.startswith("python"))
print(a.endswith("fun"))

# 7
a = "python is fun" 
print(a.split(" "))

# 8
a = "hello world"
print(a.title())
print(a.capitalize())

# 9
# isalnum() → True, kyunki string mein sirf letters (abc) aur numbers (123) hain, aur kuch nahi.
# isalpha() → False, kyunki ye tabhi True deta hai jab sirf letters ho. Yahan 123 bhi hai.
# isdigit() → False, kyunki ye tabhi True deta hai jab sirf numbers ho. Yahan abc bhi hai.
a = "abc123"
print(a.isalnum())
print(a.isalpha())
print(a.isdigit())

# 10
# isalnum() tabhi True deta hai jab string mein sirf letters aur numbers hon. “hello world” ke beech mein space hai, aur space na letter hai na number, isliye False.
a = "hello world"
print(a.isalnum())   


# 11
a = "  python  "
print(len(a))
print(a.strip())
print(len(a.strip()))


