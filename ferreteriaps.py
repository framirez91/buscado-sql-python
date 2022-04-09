from cProfile import label
from cgitb import text
from email.mime import application
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from turtle import back
from xml.dom.minidom import Element
import mysql.connector
from setuptools import Command

#Conexion sql
# conexion1=mysql.connector.connect(host="localhost", 
#    user="root", 
#    passwd="", 
#    database="escuela")
class App:
    
    def buscarRut(self):
        pass
    
    def buscarcodigo(self):
        pass


    def __init__(self,master):
        self.ventana = master
        self.DibujarLabel()
        self.DibujarEntry()
        self.DibujarBoton()
        self.DibujarLista()

    def DibujarLabel(self):
        
        self.lbl_title = Label(self.ventana, foreground="white", background="#314252",text="Bienvenido Sistema Busqueda SQL",font=(8)).place(x=200,y=10)   
   
    
       #buscar codigo 
        self.lbl_cod = Label(self.ventana, foreground="white", background="#314252",text="Buscar por Codigo :").place(x=60,y=80)   
       #buscar rut
        self.lbl_rut = Label(self.ventana, foreground="white", background="#314252",text="Buscar por Rut :").place(x=60,y=50)   
        
    

    def DibujarEntry(self):
        self.rut= StringVar()
        self.codigo= StringVar()
        self.txt_rut= Entry(self.ventana,font=('arial',12),textvariable=self.rut).place(x=170,y=80)
        self.txt_codigo= Entry(self.ventana,font=('arial',12),textvariable=self.codigo).place(x=170,y=50)

    def DibujarBoton(self):
        self.btn_buscarRut = Button(self.ventana,text='Buscar Rut',background="#0051C8",foreground="white",width=20,command=self.buscarRut ).place(x=380,y=50)
        self.btn_buscarcodigo = Button(self.ventana,text='Buscar Codigo Producto',background="#0051C8",foreground="white",width=20,command=self.buscarcodigo ).place(x=380,y=80)
        
    def DibujarLista(self):
        self.lista = ttk.Treeview(self.ventana, columns=(1,2,3,4,5,6,7),show='headings',height=8)
        #estilo
        estilo = ttk.Style()
        estilo.theme_use('clam')

        estilo.configure("Treeview.Heading", background="#0051C8", foreground="white", fieldbackground="white", fieldforeground="white")
        self.lista.heading(1, text="Codigo")
        self.lista.heading(2, text="Nombre")
        self.lista.heading(3, text="Rut")
        self.lista.heading(4, text="Fecha")
        self.lista.heading(5, text="Cod Producto")
        self.lista.heading(6, text="Producto")
        self.lista.heading(7, text="Cantidad")
        self.lista.column(1, width=100)
        self.lista.column(2, width=100)
        self.lista.column(3, width=100)
        self.lista.column(4, width=100)
        self.lista.column(5, width=100)
        self.lista.column(6, width=100)
        self.lista.column(7, width=100)
        self.lista.place(x=60,y=120)
      
      
      
    



root = Tk()
root.title("Consulta Venta y usuarios")
root.geometry("800x400")
root.config(background="#314252")
application = App(root)
root.mainloop()
