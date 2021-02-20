# Time Complexity = O(n) | Space Complexity = O(n)

def minRemoveToMakeValid(s): 
    def delete_invalid_closing(string, open_symbol, close_symbol):
        sb = []
        balance = 0
        for c in string:
            if c == open_symbol:
                balance += 1
            if c == close_symbol:
                if balance == 0: continue
                balance -= 1
            sb.append(c)
        return "".join(sb)

    s = delete_invalid_closing(s, "(", ")")
    s = delete_invalid_closing(s[::-1], ")", "(")
    return s[::-1]     