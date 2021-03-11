# Program for relational operators; works based on value stored in variable or ASCII value

a=10
b=20
print(f"{a}<{b} is {a<b}")
print(f"{a}>{b} is {a>b}")
print(f"{a}=={b} is {a==b}")
print(f"{a}<={b} is {a<=b}")
print(f"{a}>={b} is {a>=b}")
print(f"{a}!={b} is {a!=b} \n")

# a+2 < b-15 corresponds to (a+2)<(b-15) and not a+(2<b)-15.
# precedence of arithmetic operators over relational operators.
print(f"{a+2}<{b-15} is {a+2<b-15}")

a=10
b=10.00
print(f"{a}<{b} is {a<b}")
print(f"{a}>{b} is {a>b}")
print(f"{a}=={b} is {a==b}")
print(f"{a}<={b} is {a<=b}")
print(f"{a}>={b} is {a>=b}")
print(f"{a}!={b} is {a!=b} \n")

c="computer"
d="programming"
print(f"{c}<{d} is {c<d}")
print(f"{c}>{d} is {c>d}")
print(f"{c}=={d} is {c==d}")
print(f"{c}<={d} is {c<=d}")
print(f"{c}>={d} is {c>=d}")
print(f"{c}!={d} is {c!=d} \n")


c="computer"
d=" computer"
# non-printing characters like white space have ASCII values
print(f"{c}<{d} is {c<d}")
print(f"{c}>{d} is {c>d}")
print(f"{c}=={d} is {c==d}")
print(f"{c}<={d} is {c<=d}")
print(f"{c}>={d} is {c>=d}")
print(f"{c}!={d} is {c!=d}")
