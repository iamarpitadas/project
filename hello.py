# Area of the circle

x=input("Enter the radius of the circle :")
r=int(x)
a=3.14*r**2
print("area of the circle",a)



# Print the extension

filename= input("input of the Filename:")
f_extns=filename.split(".")
print("The extension of the file is:"+ repr(f_extns[-1]))



# positive number in a range

start=int(input("Enter the start of range:"))
end=int(input("Enter the end of range:"))
for num in range(start, end+1):
    if num>=0:
        print(num,end=" ")

        
        
#fibonacci

n=int(input("enter how many no you want:"))
a=0
b=1
for i in range(n):
    print(a)
    c=a
    a=b
    b=c+b


