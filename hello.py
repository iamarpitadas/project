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
    
    
    
    
 # school admission program

import csv

def write_into_cvs(info_list):
    with open("student_info.cvs", 'a', newline='') as csv_file:
        writer = csv.writer(csv_file)


        writer.writerow(info_list)

condition= True

while(condition):
    student_info = input("Enter student information in following format (Name Standard Section Roll_no)")
    print("Entered information: "+ student_info)

    #split
    student_info_list= student_info.split(' ')
    print("Entered split up information is:" + str(student_info_list))

    write_into_cvs(student_info_list)

    continue_input = input(" Enter (yes or no) if you want to add information of another student : ").lower()
    print("\n")
    if continue_input == "Yes":
        condition = True
    elif continue_input == "no":
        condition = False







