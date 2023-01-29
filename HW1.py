# #1
val = input("Enter the value: ")

if str(val)==str(val)[::-1]:
    print("true")
else:
    print("false")
    
    
    
# #2
normLst = []

userInput = input("Enter value seperated by space: ")
normLst = userInput.split()
normLst.sort()

noDup = [*set(normLst)]
    
print(normLst)
print(noDup)


# #3
sum = 0

userInput = int(input("Enter the value: "))

for i in range (userInput):
    if i%3==0 or i%5==0:
        sum += i          
print(sum)

# keep incrementing by 1

# until multi < user input

# if userInput is bigger than 3 or 5:

#     print()



# #4
lst = []
wrdCount = 0

userInput = input("Type in your sentence(s): ")

lst = userInput.split()
 
wrdCount = len(lst)

print(lst)

print(wrdCount)



#5
def gen_pattern(letter):
    front = ""
    behind = "" 
    repeat = "" 
    row = "" 
    horizontal = len(letter) 
    for char in letter[::-1]: 
        temp = [front, char, behind] 
        if char == letter[len(letter) - 1]: 
            row = char 
        else:
            row = ".".join(temp) 
        front = row[:int(len(row) / 2) + 1]
        behind = front[::-1] 
        row = row.center((horizontal * 2 + horizontal + 1), ".") 
        repeat += row + "\n" 

    repeat = repeat.rstrip("\n") 
    lines = repeat.split("\n") 
    for i in range((horizontal - 2), -1, -1): 
        repeat = repeat + "\n" + lines[i].rstrip("\n") 
    return repeat 


print(gen_pattern("WXYZ")) #Test case

# print(pyramid("@"))
# print(pyramid("@%"))
# print(pyramid("ABC"))
# print(pyramid("####"))
# print(pyramid("adcdefghijklmnop"))