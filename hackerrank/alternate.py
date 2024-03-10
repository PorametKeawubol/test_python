def alternate(s):  
    max_alternate_length = 0  
    for char1 in set(s):
        for char2 in set(s):           
            if char1 != char2:               
                filtered_s = ''.join(c for c in s if c == char1 or c == char2)             
                is_alternate = all(filtered_s[i] != filtered_s[i+1] for i in range(len(filtered_s) - 1))       
                if is_alternate:
                    max_alternate_length = max(max_alternate_length, len(filtered_s))
    return max_alternate_length
