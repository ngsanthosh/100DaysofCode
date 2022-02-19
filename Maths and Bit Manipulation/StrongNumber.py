# https://takeuforward.org/data-structure/check-if-a-number-is-a-strong-number-or-not/

# n=int(input())

def fact(n):
    if(n==0):
        return 1
    
    return (n * fact(n-1))
            
    
    
# print(fact(n))

t=int(input("Enter the strong or not number"))
check=t
sum=0
while t!=0:
    getit=t%10
    sum+=fact(getit)
    t=t//10
# print(t)
# print(sum)
print(check==sum)