# Question 1

def find(array, len, summ):
    print('pairs whose sum is : ', summ)
    for i in range(len):
        for j in range(i, len):
            if (array[i] + array[j]) == summ:
                print(f'[{array[i]}, {array[j]}]')

        print('no match found')


array = [int(item) for item in input('enter the No.s in 1 2 3 ... format : ').spilt()]
summ = int(input('enter sum : '))
print('array = ', array)
find(array, len(array), summ)

