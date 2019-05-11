from Stack import *
#para checker using stack
# ALgo : insert open braces in stack
# for closure : if closure brace is found pop the stack
# at last if the stack is empty then its a balanced paranthesis

def paracheck(p_set):
    s = Stack()
    index = 0

    while index < len(p_set):
        if p_set[index] in "({[":
            s.push(p_set[index])
        else:
            s.pop()
        index += 1

    return s.isEmpty()

print("TRUE") if paracheck("({[]") else print("False")