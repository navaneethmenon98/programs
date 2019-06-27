comp=[]
while(True):
    z = int(input("enter 1:add employee \n2:show all \n3:show by id \n4:update by id \n5:delete by id \n"))
   
    if(z==1):
        s = int(input("enter no. of employees"))
       
        for i in range(s):
            elm=[]
            elm.append(input("enter id"))
            elm.append(input("enter name"))
            elm.append(input("enter designation"))
            elm.append(input("enter doj"))
            comp.append(elm)
            
    elif(z==2):
            print(comp,"\n")
            
    elif(z==3):
        a = (input("enter id"))
        for i in range(len(comp)):
            if(comp[i][0]==a):
                print(comp[i])
                
                
    elif(z==4):    
        b = (input("enter id"))
        for i in range(len(comp)):
            if(comp[i][0]==b):
                comp[i][1] = input("enter name")
                comp[i][2] = input("enter designation")
                comp[i][3] = input("enter doj")
        
        
    elif(z==5):
        c = (input("enter id"))
        for i in range(len(comp)):
            if(comp[i][0]==c):
                    del(comp[i])
    else:
        break
