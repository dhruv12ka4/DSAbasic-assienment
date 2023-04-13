# Question 2

def reverseList(array):
    start = 0
    end = len(array) - 1
    while start < end:
        array[start], array[end] = array[end], array[start]
        start += 1
        end -= 1

array = [int(item) for item in input("Enter the No.s in 1 2 3 ... format : ").split()]
print(array)
reverseList(array)
print("Reversed array is :")
print(array)
















   
