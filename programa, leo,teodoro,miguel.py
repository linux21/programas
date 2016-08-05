edges={                 
       (1,'a'):2,
       (2,'a'):2,
       (2,'b'):3,
       (3,'b'):3,
       (3,'a'):4,
       (4,'a'):5}
aceptacion=[8]  
def fsmsim(string, current, edges, aceptacion):
    if string == "":
        return current in aceptacion
    else:
        letter= string[0] 
        if(current,letter)in edges: 
            destination=edges[(current,letter)]
            remaining_string=string[1:]
            return fsmsim(remaining_string,destination,edges,aceptacion)
        else:
            return False 
#hacemos una prueba
print(fsmsim("aaabbba",1,edges,aceptacion))