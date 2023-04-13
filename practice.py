# Question 5

def tower_of_hanoi(disks, source, auxiliary, target):
    if disks == 1:
        print('Move disk 1 from location {} to location {}.'.format(source, target))
        return
 
    tower_of_hanoi(disks - 1, source, target, auxiliary)
    print('Move disk {} from location {} to location {}.'.format(disks, source, target))
    tower_of_hanoi(disks - 1, auxiliary, source, target)
 
 
disks = int(input('Enter number of disks: '))
tower_of_hanoi(disks, 'A', 'B', 'C')
