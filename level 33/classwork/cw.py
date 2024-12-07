def manual_swapcase(string):
    result = ""
    for char in string:
        if 'a' <= char <= 'z':  
            result += chr(ord(char) - 32)
        elif 'A' <= char <= 'Z':  
            result += chr(ord(char) + 32)
        else:
            result += char
    return result

