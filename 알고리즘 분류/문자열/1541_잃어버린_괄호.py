import sys

expression = sys.stdin.readline().rstrip()

operands, operators = [], []
operand = ""
for i in range(len(expression)+1):
    if i<len(expression):
        if expression[i].isdigit():
            operand += expression[i]
        else:
            operands.append(int(operand))
            operand = ""
            operators.append(expression[i])
    else:
        operands.append(int(operand))

# print(operators)
# print(operands)

i = 1
min_sum = operands[0]
while i < len(operands):
    # print("here1's i : ",i)
    if operators[i-1] == '-':
        sub_sum = operands[i]
        i += 1
        while i < len(operands) and operators[i-1] == '+':
            # print("here1's i : ", i)
            sub_sum += operands[i]
            i += 1
        min_sum -= sub_sum
    else:
        sub_sum = operands[i]
        i += 1
        while i < len(operands) and operators[i-1] == '+':
            # print("here1's i : ", i)
            sub_sum += operands[i]
            i += 1
        min_sum += sub_sum

print(min_sum)