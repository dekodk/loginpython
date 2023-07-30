import customtkinter
import pymysql.cursors
import tkinter.messagebox as messagebox
import subprocess
import sys

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

conexao = pymysql.connect(
    host='localhost',
    user='root',
    password='025507',
    database='python',
    cursorclass=pymysql.cursors.DictCursor
)

# Função para verificar o login
def verificar_login():
    usuario = email.get()
    senha_informada = senha.get()

    try:
        # Verificar o usuário no banco de dados
        with conexao.cursor() as cursor:
            cursor.execute('SELECT * FROM user WHERE usuario=%s AND senha=%s', (usuario, senha_informada))
            resultado = cursor.fetchone()

        if resultado:
            print("Login bem-sucedido!")
            # Aqui você pode implementar a lógica para abrir a próxima janela ou executar a ação de login bem-sucedido
            abrir_menu_py()
            #janela.destroy()  # Fechar a janela de login após o login bem-sucedido
        else:
            messagebox.showerror("Erro de login", "Usuário/senha incorretos. Tente novamente.")

    except pymysql.Error as err:
        print(f"Erro ao verificar o login: {err}")

# Função para iniciar o arquivo menu.py
def abrir_menu_py():
    subprocess.run([sys.executable, "menu.py"])
    janela.destroy() if janela.winfo_exists() else None  # Fechar a janela de login se ainda existir

janela = customtkinter.CTk()
janela.title("Login")
janela.geometry("500x400")

texto1 = customtkinter.CTkLabel(janela, text="BrinKantes e Molekes System", font=("", 22))
texto1.pack(padx=10, pady=10)

texto2 = customtkinter.CTkLabel(janela, text="Fazer Login!")
texto2.pack(padx=10, pady=10)

email = customtkinter.CTkEntry(janela, placeholder_text="Seu usuário")
email.pack(padx=10, pady=10)

senha = customtkinter.CTkEntry(janela, placeholder_text="Sua senha", show="*")
senha.pack(padx=10, pady=10)

botao = customtkinter.CTkButton(janela, text="Login", command=verificar_login)
botao.pack(padx=10, pady=10)

janela.mainloop()
