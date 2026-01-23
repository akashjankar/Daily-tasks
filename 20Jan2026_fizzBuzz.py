
list=[1,29,9,5,15,96]

i=0

for i in range(0,len(list)):
    if(list[i]%3==0 and list[i]%5==0):
        list[i]="FizzBuzz"
    elif(list[i]%3==0):
        list[i]="Fizz"
    elif(list[i]%5==0):
        list[i]="Buzz"
    i+=1

print("List after game=", list)