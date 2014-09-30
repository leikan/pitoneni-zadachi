def ABCheck(str):
    for i in range (0, len(str)-4):
        if str[i]=='a' and str[i+4]== 'b':
            return 'true'
    return 'false'    
            
