s = int(input("enter no. of employees"))
comp=[]
elm=[]
for i in range(s):
    elm.append(input("enter id"))
    elm.append(input("enter name"))
    elm.append(input("enter designation"))
    elm.append(input("enter doj"))
    comp.append(elm)
    
print (comp[0][0])
