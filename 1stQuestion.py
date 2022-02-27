# 0. Read a natural number n, then a sequence of n natural numbers from the keyboard.
#  Check whether the given numbers are sorted (ascendingly or descendingly) or not

n = int(input("How many numbers do you want to input: "))
while 2>n:
    n = int(input("number has to be 2 or bigger: "))

i=1
number_list=[]
while int(n)>=i:
    new_number = int(input("please input a number: "))
    number_list.append(new_number)
    i+=1


a=number_list[0]
x=1
passed=False

while n>x:
    if a>number_list[x]:
        a=number_list[x]
        x+=1
        if x>n-1:
            print("it is descending")
            passed=True
    else:
        break

a=number_list[0]
x=1
while n>x:
    if a<number_list[x]:
        a=number_list[x]
        x+=1
        if x>n-1:
            print("it is ascending")
            passed=True
    else:
        break
        

if passed==False:
    print("it is not ascending or descending.")