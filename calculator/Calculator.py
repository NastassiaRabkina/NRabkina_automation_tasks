from datetime import datetime
import os

class InputValidator(object):
    """this class validates users input before calculation"""

    def is_input_valid(self):
        while True:
            x = input("Enter Value:")
            try:
                x = float(x)
            except:
                print("Input must be digital value")
                continue

            if x > 20:
                print ("Input must be in between -20 and 20")
                continue
            elif x < -20:
                print ("Input must be in between -20 and 20")
                continue
            else:
                break
        return x

    def is_operator_valid(self):
        while True:
            x = input("Enter Operator:")

            if x not in ["+", "-", "*", "/"]:
                print("Operator must be +, -, * or /")
                continue
            else:
                break
        return x

class Calculator(object):
    """this class performs calculation"""

    def adding(self,a,b):
        result = a + b
        return result

    def subtracting(self,a,b):
        result = a - b
        return result

    def multiplying(self,a,b):
        result = a * b
        return result

    def dividing(self,a,b):
        result = a / b
        return result

class FileSaver(object):
    """this class is to write the results to a results.txt file"""

    def write_to_file(self,res):
        path = os.getcwd()
        filepath = os.path.join (path, 'results.txt')
        with open(filepath, 'a') as f:
                f.write(res)
                f.write('\n')

    def add_date_time(self, log):
        date = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
        result = date + ": " + log
        return result


#verify input
val = InputValidator()
calc = Calculator()
save = FileSaver()

run_loop = True

while run_loop:

    op_a = val.is_input_valid()
    print("A =", op_a)
    op_b = val.is_input_valid()
    print("B = ", op_b)
    opr = val.is_operator_valid()
    print("Operator: ", opr)

    #perform calculation

    if opr == "+":
        calc_result = calc.adding(op_a, op_b)
    elif opr == "-":
        calc_result = calc.subtracting(op_a, op_b)
    elif opr == "*":
        calc_result = calc.multiplying(op_a, op_b)
    else:
        calc_result = calc.dividing(op_a, op_b)

    #add current time and date and add calculation to a file
    log = str(op_a) + ' ' + opr + ' ' + str(op_b) + ' = ' + str(calc_result)

    result = save.add_date_time(log)
    save.write_to_file(result)
    print("Operation complete. \n")

    next_op = ''
    while next_op not in ("y", "n"):
        next_op = input("Continue(y/n)?")    
        if next_op == "y":
            run_loop = True
        elif next_op == "n": 
            run_loop = False   
      

