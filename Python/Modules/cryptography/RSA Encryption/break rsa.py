# all prime factors p and q factorise of n
x = [2434792384523484381583634042478415057961, 650809615742055581459820253356987396346063]

# n
n = 1584586296183412107468474423529992275940096154074798537916936609523894209759157543

# e
e = 65537

# cipher text
ct = 964354128913912393938480857590969826308054462950561875638492039363373779803642185

# start value for phi(n)
i = 1

# loop through prime factors and multiply them together with (factor-1)*(nextFactor-1)...
for a in x:
    i = i * (a-1)

# inverse pow (3.8+ syntax, for previous versions of python use gmpy2.invert)
d = pow(e, -1, i)

# solve for the answer
ans = pow(ct, d, n)

# print the answer
print(bytes.fromhex(hex(ans)[2:]).decode('ascii'))
