def base(number, base):
    if number == 0:
        return '0'
    else:
        result = ''
        while number != 0:
            remainder = number % base
            if remainder < 10:
                result = str(remainder) + result
            else:
                result = chr(remainder + 55) + result
            number //= base
        return result
nbre = str(input("nombre :"))
while True :
    try :
        puissance = int(input("puissance :"))
        puissance_souhaitee = int(input("puissance souhaitée :"))
        break
    except ValueError:
        print("invalid syntax")
b=1
rang = 0
base_10 = 0
for i in range (0,len(nbre)) : 
    
    c = nbre[-b]
    c= str(c)
    b = b+1
    if  c.isdigit()==True :
        c = int(c)
    else :
        c = ord(c) - 55
    d = c*(puissance**rang)
    rang = rang+1
    base_10 = base_10 + d
    
print(base(base_10,puissance_souhaitee))