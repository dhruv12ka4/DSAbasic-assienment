# Question 3

def Check_Rotations(string1, string2):
 
    if len(string1) != len(string2):
        return False
 
    temp = string1 + string1
 
    if ( temp.count(string2) > 0):
        return True
    else:
        return False

string1 = input("Enter String 1 : ")
string2 = input("Enter String 2 : ")
 
if Check_Rotations(string1, string2):
    print("Strings are rotations of each other")
else:
    print("Strings are not rotations of each other")
 
