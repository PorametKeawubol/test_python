def funnyString(s):    
    abs_diff = []  
    for i in range(1, len(s)):
        abs_diff.append(abs(ord(s[i]) - ord(s[i-1])))
    if abs_diff == abs_diff[::-1]:
        return "Funny"
    else:
        return "Not Funny"
