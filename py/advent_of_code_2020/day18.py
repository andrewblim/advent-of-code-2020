import sys
import re
from collections import deque


def tokenize(input):
    input = re.sub(r"\(", "( ", input)
    input = re.sub(r"\)", " )", input)
    return deque(input.split())


def eval_tokens(tokens):
    val_stack = []
    op_stack = []
    while len(tokens) > 0:
        c = tokens.popleft()
        if c == "+" or c == "*":
            op_stack.append(c)
        elif c == "(":
            op_stack.append(c)
        elif c == ")":
            close = op_stack.pop()
            if close != "(":
                raise RuntimeError("mismatched parentheses")
            tokens.appendleft(val_stack.pop())
        else:
            val = int(c)
            if len(op_stack) > 0:
                if op_stack[-1] == "+":
                    val += val_stack.pop()
                    op_stack.pop()
                elif op_stack[-1] == "*":
                    val *= val_stack.pop()
                    op_stack.pop()
            val_stack.append(val)
    if len(val_stack) != 1:
        raise RuntimeError("ended without 1 value on the val stack")
    if len(op_stack) != 0:
        raise RuntimeError("ended without 0 operations on the op stack")
    return val_stack.pop()


def eval_expr(expr):
    return eval_tokens(tokenize(expr))


def eval_tokens2(tokens):
    val_stack = []
    op_stack = []
    while len(tokens) > 0:
        c = tokens.popleft()
        if c == "+" or c == "*":
            op_stack.append(c)
        elif c == "(":
            op_stack.append(c)
        elif c == ")":
            val = val_stack.pop()
            op = op_stack.pop()
            while op != "(":
                if op == "*":
                    val *= val_stack.pop()
                    op = op_stack.pop()
                else:
                    raise RuntimeError("mismatched parentheses/unexpected op")
            tokens.appendleft(val)
        else:
            val = int(c)
            if len(op_stack) > 0 and op_stack[-1] == "+":
                val += val_stack.pop()
                op_stack.pop()
            val_stack.append(val)

    val = val_stack.pop()
    while len(op_stack) > 0:
        op = op_stack.pop()
        if op == "*":
            val *= val_stack.pop()
        else:
            raise RuntimeError("mismatched parentheses/unexpected op")
    if len(val_stack) != 0:
        raise RuntimeError("ended with values on the val stack")
    return val


def eval_expr2(expr):
    return eval_tokens2(tokenize(expr))


if __name__ == "__main__":
    with open(sys.argv[1], "r") as fp:
        input = [x.strip() for x in fp.readlines()]
    print("Part 1:")
    print(sum([eval_expr(x) for x in input]))
    print("Part 2:")
    print(sum([eval_expr2(x) for x in input]))
