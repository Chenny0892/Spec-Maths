
def fibbo(n):  
    fib_seq = [1,1]


    for i in range(2,n):
        next = fib_seq[-1] +  fib_seq[-2]  
        fib_seq.append(next)  
    return fib_seq 

n = int(input("input a pos int"))

print(fibbo(n))  

