# break = “bas, ruk jao!”
# Loop wahin khatam. Aage ke round chalte hi nahi.

# Real life example: Maan lo aap 5 aam (mango) check kar rahi ho.       
# break: Teesra aam kharab nikla, aapne gussa hoke bola “bas, baaki check hi nahi karungi!” Toh sirf 2 aam check hue.
# continue: Teesra aam kharab nikla, aapne use side mein rakha aur bola “chalo agla dekhte hain.” Toh 1, 2, 4, 5 check hue, sirf 3 chhoota.


for i in range(12):
    if(i == 10):
            break
    print("5 X", "=", 5 * (i + 1))
print("Loop ko chodkar nikal gaya")

# practice
#1  range(1, 8) mein break use karke sirf 1 se 4 tak print karo (jab i == 5 ho toh ruk jao).
for i in range(1, 8):
    if i == 5:
        break
    print(i)


#2 range(1, 8) mein continue use karke 5 ko chhodke baaki print karo.
for i in range(1, 8):
    if i == 5:
        continue
    print(i)

#3 a = "Python" ke characters print karo, lekin "h" aaye toh break kar do. Output kya aayega?
a = "Python"
for i in a:
    if i == "h":
        break
    print(i)


#4 a = "Python" ke characters print karo, lekin "h" ko continue se skip karo. Output kya aayega?
a = "Python"
for i in a:
    if i == "h":
        continue
    print(i)


#5 while loop mein i = 0 se shuru karke 1 se 5 tak print karo, par i == 3 pe continue lagao. (Hint: i = i + 1 ko continue se pehle rakhna, warna infinite loop banega!)
i = 0
while i < 5:
    i = i + 1
    if i == 3:
        continue
    print(i)
