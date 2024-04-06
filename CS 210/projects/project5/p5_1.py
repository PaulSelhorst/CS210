# Implement your solutions here. Remember to follow PEP8 Style Guide .
# Do not forget to click SUBMIT -- you can submit multiple times without penalty.
#

# pass means the function will be defined later (by you)
# pass is ignored by the Python interpreter and will avoid 
# the error signal of an empty function.

def is_operator(operator:str) ->bool:
    if operator in ['+', '-', '*', '/']:
        return True
    else:
        return False
    
def is_operand(operand:str) ->bool:
    if operand.lstrip("-").isdigit():
        return True
    else:
        return False
    
def apply_operator(op:str, oper_1:float, oper_2:float) ->float:
    if op == '+':
        return oper_1 + oper_2
    elif op == '-':
        return oper_1 - oper_2
    elif op == '*':
        return oper_1 * oper_2
    elif op == '/':
        return oper_1 / oper_2
    else:
        return 0.0


def eval_postfix(expr_str:str)->float:
    b = expr_str.split()
    stack = []
    counter_operand = 0
    counter_operator = 0
    for i in b:
        if is_operand(i):
            counter_operand += 1
        elif is_operator(i):
            counter_operator += 1
    if counter_operand - counter_operator != 1:
        return "error on postfix expression"
    for i in b:
        if is_operand(i):
            stack.append(i)
        elif is_operator(i):
            oper_2 = stack.pop()
            oper_1 = stack.pop()
            stack.append(apply_operator(i, float(oper_1), float(oper_2)))
        else:
            return "error on postfix expression"
        
    return stack.pop()


print(eval_postfix("3 4 - 7 * "))