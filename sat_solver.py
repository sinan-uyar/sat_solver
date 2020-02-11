#bearbeitet von Amirhossein Rajabi Pour Kiakolaie und Sinan Uyar
'''
form der eingabe: liste aus listen mit der gleichen eingabeform wie aus der aufgabenstellung
beispiel dafuer unten bzw. auch bei dem ausfuehren.

die knf muss in sat eingegeben werden, um die berechnung zu starten.
es wird davon ausgegangen, dass die terme von 1 anfangend bis zum hoechsten ohne luecken sind
'''

#es wird nicht auf laufzeit geachtet 
import copy
g=[]

def sat(l):
    global g
    newmax=0
    for i in l:
        for k in i:
            if newmax < abs(k):
                newmax=abs(k)
    g=[0 for p in range(newmax)]
    h=[(i+1) for i in range(newmax)]
    if solver(l,newmax):
        print("\neine gueltige belegung waere:\n",h,"=",g)
        return
    else:
        g=[]
        return("eingabe ist unloesbar")

def solver(l,m):
    print(l,m)
    global g
    z1=copy.deepcopy(l) #als backup, falls falsche wahlen getroffen wurden
    z2=copy.deepcopy(l)
    if m<1:
        return True
    if clean(z1,m,True):    #im prinzip werden nur die 2 regeln aus der aufgabenstellung angewendet
        g[m-1]=True    
        if solver(z1,m-1):  #rekursives backtracking
            return True
    
    if clean(z2,m,False):
        g[m-1]=False
        return solver(z2,m-1)
        
    return False

def clean(z,m,b):
    print("\nin: ",m,"mit: ",b)
    hilf=[]
    for i in z:
        if m in i:
            if b==True:
                print(z,m,i)
                hilf+=[i]   #wird abgespeichert und spaeter entfernt, da es sonst zu problemen fuehrt
                print(z)
            else:
                print(z,m,i)
                if i not in hilf:
                    i.remove(m)
                    print(z)
                    if i==[]:
                        return False
                
        elif (-m) in i:
            if b==False:
                print(z,-m,i)
                hilf+=[i]
                print(z)
            else:
                print(z,-m,i)
                if i not in hilf:
                    i.remove(-m)
                    print(z)
                    if i==[]:
                        return False
    print("")
    print("geloescht wird: ",hilf)
    print("in: ",z)
    print("")
    for s in hilf:
        z.remove(s)
    return True
        
f=[[1,2,3],[1,-2],[-1,-2,3],[-3]]
sat(f)
