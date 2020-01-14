

#Countdown
def Countdown(num):
    my_list = []
    for i in range(num,-1,-1):
        my_list.append(i)
    return my_list

x = Countdown(5)
print(x)


#Print and Return
def PrintAndReturn(list):
    print(list[0])
    return list[1]

my_list = []
my_list.append(1)
my_list.append(4)
x = PrintAndReturn(my_list)
print(x)


#First Plus Length
def FirstPlusLength(list):
    return list[0] + len(list)

x = FirstPlusLength([1,3,5,7,8,9,10])
print(x)

#Values Greater than Second
def GreaterThanSecond(list):
    new_list = []
    total = 0
    for i in range(0,len(list),1):
        if list[i] > list[1]:
            new_list.append(list[i])
            total += 1
    print(total)
    return new_list

x = GreaterThanSecond([1,5,9,12,412,2,9])
print(x)

#This Length That Value
def ThisLengthThatValue(num1, num2):
    newList = []
    for i in range(0, num1, 1):
        newList.append(num2)
    return newList

x = ThisLengthThatValue(5,2)
print(x)


