
def addition (num1,num2):
	a = num1 +  num2
	print(num1, "+", num2, "=", a)

def substraction (num1, num2):
	s = num1 - num2
	print(num1, "-", num2, "=", s)
	 

def division (num1, num2):
	if num1 == 0 or num2 == 0:
		print('division by zero')
	else:
		d = num1 / num2

def multiplication(num1, num2):
	m = num1 *  num2
	print(num1, "*", num2, "=", m)


print("choose an operator: 1- addition | 2-substraction | 3- division | 4-multiplication") 

choice = input("choose: ") 

n1 = int(input("enter a number: ")) 
n2 = int(input("enter a number: ")) 

if choice == '1': 
	addition(n1, n2)

elif choice == '2': 
	substraction(n1, n2)

elif choice == '3': 
        division(n1, n2)

elif choice == '4':
        multiplication(n1, n2)



