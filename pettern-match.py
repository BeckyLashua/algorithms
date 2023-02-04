def patternmatch(string, p):
    str_pointer = -1
    p_pointer = -1

    i = 0
    j = 0

    while i < len(string):
        if (string[i] == p[j] or p[j] == '?') and j < len(p):
            i = i + 1
            j = j + 1
        elif p[j] == '*' and j < len(p):
            str_pointer = i
            p_pointer = j 
            j = j + 1
        elif str_pointer >= 0:
            str_pointer = str_pointer + 1
            i = str_pointer 
            j = p_pointer + 1
        else:
            return False
    while j < len(p) and p[j] == '*':
        j = j + 1 
    return j == len(p)  


