def infix_2_postfix(expression):
    expression= list(expression)
    op_stack =[]
    postfix = []
    oprands = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    opprecedence ={'(':1,'+':2,'-':2,'*':3,'/':3}
    for token in expression:
        if token in oprands:
            postfix.append(token)
        elif token=='(':
            op_stack.append(token)
        elif token==')':
            op = op_stack.pop()
            while op_stack!=[] and op!='(':
                  postfix.append(op)
                  op = op_stack.pop()
        else:
            while op_stack!=[] and opprecedence[op_stack[-1]
                    ]>=opprecedence[token]:
                   op = op_stack.pop()
                   postfix.append(op)
            op_stack.append(token)
            print(op_stack)


    while op_stack!=[]:
        postfix.append(op_stack.pop())

    postfix_exp=''.join(postfix)
    return postfix_exp


def evaulation(postfix):
    exp = list(postfix)
    oprands_stack = []
    for token in exp:
        if token in '0123456789':
            oprands_stack.append(token)
        else:
            oprand2 = int(oprands_stack.pop())
            oprand1 = int(oprands_stack.pop())
            result = domath(token,oprand1,oprand2)
            oprands_stack.append(result)

    return oprands_stack[0]

def domath(op,oprand1,oprand2):
    if op=='+':
        return oprand1+oprand2
    elif op=='-':
        return oprand1-oprand2
    elif op=='*':
        return oprand1*oprand2
    else:
        return oprand1/oprand2

