## Description

Do you want to play crosswords? Just take it diagonally and never skip the algebra course again.

## Solution

we were given a text file :

```
└─$ cat the_wise_man.txt

}yvtK_XtwICghIzPPUlCMJJMBcfm}QXeexprWLEgxiJlFy{PqlbiShphiPgyG{jOEBgOjpwaTUEhNlHMTbe_fePsrzZozgf
...
mIpAjflXnsYEfsVtSt}vc}ZcWuTG{A}DKrfTXVSgHDvxTukmIOLsCthCLWIDbM}ulOqMCEDKwMeDpzgnfW, it seems you don't like my story, but trust me, it contains letters written in gold, priceless for those who understand it ...
```

okey, we have a weird looking string, a hint from the authors states that it has to do with diagonal matrix, and if we check the number of characters in that file we get `47089` :

```
└─$ wc -c the_wise_man.txt
47089 the_wise_man.txt
```

if we calculate the square root of that number we get `217` :

```
>>> 47089**0.5
217.0
```

this hints that the string might be in form of a square matrix, this means we can make an imaginary row every `217` characters and we would get 217 rows and 217 columns which is a form of a square matrix.

another hint states that the juicy stuff are in the diagonals of that matrix, so we can create a python script that get the diagonals of this imaginary matrix :

```python
└─$ cat slicing.py
for j in range(0,217):
    output=open("the_wise_man.txt","r").read()
    outstr=""
    count=j
    for i in range(0,217-j):
        outstr=outstr+output[count]
        count=count+218
    if "shellmates" in outstr:
```

let's run it :

```
└─$ python3 slicing.py
Found The Flag !! ==> finally_the_golden_letters_shellmates{YOu_vE_eaRnEd_w1$d0M_4ND_MaTH$Ss}_no_needy}WUEnxQ_by
```

- flag: `shellmates{YOu_vE_eaRnEd_w1$d0M_4ND_MaTH$Ss}`
