import operation
import history
print("Два нуля (00) в качестве знака операции завершит работу программы")

while True:
    x = input("x=")
    if x == '00': break
    elif x =='h':
        history.h(x)
        break
    x= float(x)    
    s = input("Знак (+,-,*,/,** )")
    y = float(input("y="))
   
    if s == '+':
        z= operation.plus(x,y)
        print(z)            
    elif s == '-':
        z=operation.minus(x,y)
        print(z)
    elif s == '*':
        z=operation.multy(x,y)
        print(z)
    elif s == '/' and y != 0:
        z=operation.div(x,y)
        print(z)
    elif s == '/' and y == 0:
        print("На ноль делить нельзя!")            
    elif s ==  "**":
       z=operation.expon(x,y)
       print(z)
    else:        
        print("Неверный знак операции!")
     
    history.listadd(x,y,s,z)    