# #1
# val = input("Enter the value: ")

# if str(val)==str(val)[::-1]:
#     print("true")
# else:
#     print("false")
    
    
    
# #2
# normLst = []

# userInput = input("Enter value seperated by space: ")
# normLst = userInput.split()
# normLst.sort()

# noDup = [*set(normLst)]
    
# print(normLst)
# print(noDup)


# #3

# sum = 0

# userInput = int(input("Enter the value: "))

# for i in range (userInput):
#     if i%3==0 or i%5==0:
#         sum += i          
# print(sum)

#keep incrementing by 1

#until multi < user input

# if userInput is bigger than 3 or 5:

#     print()



# #4
# lst = []
# wrdCount = 0

# userInput = input("Type in your sentence(s): ")

# lst = userInput.split()
 
# wrdCount = len(lst)

# print(lst)

# print(wrdCount)



#5

# def pyramid(x:str):
#     st = ""
#     n = (len(x) * 2) - 1
#     for i in range(n):
#         temp1 = x[0:i+1]
#         temp2 = x[i:0:-1]
#         temp = ".".join(temp2 + temp1)
#         temp = temp.center(4*n-3, ".")
#         st += temp
#         if i != n-1:
#             st += "\n"
        
#     return st
# print(pyramid("WXYZ"))

def pyramid(x:str):
    st = ""
    n = (len(x)*2)-1
    for i in range(n):
        temp1 = x[-i+1:0:-1]

    return st
print(pyramid("WXYZ"))

#@2:03:53 of video is where i talks about this

# print(pyramid("@"))
# print(pyramid("@%"))
# print(pyramid("ABC"))
# print(pyramid("####"))
# print(pyramid("adcdefghijklmnop"))


