import random
import string
import tkinter as tk

class GeneradorUI:  #Clase necesaria para ejecutar la interfaz
    def __init__(self, root):
        self.root = root
        self.root.title("Generador de Contraseñas") #Titulo de la pagina

        self.label = tk.Label(root, text="Contraseña generada: ") #Cuadro de texto para imprimir
        self.label.pack()

        self.password_var = tk.StringVar()
        self.password_entry = tk.Entry(root, textvariable=self.password_var, show="") #Muestra la contraseña
        self.password_entry.pack()

        self.generate_button = tk.Button(root, text="Generar Contraseña", command=self.generar) #Boton para generar y llamado a la funcion
        self.generate_button.pack()

    def generar(self, longitud=12, incluir_mayusculas=True, incluir_numeros=True, incluir_simbolos=True): #Funcion para  generar contraseña

        """Genera una contraseña segura según los parámetros especificados."""
        caracteres = string.ascii_letters  # Letras minúsculas y mayúsculas
        caracteres += string.digits  # Números
        caracteres += string.punctuation  # Símbolos especiales
        contraseña = ''.join(random.choice(caracteres) for _ in range(longitud))
        self.password_var.set(contraseña)
if __name__ == "__main__": #Contiene la llamada a la aplicacion
    root = tk.Tk()
    app = GeneradorUI(root)
    root.mainloop()