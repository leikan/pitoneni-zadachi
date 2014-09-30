def dashInsert(num):
    str1=''
    result='' 
    str1= str(num)
    for i in range (0,len(str1)-1):
        result+=str1[i]
        if int (str1[i])%2==1 and int(str1[i+1])%2==1:
            result+='-'
    result+= str1[len(str1)-1]
    return result
