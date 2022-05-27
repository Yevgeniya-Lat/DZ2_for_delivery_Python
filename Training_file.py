# def decimalToBinary(n):
 
#     if(n > 1):
      
#         decimalToBinary(n//2)
 
     
#     print(n%2, end=' ')

# N = 8
# print(decimalToBinary(N))



# def decimalToBinary(n):
#     return bin(n).replace("0b","")

# N = 8
# print(decimalToBinary(N)) 


# n = int(input())
n = 8 
b = ''
 
while n > 0:
    b = str(n % 2) + b
    n = n // 2
 
print(b)