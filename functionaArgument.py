 
# 1. Default arguments: we can provide a default value while creating a function . this way the function assumes a default value if a value is not provided in the function call for that arguments.
# Default → agar value na di jaye toh kya ho: pehle se rakhi value use hoti hai.

def average (a=9, b=1):
    print("The avarage is ",(a+b)/2)
average(b=9)

# 2. Keyword arguments: call karte waqt parameter ka naam likhke value dete hain (naam=value). Isliye order matter nahi karta.

def intro(name, age):
    print(name, age)

intro("Bhavi", 20)        # positional: order se
intro(age=20, name="Bhavi")   # keyword: naam se, order ulta bhi chalega


# 3.Variable-length arguments : Jab pata nahi ki kitne arguments aayenge. *args kitni bhi positional values leta hai, aur **kwargs kitni bhi keyword values leta hai.

# 4.Required arguments : Wo arguments jo function ko dene hi padte hain. Agar nahi diye toh error aata hai.

# 5. Positional arguments = Value usi order mein jati hai jis order mein parameters likhe hain.


# practice:

#1 
def greet(name):
    print("Hello,", name)
    
greet("bhavi")


#2
def add(a, b):
    print("the addon is" , a+b )

add(10, 20)
add(100,50)

#3
def intro(name, age=18):
    print(name, age)

intro("Bhavi")
intro("bhavi",  20)    # yahan naam aur age dono do

