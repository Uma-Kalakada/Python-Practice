# Program for identity operators; is & is not , refer to same memory location or not

a=10
b=20
c=10

print(f"a={a} is b={b} is {a is b}")

print(f"a={a} is c={c} is {a is c}")

print(f"c={c} is b={b} is {c is b}")


#printing memory locations

print(f"a memory is {id(a)},\nb memory is {id(b)},\nc memory is {id(c)} \n")

b=b-10

print("after changing b value to b-10")
print(f"a={a} is b={b} is {a is b}")

print(f"a={a} is c={c} is {a is c}")

print(f"c={c} is b={b} is {c is b}")


#printing memory locations

print(f"a memory is {id(a)},\nb memory is {id(b)},\nc memory is {id(c)}")
