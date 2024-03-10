def caesarCipher(s, k):  
    result = ''   
    for char in s:     
        if char.isalpha():      
            shift = k % 26 if char.islower() else k % 26 - 26        
            encrypted_char = chr(((ord(char) - ord('a' if char.islower() else 'A') + shift) % 26)
                                 + ord('a' if char.islower() else 'A'))          
            result += encrypted_char
        else:        
            result += char
    return result