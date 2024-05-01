import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askopenfilename
import os
import src.huffman as hf
import pickle
# Ventana
window = tk.Tk()


ABS_PATH = os.getcwd()

i_f = "input.txt"
o_f = "output.bin"


def ventana_bienvenida():
    for widget in window.winfo_children():
        widget.destroy()  # Esta funcion borra el contenido del widget
    ventana()
    ttk.Label(window, text="Bienvenido a la Actividad 07 - AGC").place(x=525, y=50)  # Etiqueta pricipal mensaje
    ttk.Label(window, text="Selecciona Un Archivo").place(x=557, y=100)  # mensaje de seleccionar archivo


def Abrir_Archivo():  # Función Seleccionar archivo
    filepath = askopenfilename(initialdir="/", title="Seleccion de Archivo", filetypes=(("Text files", "*.txt"), ("Todos los Archivos", "*.*")))  # Abre el explorador de archivos, filtrando solo archivos txt   
    return filepath  # Retorna el archivo seleccionado


def Abrir_BIN():
    filepath = askopenfilename(initialdir="/", title="Seleccion de Archivo", filetypes=(("Binary files", "*.bin"), ("Todos los Archivos", ".")))
    return filepath


def huff_txt():
    for widget in window.winfo_children():
        widget.destroy()
    ventana()
    filepath = Abrir_Archivo()
    filename = os.path.basename(filepath)
    archivos = ttk.Label(window, text="Seleccione Archivo:")

    archivos.place(x=555, y=50)
    archivos.configure(text="Archivo abierto: \n\n"+filename)
    
    freq_list = hf.generate_dict(filename)
    freq_list = sorted(freq_list.items(), key=lambda x: x[1], reverse=True)

    nodes = freq_list

    while len(nodes) > 1:
        (key1, c1) = nodes[-1]
        (key2, c2) = nodes[-2]
        nodes = nodes[:-2]
        
        node = hf.NodeTree(key1, key2)
        nodes.append((node, c1 + c2))

        nodes = sorted(nodes, key=lambda x: x[1], reverse=True)

    huffman_code = hf.huffman_code_tree(nodes[0][0])

    output = tk.Text(window)
    output.pack(expand=True, fill="x")
    
    output.insert(tk.END, ' Char | Huffman Code')
    output.insert(tk.END, '--------------------')
    for (char, frequency) in freq_list:
        output.insert(tk.END, ' %-4r |%12s' % (char, huffman_code[char]))
    output.see()

def compress_txt():
    for widget in window.winfo_children():
        widget.destroy()  # Esta funcion borra el contenido del widget
    ventana()
    filepath = Abrir_Archivo()  # Llama a la función Abrir_Archivo
    filename = os.path.basename(filepath)  # Obtiene el nombre del archivo seleccionado
    archivos = ttk.Label(window, text="Seleccione Archivo:")  # Etiqueta de seleccionar archivo
    archivos.place(x=555, y=50)  # posicion de la etiqueta archivo
    archivos.configure(text="Archivo comprimido: \n\n"+filename)  # realiza la apertura del explorador de archivos y lo limita a los tipos .xlsx y csv

    input_f = open(ABS_PATH+"//"+filename, "rb").read()
    output_f = open(ABS_PATH+"//"+o_f, "wb")
    
    compressed_file = hf.compress(input_f)
    pickle.dump(compressed_file, output_f)

    # Crea un widget de texto
    output = tk.Text(window)
    output.pack(expand=True, fill="x")
    # Se inserta el texto en el widget de texto
    output.insert(tk.END, f'Compressed file in {o_f}')  # Imprime el resultado en el widget de texto
    output.see()  # Muestra el resultado en el widget de texto


def decompress_bin():
    for widget in window.winfo_children():
        widget.destroy()  # Esta funcion borra el contenido del widget
    ventana()
    filepath = Abrir_BIN()  # Llama a la función Abrir_Archivo
    filename = os.path.basename(filepath)  # Obtiene el nombre del archivo seleccionado
    archivos = ttk.Label(window, text="Seleccione Archivo:")  # Etiqueta de seleccionar archivo
    archivos.place(x=555, y=50)  # posicion de la etiqueta archivo
    archivos.configure(text="Archivo descomprimido: \n\n"+filename)  # realiza la apertura del explorador de archivos y lo limita a los tipos .xlsx y csv

    input_f = pickle.load(open(ABS_PATH+"//"+filename, "rb"))
    output_f = open(ABS_PATH+"//"+i_f, "w")

    uncompressed_file = hf.decompress(input_f)

    for l in uncompressed_file:
        output_f.write()
    output_f.close()
    
        # Crea un widget de texto
    output = tk.Text(window)
    output.pack(expand=True, fill="x")
    # Se inserta el texto en el widget de texto
    output.insert(tk.END, f'Decompressed file in {i_f}')  # Imprime el resultado en el widget de texto
    output.see()  # Muestra el resultado en el widget de texto




def ventana():
    for widget in window.winfo_children():
        widget.destroy()  # Esta funcion borra el contenido del widget

    button_frame = tk.Frame(window)
    button_frame.pack(side=tk.BOTTOM, padx=10, pady=10)
    # Boton Examinar
    examinar_button = tk.Button(button_frame, text="Examinar", command=huff_txt)
    examinar_button.pack(side=tk.RIGHT, padx=5)
    # Boton Comprimir
    comprimir_button = tk.Button(button_frame, text="Comprimir", command=compress_txt)
    comprimir_button.pack(side=tk.RIGHT, padx=5)
    # Boton Descomprimir
    descomprimir_button = tk.Button(button_frame, text="Descomprimir", command=decompress_bin)
    descomprimir_button.pack(side=tk.RIGHT, padx=5)

window.title("Actividad 07 - AGC")  # Titulo en la ventana 
window.geometry("1200x700")  # Tamaño de la ventana
ventana_bienvenida()
window.mainloop()  # Mainloop para correr ventana
