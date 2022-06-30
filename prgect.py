from tkinter import*
from tkinter.messagebox import *
from abc import ABC,abstractmethod
class personne(ABC):
    con=0
    def __init__(self,nom='',cin='',prenom='',adresse='',datenaiss=''):
        personne.con=personne.con+1
        self.num=personne.con
        self.nom=nom
        self.CIN=cin
        self.prenom=prenom
        self.adresse=adresse
        self.dateNaiss=datenaiss
    @abstractmethod
    def calculesala(self):
        pass
class commerciale(personne):
    def __init__(self, nom='', cin='', prenom='', adresse='', datenaiss='',prime=0,salare=0,chiffred=0):
        personne.__init__(self,nom,cin, prenom, adresse, datenaiss)
        self.prime=prime
        self.salare=salare
        self.chiffred=chiffred
    def pomuntveute(self):
        return (5/100)*self.chiffred
    def calculesala(self):
        self.prime= self.pomuntveute()
        return self.salare +self.prime
    def saisir(self,x,y,z):
        self.prime = x
        self.salare =y
        self.chiffred =z
    def afficher(self):
        af1 = "prime : {} | salare : {} DH| chiffred : {} ".format(self.prime, self.salare, self.chiffred)
        return af1
class new(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.crer()
        
        
        
    

    def crer(self):
        self.Login = StringVar()
        self.password = StringVar()
        self.message=StringVar()
        self.label1= Label(self,width="300", text="Please enter details below", bg="orange",fg="white")
        self.label1.pack()
        self.label2=Label(self, text="Login : ")
        self.label2.pack()
        self.entry=Entry(self, textvariable=self.Login)
        self.entry.pack()
        self.label3=Label(self, text="Password : ")
        self.label3.pack()
        self.entry1=Entry(self, textvariable=self.password ,show="*")
        self.entry1.pack()
        self.label4=Label(self, text="",textvariable=self.message)
        self.label4.pack()
       
liste=[]
class new2(Frame):
    def __init__(self):
         Frame.__init__(self)
         self.crer2()
         
         
    def ajouter(self):
       global liste
       Ar = commerciale()
       Ar.saisir(self.v1.get(),self.v2.get(),self.v3.get())
       liste.append(Ar)
       showinfo("Votre commerciale a bien été ajouté !")
    def afficherarticles(self):
       global liste
       self.Produits.delete("1.0", "end")
       for i in range(0, len(liste)):
           self.Produits.insert(END, liste[i].afficher() + "\n")




    def crer2(self):
        self.texteaa = StringVar()
        self.v1 = IntVar(value='')
        self.v2 = IntVar(value='')
        self.v3 = IntVar(value='')
        self.lab1=Label(self,text="Prime:")
        self.lab1.grid(row=2,column=0)
        self.entry1=Entry(self, textvariable=self.v1).grid(row=2,column=1)
        self.lab2=Label(self,text="Salaire:")
        self.lab2.grid(row=3,column=0)
        self.entry2=Entry(self, textvariable=self.v2).grid(row=3,column=1)
        self.lab3=Label(self,text="chiffre d'affare:")
        self.lab3.grid(row=4,column=0)
        self.entry3=Entry(self, textvariable=self.v3).grid(row=4,column=1)
        self.x=Button(self, text="ajouter", command=self.ajouter,relief=RAISED)
        self.x.bind("<Button>", self.ajouter)
        self.x.grid(row=5,column=1)
        self.Produits = Text(self, width=66, height=9)
        self.Produits.grid(row=7,column=3)
        self.btn2 = Button(self, text="Afficher les produits", command=self.afficherarticles)
        self.btn2.grid(row = 6, column = 1,)
#class new3(Frame):
 #   def __init__(self):
  #      Frame.__init__(self)
        
        







T=Tk()
F=new()
F.pack()
def login():
    #getting form data
        uname=F.Login.get()
        pwd=F.password.get()
    #applying empty validation
        if  uname=="oussama" and pwd=="123":
             showinfo("Login success")
           

             g=new2()
             g.pack()
             g.lift()
             F.destroy()
             button.destroy()
             g.focus_force
        else:
            showwarning("Wrong username or password!!!")
            F.Login.set('')
            F.password.set('')
button=Button(T, text="Login", width=10, height=1, bg="orange",command=login)
button.pack()
F.mainloop()