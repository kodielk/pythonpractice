'''
This function adds 2 numbers and returns the addition.
Two paramaters: operand1 and operand2
'''
import sys
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
    try:
        res = operand1/operand2
    except ZeroDivisionError:
        print("You need to enter a non zero divisor.")
    return res

def main ():
    

        #input
    try:
        if len(sys.argv)>4:
            print("Too many inputs. Please type two.")

                
        #put other inputs here- the numbers
        choice = str(sys.argv[1])
        operand1 = int(sys.argv[2])
        operand2 = int(sys.argv[3])
        if operand1 or operand2 <0:
            print('cannot proccess a negative number.')
        #processing
        elif choice == 'addition':
            operation='addition'
            opsign='+'
            res = addition(operand1, operand2)
        elif choice == 'subtraction':
            operation='subtraction'
            opsign='-'
            res = subtraction(operand1, operand2)
        elif choice == 'multiplication':
            operation='multiplication'
            opsign='*'
            res = multiplication(operand1,operand2)
        elif choice == 'division':
            operation='division'
            opsign='/'
            res = division(operand1,operand2)
        else:
            print('invalid number of paramaters.')
    except ZeroDivisionError:
        print('Unable to divide by zero.')
        
        

    #output
    
if __name__ == "__main__":
    main()