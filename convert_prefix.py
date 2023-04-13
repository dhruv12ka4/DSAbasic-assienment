# Question 7

def is_operator(x):

	if x == "+":
		return True

	if x == "-":
		return True

	if x == "/":
		return True

	if x == "*":
		return True

	return False

def prefix_to_infix(prefix_exp):
    stack = []
     
    i = len(prefix_exp) - 1
    while i >= 0:
        if not is_operator(prefix_exp[i]):
             
            stack.append(prefix_exp[i])

        else:
           
            str = "(" + stack.pop() + prefix_exp[i] + stack.pop() + ")"
            stack.append(str)
        
        i-=1
     
    return stack.pop()

prefix_exp = input("Enter Prefix Expression :")
print("Infix Expression : ", prefix_to_infix(prefix_exp))
