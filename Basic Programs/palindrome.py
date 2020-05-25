def pal(st):
    st=st.casefold()
    # print (st)
    rst=reversed(st)
    # print (rst)
    if list(st)==list(rst):
        return "P"
    else:
        return "N P"
st=input()
print(pal(st))