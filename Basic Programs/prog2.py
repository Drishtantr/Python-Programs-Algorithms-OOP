# The function is expected to return a string.
# The function accepts string as parameter.

def logic(my_input):
    x=my_input
    p=True
    c=0
    d=0
    for i in range (len(x)):
        if x[i]=='0':
            c=c+1
        elif x[i]=='1':
            d=d+1
        else:
            p=False
    if (c%2)==0 and (d%2)!=0:
        return "Yes"
    elif p==False:
        return "Not 0 and 1"
    else:
        return "No"






# Do not edit below

# Get the input
my_input = input()

# Print output returned from the logic function
print(logic(my_input))
