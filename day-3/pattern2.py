def num_pattern(num):
    for i in range(1,num+1):
        for j in range(1,i+1):
           print(j,end=" ")
        print('')
num_pattern(5)

def num_pattern_rev(num):                
    for i in range(1, num + 1):
        print((num - i) * " ", end=" ")
        for j in range(1, i + 1):                
            print(j, end="")
        
        print('')                

num_pattern_rev(5)