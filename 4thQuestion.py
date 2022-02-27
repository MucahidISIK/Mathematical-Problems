# 3. Read a natural number n, then a sequence of n natural numbers. Print the length of the longest sequence of consecutive zeros.
# Ex: [4,0,0,3,0,0,0,11,1,3,0,4,0,0] -> maximum length of consecutive zeros: 3

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
consecutive0s=0
current=0
while n>x:
    if number_list[x]==0:
        a=number_list[x]
        current+=1
        x+=1
        if current>consecutive0s:
            consecutive0s=current
    else:
        current=0
        x+=1

print("Maximum length of consecutive zeros: ", consecutive0s)
