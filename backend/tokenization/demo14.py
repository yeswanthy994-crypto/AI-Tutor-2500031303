n=int(input("Enter the number of entries : ") )
students = {}
for i in range(n):
    key=input("Enter key : ")
    value=input("Enter value : ")
    students[key]=value
print("Students dictionary : ", students)