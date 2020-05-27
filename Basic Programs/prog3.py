# The function is expected to return an integer.
# The function accepts string as parameter.

def logic(my_input):
    x=my_input
    h=len(x)
    if x[0]!=x[1]:
        h-=1
    if x[-1]!=x[-2]:
        h-=1

    for i in range(1,len(x)-1,1):
        if x[i]!=x[i-1] and x[i]!=x[i+1]:
            h-=1
    
    return h


# Do not edit below

# Get the input
my_input = input()

# Print output returned from the logic function
print(logic(my_input))
