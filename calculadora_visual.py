import tkinter as tk


janela = tk.Tk()
janela.title("calculadora teste.")
janela.geometry("400x300")
janela.resizable(False, False)
entrada = tk.Entry(janela)


# ===============================
# grid() — parâmetros principais
# ===============================

# row -> linha da grade onde o widget será colocado
# Ex: row=0

# column -> coluna da grade onde o widget será colocado
# Ex: column=1

# rowspan -> quantas linhas o widget ocupa
# Ex: rowspan=2

# columnspan -> quantas colunas o widget ocupa
# Ex: columnspan=4


# ===============================
# espaçamentos
# ===============================

# padx -> espaço externo horizontal (margem)
# Ex: padx=10

# pady -> espaço externo vertical (margem)
# Ex: pady=5

# ipadx -> espaço interno horizontal (aumenta o widget)
# Ex: ipadx=10

# ipady -> espaço interno vertical (aumenta o widget)
# Ex: ipady=5

entrada.grid(
    row=100,
    column=100,
    columnspan=100,
    padx=100,
    pady=100,
    
)

#pady = altura
#padx = "distancia das bordas"





janela.mainloop()