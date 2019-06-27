import pickle
try:
    f=open("employee.txt",'rb')
    comp=pickle.load(f)
    f.close()
except:
    comp=dict()
while(True):
    z = int(input("enter 1:add employee \n2:show all \n3:show by id \n4:update by id \n5:delete by id \n"))
   
    if(z==1):
        s = int(input("enter no. of employees"))
       
        for i in range(s):
            elm=[]
            id = input("enter id")
            elm.append(id)
            elm.append(input("enter name"))
            elm.append(input("enter designation"))
            elm.append(input("enter doj"))
            comp[id] = elm
            
    elif(z==2):
            for i in comp.values():
                print("\n\nID: ",i[0])
                print("\nName: ",i[1])
                print("\nDesignation: ",i[2])
                print("\nDOJ: ",i[3],"\n\n")
            
    elif(z==3):
        a = input("enter id")
        i = comp[a]
        print("\n\nID: ",i[0])
        print("\nName: ",i[1])
        print("\nDesignation: ",i[2])
        print("\nDOJ: ",i[3],"\n\n")
                
                
    elif(z==4):    
        b = input("enter id")
        elm=[]
        elm.append(b)
        elm.append(input("enter name"))
        elm.append(input("enter designation"))
        elm.append(input("enter doj"))
        comp[b]=elm
        
        
    elif(z==5):
        c = input("enter id")
        del(comp[c])
    
    else:
        try:
            outfile = open("employee.txt",'wb')
            pickle.dump(comp,outfile)
        finally:
            outfile.close()
        break
