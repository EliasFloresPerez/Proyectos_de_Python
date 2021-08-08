txt=[">","<"]
for i in range(1,10):
    str="@"*i
    p=' '*(10-i)
    print("",end=p)
    print(str.join(txt))
