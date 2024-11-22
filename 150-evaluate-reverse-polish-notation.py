class Solution:
    def performOp(rev_pol_not_exp):
        op1, op2, operator = rev_pol_not_exp
        if operator == "+":
            return int(op1) + int(op2)

        if operator == "-":
            return int(op1) - int(op2)

        if operator == "*":
            return int(op1) * int(op2)

        if operator == "/":
            return int(int(op1) / int(op2))

    def evalRPN(self, tokens: List[str]) -> int:
        operators = {"+", "-", "*", "/"}
        while len(tokens) > 1:
            new_tokens = []
            for i in range(len(tokens)):
                if tokens[i] in operators:
                    new_tokens.append(performOp(tokens[i - 2 : i + 1]))
                else:
                    new_tokens.append(tokens[i])
            tokens = new_tokens
        return new_tokens[0]
