class StringProcessor():
    def __init__(self):
        self.stack = []

    def reverse(self,s):
        tmp = ""
        for i in range(len(s)-1,-1,-1):
            tmp = tmp + s[i]
        return tmp

    def process_sequence(self,s):
        tmp = ""
        for i in range(len(s)):
            if (s[i] == '*'):
                tmp += self.stack.pop()
            else:
                self.stack.append(s[i])
        self.stack.clear()
        return tmp

    def binary_string(self,n):
        tmp = ""
        if n == 0:
            return "0"

        while (n > 0):
            digit = n % 2
            tmp += str(digit)
            n //= 2

        return self.reverse(tmp)

    def is_balanced(self,s):
        s_is_balanced = True

        for c in s:
            if (c == '{' or c == '(' or c == '['):
                self.stack.append(c)
            elif (c == '}' or c == ')' or c == ']'):
                if (len(self.stack) == 0):
                    s_is_balanced = False
                    break
                else:
                    top_stack = self.stack.pop()
                    if (top_stack == '{' and c == '}'):
                        pass
                    elif (top_stack == '(' and c == ')'):
                        pass
                    elif (top_stack == '[' and c == ']'):
                        pass
                    else:
                        s_is_balanced = False
                        break
        
        if (s_is_balanced and len(self.stack) > 0):
            s_is_balanced = False

        self.stack.clear()
        return s_is_balanced

a = StringProcessor()
# print(a.reverse("abcxyz"))

# print(a.is_balanced("{(}"))