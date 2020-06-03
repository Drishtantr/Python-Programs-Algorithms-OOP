def logic(my_input):

    #zylophone
    if my_input.startswith('x')==True and len(my_input)>0:
        new=my_input.replace(my_input[0],"z")
        return new

    #ecks
    elif my_input.startswith('x')==False:
        for i in range(len(my_input)):
            if my_input[i]=='x':
                new=my_input.replace('x','ecks')
        return new
   
    #x ray

    else:
        p=my_input.split(" ")
        for i in range(len(p)):
            if p[i]=='x':
                p.pop(i)
                p.insert(i,'cks')
        j=" "
        new=j.join(p)
        return new


        




# Do not edit below

# Get the input
my_input = input()

# Print output returned from the logic function
print(logic(my_input))