# Question 6

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

def post_to_pre(post_exp):

	s = []
	length = len(post_exp)

	for i in range(length):

		if (is_operator(post_exp[i])):

			op1 = s[-1]
			s.pop()
			op2 = s[-1]
			s.pop()

			temp = post_exp[i] + op2 + op1
			s.append(temp)
		else:
			s.append(post_exp[i])

	
	pre = ""
	for i in s:
		pre += i
	return pre



post_exp = input("Enter Postfix Expression :")
print("Prefix Expression : ", post_to_pre(post_exp))
