## Description

== or !=, are u sure?

**source code available**

## Solution

we were given a server to connect to ` ncat -v --ssl equal5butnotequal5.hackini24.shellmates.club 443`, let's connect :

```
└─$  ncat --ssl equal5butnotequal5.hackini24.shellmates.club 443
a =
No No No ...
```

hmm, let's check the source code :

```python
import os
try:
    a = float(input('a = '))
    if a == a:
        print('No No No ...')
    else:
        flag = open('flag.txt', 'r').read()
        print(flag)
except:
    print('No No No ...')
```

we see that it saves our input to a variable called `a`, then it compares this variable to it self, and if it's not equal to it self, we get the flag.

we notice that our input is getting converted to a `float`, we can use `nan` which stands for `Not a Number`, if we compare this value with it self we get `False` as we see in this example :

```
>>> a = float('nan')
>>> print(a==a)
False
```

let's try that on the challenge :

```
a = nan
shellmates{eKwaL5_8U7_N07_eKWAl5_W17h_Nan}
```

- flag: `shellmates{eKwaL5_8U7_N07_eKWAl5_W17h_Nan}`
