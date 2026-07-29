from stack import Stack


def is_balanced(input_string):
    stack = Stack()
    brackets = {
        '(':')',
        '{':'}',
        '[':']'
    }

    for symbol in input_string:
        if symbol in brackets:
            stack.push(symbol)
        else:
            if stack.is_empty() or brackets[stack.pop()] != symbol:
                return False

    return stack.is_empty()


# Test 1
stack = Stack()
assert stack.is_empty() == True
stack.push(1)
stack.push(2)
stack.push(3)
assert stack.is_empty() == False
assert stack.size() == 3
assert stack.get_items() == [1, 2, 3]
assert stack.peek() == 3
assert stack.pop() == 3
assert stack.pop() == 2
assert stack.pop() == 1
print(stack.size())
assert stack.is_empty() == True

# Test 2
assert is_balanced("(({}))") == True
