# Question 4

string = input("Enter String :")
flag = 0
for i in string:
    if string.count(i) == 1:
        print("First non-repeating character is :", i)
        flag = 1
        break
if flag == 0:
    print("No non-repeating character")
   
    
