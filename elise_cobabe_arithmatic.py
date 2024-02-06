'''
This function adds 2 numbers and returns the addition.
Two paramaters: operand1 and operand2
'''
#definitions of the functions
def addition(operand1,operand2):
    '''adds operand 1 and operand 2. (inputted by user)'''
    res = operand1 + operand2
    return res
def subtraction(operand1,operand2):
    '''subtracts operand 1 and operand 2. (inputted by user)'''
    res = operand1 - operand2
    return res
def multiplication(operand1,operand2):
    '''multiplies operand 1 and operand 2. (inputted by user)'''
    res = operand1*operand2
    return res
def division(operand1,operand2):
    '''divides operand1 and operand 2. (inputted by user)'''
    res = operand1/operand2
    return res

def main ():
    while True:
        #promt
        print('''Welcome to the Arithmetic Operations Program!
        Menu:
        1. Addition
        2. Subtraction
        3. Multiplication
        4. Division
        5. Exit''')

        #input
        try:
            choice = int(input("Enter your choice (1/2/3/4/5): "))
            if choice == 5:
                    print("Farewell.")
                    break
            #put other inputs here- the numbers
            operand1 = float(input('Enter the first number:'))
            operand2 = float(input('Enter the second number:'))
            #processing
            if choice == 1:
                operation='addition'
                opsign='+'
                res = addition(operand1, operand2)
            elif choice == 2:
                operation='subtraction'
                opsign='-'
                res = subtraction(operand1, operand2)
            elif choice == 3:
                operation='multiplication'
                opsign='*'
                res = multiplication(operand1,operand2)
            elif choice == 4:
                operation='division'
                opsign='/'
                res = division(operand1,operand2)
            if choice != 5:
                print(f"Result of {operation}: {operand1}{opsign}{operand2}={res}")
                choice = input(("Would you like to continue?(y/n)"))
                if choice==("n"):
                    break


        except:
            print('You need to enter either 1/2/3/4 or 5, or you tried to divide by 0.')
        
        

    #output
    
if __name__ == "__main__":
    main()