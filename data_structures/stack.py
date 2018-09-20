class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return self.items == []

    def peek(self):
        if not self.is_empty:
            return self.items[-1]


def is_match(p1, p2):
    if p1 == "(" and p2 == ")":
        return True
    if p1 == "{" and p2 == "}":
        return True
    if p1 == "[" and p2 == "]":
        return True
    return False

def is_paren_balanced(paren_string):
    s = Stack()
    index = 0
    balanced = True
    while index < len(paren_string):
        paren = paren_string[index]
        if paren in "([{":
            s.push(paren)
        elif s.is_empty():
            balanced = False
        elif not is_match(s.pop(), paren):
            balanced = False
        index += 1
    if s.is_empty() and balanced:
        return True
    else:
        return False

def main():
    print(is_paren_balanced("()"))
    print(is_paren_balanced("()()"))
    print(is_paren_balanced("(({[]}))"))
    print(is_paren_balanced("{[]}"))
    print(is_paren_balanced("(()"))
    print(is_paren_balanced("{\{\{)}]"))
    print(is_paren_balanced("[][]]]"))
    print(is_paren_balanced("))"))

main()
