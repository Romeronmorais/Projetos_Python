from tkinter .ttk import *
from tkinter import *

class telaLogin:
    def __init__(self,tela):
        self.frame1=Frame(tela)
        self.frame1.pack()

        self.frame2=Frame(tela)
        self.frame2.pack()

        self.frame3=Frame(tela,pady=10)
        self.frame3.pack()

        self.frame4=Frame(tela,pady=10) #,pady=10
        self.frame4.pack()       

        tela.geometry('200x260')
        tela.title('Tela de Login')    

        Label(self.frame1,text='Tela login Python', fg='darkblue',              
        font=('Verdana','14','bold'), height=3).pack()
        fonte1=('Verdana','10','bold')
        Label(self.frame2,text='Nome: ',font=fonte1,width=8).pack(side=LEFT)

        self.nome = Entry(self.frame2,width=10,font=fonte1)
        self.nome.focus_force() # Para o foco começar neste campo
        self.nome.pack(side=LEFT)

        Label(self.frame3,text='Senha: ', font = fonte1 , width=8).pack(side=LEFT)
        self.senha = Entry(self.frame3,width=10,show='*',font=fonte1)
        self.senha.pack(side=LEFT)

        self.confere = Button(self.frame4, font = fonte1, text = 'Conferir',bg ='gray', command = self.conferir)        
        self.confere.pack(side=TOP, padx=0, pady=0)

        self.msg = Label(self.frame4,font=fonte1,height=3,text='AGUARDANDO...')
        self.msg.pack(side=LEFT, padx=0, pady=0)

    def conferir(self):        
        NOME = self.nome.get()
        SENHA = self.senha.get()

        if NOME == SENHA:
            self.msg['text']='ACESSO PERMITIDO'
            self.msg['fg']='darkgreen'
        else:
            self.msg['text']='ACESSO NEGADO'
            self.msg['fg']='red'
            self.nome.focus_force()

instancia=Tk()
telaLogin(instancia)
instancia.mainloop()