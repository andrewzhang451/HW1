# #1
# val = input("Enter the value: ")

# if str(val)==str(val)[::-1]:
#     print("true")
# else:
#     print("false")
    
    
    
#2
normLst = []

userInput = input("Enter value seperated by space: ")
normLst = userInput.split()
normLst.sort()

noDup = [*set(normLst)]
    
print(normLst)
print(noDup)

#3

userInput = input("Enter the value: ")

# if userInput > 3 or 5:
    