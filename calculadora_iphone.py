import customtkinter as ctk


root = ctk.CTk()#<========= a janela
root.geometry('310x460')
root.maxsize(310,460)
root.minsize(310,460)
root.config(background='black')
root.title('Iphone')



e = ctk.CTkEntry(root,
                fg_color='black',
                bg_color='black',
                width=420,
                height=100, 
                text_color='white',
                border_color='black',
                font=('San Francisco', 32, 'bold'),
                )#<======= *O painel onde os numeros apareceram*

e.place(x=180, y=40)
#onde ficaram as funçoes


numero = ''
adicao = False
subtraçao = False
vezes = False
divisao = False

def botao(num):#<======== adicina o  numero a variavel "e", deste modo aparecendo no painel
    e.insert(2, num)

def mais():
    global numero
    global adicao
    numero = e.get()
    adicao = True
    e.delete(0, 1000000)
    
def menos():
    global numero
    global subtraçao
    numero = e.get()
    subtraçao = True
    e.delete(0, 1000000)

def vezes():
    global numero
    global vezes
    numero = e.get()
    vezes = True
    e.delete(0, 100000000)

def divisao():
    global numero
    global divisao
    numero = e.get()
    divisao = True
    e.delete(0, 10000000)

def delall():
    e.delete(0, 10000000)


def igual():
    global adicao
    global subtraçao
    global vezes
    global divisao
    numero2 = e.get()
    e.delete(0, 100000000)
    if adicao == True:
        e.insert(0, int(numero) + int(numero2))
        adicao = False
    if subtraçao == True:
        e.insert(0, int(numero) - int(numero2))
        subtraçao = False
    if vezes == True:
        e.insert(0, int(numero) * int(numero2))
        vezes = False
    if divisao == True:
        e.insert(0, int(numero) / int(numero2))    
#numeros e sinais



numero_0 = ctk.CTkButton(root, 
                         fg_color='gray',
                         bg_color='black',
                         text='0',
                         command=lambda: botao(0),
                         corner_radius=100, 
                         width=130,
                         height=50,
                         border_spacing=0,
                         border_width=0,
                         font=('circular', 22, 'bold' ))
numero_0.place(x=20, y= 400)

numero_flt = ctk.CTkButton(root, 
                         fg_color='gray',
                         bg_color='black',
                         text='.',
                         command=lambda: botao('.'),
                         corner_radius=100, 
                         width=40,
                         height=50,
                         border_spacing=0,
                         border_width=0,
                         font=('circular', 22, 'bold' ))
numero_flt.place(x=160, y= 400)

numero_1 = ctk.CTkButton(root, 
                         fg_color='gray',
                         bg_color='black',
                         text='1',
                         command=lambda: botao(1),
                         corner_radius=100, 
                         width=40,
                         height=50,
                         border_spacing=0,
                         border_width=0,
                         font=('circular', 22, 'bold' ))
numero_1.place(x=20, y= 330)

numero_2 = ctk.CTkButton(root, 
                         fg_color='gray',
                         bg_color='black',
                         text='2',
                         command=lambda: botao(2),
                         corner_radius=100, 
                         width=40,
                         height=50,
                         border_spacing=0,
                         border_width=0,
                         font=('circular', 22, 'bold' ))
numero_2.place(x=90, y= 330)

numero_3 = ctk.CTkButton(root, 
                         fg_color='gray',
                         bg_color='black',
                         text='3',
                         command=lambda: botao(3),
                         corner_radius=100, 
                         width=40,
                         height=50,
                         border_spacing=0,
                         border_width=0,
                         font=('circular', 22, 'bold' ))
numero_3.place(x=160, y= 330)

numero_4 = ctk.CTkButton(root, 
                         fg_color='gray',
                         bg_color='black',
                         text='4',
                         command=lambda: botao(4),
                         corner_radius=100, 
                         width=40,
                         height=50,
                         border_spacing=0,
                         border_width=0,
                         font=('circular', 22, 'bold' ))
numero_4.place(x=20, y= 270)

numero_5 = ctk.CTkButton(root, 
                         fg_color='gray',
                         bg_color='black',
                         text='5',
                         command=lambda: botao(5),
                         corner_radius=100, 
                         width=40,
                         height=50,
                         border_spacing=0,
                         border_width=0,
                         font=('circular', 22, 'bold' ))
numero_5.place(x=90, y= 270)

numero_6 = ctk.CTkButton(root, 
                         fg_color='gray',
                         bg_color='black',
                         text='6',
                         command=lambda: botao(6),
                         corner_radius=100, 
                         width=40,
                         height=50,
                         border_spacing=0,
                         border_width=0,
                         font=('circular', 22, 'bold' ))
numero_6.place(x=160, y= 270)

numero_7 = ctk.CTkButton(root, 
                         fg_color='gray',
                         bg_color='black',
                         text='7',
                         command=lambda: botao(7),
                         corner_radius=100, 
                         width=40,
                         height=50,
                         border_spacing=0,
                         border_width=0,
                         font=('circular', 22, 'bold' ))
numero_7.place(x=20, y= 210)

numero_8 = ctk.CTkButton(root, 
                         fg_color='gray',
                         bg_color='black',
                         text='8',
                         command=lambda: botao(8),
                         corner_radius=100, 
                         width=40,
                         height=50,
                         border_spacing=0,
                         border_width=0,
                         font=('circular', 22, 'bold' ))
numero_8.place(x=90, y= 210)

numero_9 = ctk.CTkButton(root, 
                         fg_color='gray',
                         bg_color='black',
                         text='9',
                         command=lambda: botao(9),
                         corner_radius=100, 
                         width=40,
                         height=50,
                         border_spacing=0,
                         border_width=0,
                         font=('circular', 22, 'bold' ))
numero_9.place(x=160, y= 210)



botao_de_menos_mais = ctk.CTkButton(root, 
                         fg_color='orange',
                         bg_color='black',
                         text='+/-',
                         command=delall,
                         corner_radius=100, 
                         width=10,
                         height=50,
                         border_spacing=0,
                         border_width=0,
                         font=('circular', 18 ,))
botao_de_menos_mais.place(x=95, y= 150)

del_all = ctk.CTkButton(root, 
                         fg_color='orange',
                         bg_color='black',
                         text='AC',
                         command=delall,
                         corner_radius=100, 
                         width=10,
                         height=50,
                         border_spacing=0,
                         border_width=0,
                         font=('circular', 18 ,))
del_all.place(x=15, y= 150)

teste_divisao = ctk.CTkButton(root, 
                         fg_color='orange',
                         bg_color='black',
                         text='/',
                         command=divisao,
                         corner_radius=100, 
                         width=130,
                         height=50,
                         border_spacing=0,
                         border_width=0,
                         font=('circular', 22, 'bold' ))
teste_divisao.place(x=175, y= 150)

teste_vezes = ctk.CTkButton(root, 
                         fg_color='orange',
                         bg_color='black',
                         text='x',
                         command=vezes,
                         corner_radius=100, 
                         width=40,
                         height=50,
                         border_spacing=0,
                         border_width=0,
                         font=('circular', 22, 'bold' ))
teste_vezes.place(x=230, y= 210)

teste_menos = ctk.CTkButton(root, 
                         fg_color='orange',
                         bg_color='black',
                         text='-',
                         command=menos,
                         corner_radius=100, 
                         width=60,
                         height=50,
                         border_spacing=0,
                         border_width=0,
                         font=('circular', 22, 'bold' ))
teste_menos.place(x=230, y= 270)

teste_mais = ctk.CTkButton(root, 
                         fg_color='orange',
                         bg_color='black',
                         text='+',
                         command=mais,
                         corner_radius=100, 
                         width=40,
                         height=50,
                         border_spacing=0,
                         border_width=0,
                         font=('circular', 22, 'bold' ))
teste_mais.place(x=230, y= 330)

teste_igual = ctk.CTkButton(root, 
                         fg_color='orange',
                         bg_color='black',
                         text='=',
                         command=igual,
                         corner_radius=100, 
                         width=40,
                         height=50,
                         border_spacing=0,
                         border_width=0,
                         font=('circular', 22, 'bold' ))

teste_igual.place(x=230, y= 400)



root.mainloop()