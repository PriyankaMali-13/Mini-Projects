def CheckPassword(s):
    upper = False
    number = False
    if len(s)<4:
        return 0
    elif s[0].isdigit():
        return 0
    
    for i in range(len(s)):
        if s[0] == '/' or s[0]==' ':
            return 0
        elif s[i].isupper():
            upper = True
        elif s[i].isdigit():
            number = True
    if number == True and upper == True:
        return 1
    else:
        return 0
    
s = input()
print(CheckPassword(s))