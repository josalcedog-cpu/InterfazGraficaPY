import tkinter as tk 

#https://github.com/NBOLIVARTELECO/Tkinter-Views-Basic.git
def crear_ventana():
    
    ventana = tk.Tk()
    ventana.geometry("500x500")# está en pixeles

    
    etiq = tk.Label(ventana, text = "HOLA MUNDO!!!")
    etiq.pack(pady=19)

    boton = tk.Button(ventana, text="Cerrar", command=ventana.destroy)
    boton.pack(pady = 15)

    
    etiq1 = tk.Label(ventana, text = "INGERESE SU NOMBRE: ")
    etiq1.pack(pady=11)

    camp = tk.Entry(ventana)
    camp.insert(0,"") 
    camp.pack(pady = 20)
    
    
           
    
    boton1 = tk.Button(ventana, text="Boton", command= lambda: vertext(camp.get()))
    boton1.pack(pady = 9)
    ventana.mainloop()
    return camp
        


def vertext(texto):      
        print(texto)
        

def main():
    crear_ventana()

if  __name__ == "__main__": 
    main()

#Que cada vez que se de al boton muestre el nombre en consola
#Cada vez que le de al boton y aparezca en consola cambie etiq por lo que escribio en camp 
    