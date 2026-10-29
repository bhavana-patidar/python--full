# loops = sometimes a programmer wants to executes a group of statements a certain number of times.  this can be doe using loops, based on this loops are further classified into following typs; for loop,while loop,nested loop.

# for loop tab use hota hai jab pata ho kitni baar chalna hai.


name = ' Abhishek'
for i in name:
    print(i)
    if (i =="b"):
        print("This is samething special!")
    

colors = ["Red" , "Green" , "Blue" , "Yellow"]
for color in colors:
    print(color)
    for i in color:
        print(i)

for i in range(5):
    print(i+1)

for i in range(1,20001):
    print(i)

for i in range(1, 12, 3):
    print(i)

# practice
# 1 
for i in range(1,11):
    print(i)

# 2
a = "python"
for i in a:
    print(i)

#3 
name = "Bhaviiii"
for i in name:
    print(i)


#4 
a = "Bhavi"
for i in a:
     print("Letter:",i)

#5
a = "Hello"
for i in a:
     print(i)
print(len(a))


#6
for i in range(1,6):
     print("Numberr:",i)

#7
a = " Bhavi"
for i in a:
    print(i)
print("Done")