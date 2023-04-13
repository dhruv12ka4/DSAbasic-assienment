# Question 8

def are_brackets_closed(exp):
	stack = []

	for char in exp:
		if char in ["(", "{", "["]:
      
			stack.append(char)
		else:

			if not stack:
				return False
			current_char = stack.pop()
			if current_char == '(':
				if char != ")":
					return False
			if current_char == '{':
				if char != "}":
					return False
			if current_char == '[':
				if char != "]":
					return False
	if stack:
		return False
	return True


exp = input("Enter brackets string : ")

if are_brackets_closed(exp):
	print("closed")
else:
	print("not closed")			    


				    
