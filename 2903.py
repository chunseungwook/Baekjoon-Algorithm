num1, num2 = input().split()
print(type(num1))

reverse_num1 = num1[::-1]
reverse_num2 = num2[::-1]    

if reverse_num1 > reverse_num2:
    print(reverse_num1)
else:
    print(reverse_num2)
    
