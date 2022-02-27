# 2. Read a natural number n, then a sequence of n natural numbers from the keyboard. Calculate the minimum, sum,
#  average and maximum of the elements of the sequence, 
# as well as the sum of squares of the elements of the sequence 

n = int(input("How many numbers do you want to input: "))
while 2>n:
    n = int(input("number has to be 2 or bigger: "))

i=1
number_list=[]
while int(n)>=i:
    new_number = int(input("please input a number: "))
    number_list.append(new_number)
    i+=1

minimum=0
maximum=0
sum=0
average=0
sum_of_squares=0

a=number_list[0]
x=1
while n>x:
    if a>number_list[x]:
        a=number_list[x]
        x+=1
            
    else:
        x+=1

minimum=a
print("minimum: ", minimum)

a=number_list[0]
x=1
while n>x:
    if a<number_list[x]:
        a=number_list[x]
        x+=1
            
    else:
        x+=1

maximum=a
print("maximum: ", maximum)

x=0
while n>x:
    sum+=number_list[x]
    x+=1

print("sum :",sum)

average=sum/n
print("average: ",average)

a=number_list[0]
x=0
while n>x:
    sum_of_squares += number_list[x]*number_list[x]
    x+=1
      
print("sum of squares of the elements : ", sum_of_squares)