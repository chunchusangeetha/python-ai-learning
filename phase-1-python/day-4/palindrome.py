def ispalindrome(val):
    if type(val) == str:
        reverse = ""
        for char in val:
            reverse = char + reverse
        if(reverse == val):
               return True 
        else:
           return False       
    elif type(val) == int :
        rev_num = 0
        org_num = val
        while val > 0:
            digit = val % 10
            rev_num = rev_num*10+digit
            val = val//10
        if(rev_num == org_num):
            return True   
        else:
            return False    
    else:
        return "not a num or str"    

print(ispalindrome("heh"))
print(ispalindrome("heh"))
print(ispalindrome(12346))
print(ispalindrome("121strrts121"))