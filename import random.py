import random
import tkinter as tk
from tkinter import messagebox

# Lista de palavras relacionadas à biologia
palavras_biologia = ["elefante", "girafa", "leopardo", "camarão", "borboleta", "peixe", "pinguim", "esquilo"]

# Função para iniciar o jogo
def iniciar_jogo():
    global palavra_aleatoria, tentativas, letras_digitadas, acertos
    palavra_aleatoria = random.choice(palavras_biologia)
    tentativas = 6
    letras_digitadas = []
    acertos = 0
    atualizar_interface()

# Função para verificar a letra inserida
def verificar_letra():
    global tentativas, acertos
    letra = letra_entry.get().lower()

    if letra in letras_digitadas:
        messagebox.showinfo("Aviso", "Você já digitou essa letra. Tente novamente.")
    else:
        letras_digitadas.append(letra)
        if letra in palavra_aleatoria:
            acertos += palavra_aleatoria.count(letra)
        else:
            tentativas -= 1

    letra_entry.delete(0, tk.END)
    atualizar_interface()

# Função para atualizar a interface gráfica
def atualizar_interface():
    palavra_oculta = ""
    for letra in palavra_aleatoria:
        if letra in letras_digitadas:
            palavra_oculta += letra
        else:
            palavra_oculta += "_ "
    
    palavra_label.config(text=palavra_oculta)
    tentativas_label.config(text=f"Tentativas Restantes: {tentativas}")
    
    if palavra_oculta == palavra_aleatoria:
        messagebox.showinfo("Parabéns!", f"Você adivinhou a palavra corretamente: '{palavra_aleatoria}'")
        iniciar_jogo()
    elif tentativas == 0:
        messagebox.showinfo("Fim de Jogo", f"A palavra correta era '{palavra_aleatoria}'")
        iniciar_jogo()

# Configuração da janela
janela = tk.Tk()
janela.title("Adivinhe a Palavra (Biologia)")
janela.geometry("400x300")
janela.configure(bg="#000080")  # Cor de fundo azul escuro

# Elementos da interface
titulo_label = tk.Label(janela, text="Adivinhe a Palavra (Biologia)", font=("Helvetica", 18), bg="#000080", fg="white")
palavra_label = tk.Label(janela, text="", font=("Arial", 24), bg="#000080", fg="white")
tentativas_label = tk.Label(janela, text="", font=("Arial", 16), bg="#000080", fg="white")
letra_entry = tk.Entry(janela, font=("Arial", 16))
verificar_button = tk.Button(janela, text="Verificar", command=verificar_letra, font=("Arial", 16))
iniciar_button = tk.Button(janela, text="Iniciar Jogo", command=iniciar_jogo, font=("Arial", 16))

titulo_label.pack(pady=10)
palavra_label.pack(pady=20)
tentativas_label.pack()
letra_entry.pack()
verificar_button.pack()
iniciar_button.pack(pady=10)

# Inicie o jogo
iniciar_jogo()

janela.mainloop() 