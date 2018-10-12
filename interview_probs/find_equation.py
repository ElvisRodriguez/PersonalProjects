'''
Given an array of 2 to 5 numbers and a value, return a string representing the
equation that uses all the numbers in the array (once each) to equal the value.
You can only use each operation (*, +, -, /) once each.
(TODO): fix is_valid_equation to perform proper order of operations
'''

import itertools

def format_equation(equation, value):
    result = [str(item) for item in equation]
    result.extend(['=', str(value)])
    result = ' '.join(result)
    return result

def is_value(equation, value):
    result = equation[0]
    for i in range(1, len(equation) - 1, 2):
        if equation[i] == '+':
            result += equation[i+1]
        elif equation[i] == '-':
            result -= equation[i+1]
        elif equation[i] == '*':
            result *= equation[i+1]
        else:
            result /= equation[i+1]
    return result == value

def is_valid_equation(tup_seq):
    validators = []
    for i in range(len(tup_seq)):
        if i % 2 == 0:
            validators.append(int())
        else:
            validators.append(str())
    for j in range(len(tup_seq)):
        if type(tup_seq[j]) != type(validators[j]):
            return False
    return True

def find_equation(nums, value):
    operations = ['+', '-', '/', '*']
    possible_equations = nums + operations
    size = len(nums) + (len(nums) - 1)
    all_seqs = itertools.permutations(possible_equations, size)
    possible_answers = [seq for seq in all_seqs if is_valid_equation(seq)]
    for answer in possible_answers:
        if is_value(answer, value):
            return format_equation(answer, value)
    return 'no equation possible for %i' % (value)


if __name__ == '__main__':
    print(find_equation([5, 2, 6, 4, 2], 36))
