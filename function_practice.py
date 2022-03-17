# 1. Countdown:
def countdown(num):
    for i in range(num,-1,-1):
        print(i)
countdown(5)

# 2. Print and Return:
def print_and_return(num1,num2):
    print(num1)
    return(num2)
print(print_and_return(1,2))

#  3. First plus Length:
arr = [1,2,3,4,5]
def first_plus_length():
    total = arr[0] + len(arr)
    return total
print(first_plus_length())

#  4. Values Greater than Second:

def values_greater_than_second(list):
    if len(list) < 2:
        return False
    output = []
    for i in range(0,len(list)):
        if list[i] > list[1]:
            output.append(list[i])
    print(len(output))
    return output


print(values_greater_than_second([5,2,3,2,1,4]))
print(values_greater_than_second([3]))


# 5.  This Length, That Value:

def length_and_value(size, value):
    output = []
    for i in range(0,size):
        output.append(value)
    return output

print(length_and_value(4,7))
print(length_and_value(6,2))
