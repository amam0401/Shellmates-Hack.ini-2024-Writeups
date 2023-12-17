for j in range(0,217):
    output=open("the_wise_man.txt","r").read()
    outstr=""
    count=j
    for i in range(0,217-j):
        outstr=outstr+output[count]
        count=count+218
    if "shellmates" in outstr:
        print(f"Found The Flag !! ==> {outstr}")
