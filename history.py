
def h(x):    
    f = open('history.txt', 'r')
    for line in f:
        print(line , "\n") 
        
     
def listadd(x,y,s,z):
     f = open("history.txt", mode="a+") 
     lst = [x,s,y,z]
     lst.insert(3, '=')        
     result = "".join(str(lst))
     f.writelines(result)
     f.write("\n")
     f.close