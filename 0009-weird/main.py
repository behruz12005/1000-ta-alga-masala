# agar n juft bo‘lsa → n = n / 2

# agar n toq bo‘lsa → n = n * 3 + 1

# bu jarayon n = 1 bo‘lguncha davom etadi

# har bir bosqichdagi n ni chiqarib borasan


def weird(n):
    step = 0
    if n <= 1:
        return 1
    
    while n != 1:
        if n % 2 == 0:
            n = n /2
        else:
            n = n * 3 +1
        print(n,end='\n')
        step +=1
    return step


print(weird(3))