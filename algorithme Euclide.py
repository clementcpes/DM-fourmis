def f(a,b):
    if b==0 : return a
    else : return f(b,a%b)
print(f(4513598,1342))
for i in range(10):
    print(i)
