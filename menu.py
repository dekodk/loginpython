import customtkinter
import customtkinter as ctk
import tkinter as tk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

# Função para lidar com a seleção das opções do menu
def menu_selecionado(opcao):
    if opcao == "Cadastrar":
        print("Opção Cadastrar selecionada.")
    elif opcao == "Buscar":
        print("Opção Buscar selecionada.")

# Função para exibir o menu de clientes
def exibir_menu_clientes(event):
    menu_clientes.post(event.x_root, event.y_root)

# Função para exibir o menu de usuários
def exibir_menu_usuarios(event):
    menu_usuarios.post(event.x_root, event.y_root)

# Função para exibir o menu de agendamentos
def exibir_menu_agendamento(event):
    menu_agendamentos.post(event.x_root, event.y_root)

# Criar janela principal
janela = ctk.CTk()
janela.title("Menu")
janela.geometry("500x400")

# Criar um menu de clientes
menu_clientes = tk.Menu(janela, tearoff=False)
menu_clientes.add_command(label="Cadastrar", activebackground="purple", font=(18), command=lambda: menu_selecionado("Cadastrar"))
menu_clientes.add_command(label="Buscar", activebackground="purple", font=(18), command=lambda: menu_selecionado("Buscar"))

# Criar um menu de usuários
menu_usuarios = tk.Menu(janela, tearoff=False)
menu_usuarios.add_command(label="Cadastrar", activebackground="purple", font=(18), command=lambda: menu_selecionado("Cadastrar"))
menu_usuarios.add_command(label="Buscar", activebackground="purple", font=(18), command=lambda: menu_selecionado("Buscar"))

# Criar um menu de agendamento
menu_agendamentos = tk.Menu(janela, tearoff=False)
menu_agendamentos.add_command(label="Cadastrar", activebackground="purple", font=(18), command=lambda: menu_selecionado("Cadastrar"))
menu_agendamentos.add_command(label="Buscar", activebackground="purple", font=(18), command=lambda: menu_selecionado("Buscar"))

#Criar botões customizados para exibir os menus
botao_clientes = tk.Button(janela, text="Clientes", font=(22))
botao_clientes.grid(row=0, column=0, pady=10, padx=10)
botao_clientes.bind("<Button-1>", exibir_menu_clientes)

botao_usuarios = tk.Button(janela, text="Usuários", font=(22))
botao_usuarios.grid(row=0, column=2, pady=10, padx=10,)
botao_usuarios.bind("<Button-1>", exibir_menu_usuarios)

botao_agendamentos = tk.Button(janela, text="Agendamentos", font=(22))
botao_agendamentos.grid(row=0, column=3, pady=10, padx=10,)
botao_agendamentos.bind("<Button-1>", exibir_menu_usuarios)

janela.mainloop()
