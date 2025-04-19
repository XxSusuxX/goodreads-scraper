import tkinter as tk
from tkinter import messagebox
import subprocess
import os
import webbrowser
from PIL import Image, ImageTk
import logging

logging.basicConfig(filename="app.log", level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def iniciar_scrapy():
    try:
        logging.info("Iniciando o Scrapy...")
        max_pages = int(entry_pages.get())
        if max_pages < 1 or max_pages > 100:
            raise ValueError("O número de páginas deve estar entre 1 e 100.")
        
        file_name = entry_file_name.get().strip()
        if not file_name:
            raise ValueError("O nome do arquivo não pode estar vazio.")
        
        file_format = format_var.get()
        if file_format not in ["json", "csv"]:
            raise ValueError("Formato de arquivo inválido.")

        # Caminho completo do arquivo gerado
        output_file = os.path.join(os.getcwd(), f"{file_name}.{file_format}")

        # Executar o spider com os argumentos
        subprocess.run(['scrapy', 'crawl', 'goodreads', '-a', f'max_pages={max_pages}', '-o', output_file], check=True)

        # Mensagem de sucesso
        messagebox.showinfo("Concluído", f"Arquivo gerado com sucesso!\nCaminho: {output_file}")
        logging.info(f"Arquivo gerado com sucesso: {output_file}")
    except ValueError as e:
        messagebox.showerror("Erro", str(e))
    except subprocess.CalledProcessError:
        messagebox.showerror("Erro", "Ocorreu um erro ao executar o Scrapy.")
    except Exception as e:
        logging.error(f"Erro ao executar o Scrapy: {e}")
        messagebox.showerror("Erro", f"Erro inesperado: {e}")
        raise

def abrir_portfolio():
    webbrowser.open("https://www.gabrielsuenaga.com.br")

def validar_numero(text):
    return text.isdigit() and 1 <= int(text) <= 100

# Funções para hover nos botões
def on_enter(e):
    if e.widget == start_button:
        e.widget.config(bg="#007A78", fg="#FFFFFF")  # Cor específica para o botão "Iniciar"
    else:
        e.widget.config(bg="#5865F2", fg="#FFFFFF")  # Cor padrão para outros botões

def on_leave(e):
    if e.widget == start_button:
        e.widget.config(bg="#43B581", fg="#FFFFFF")  # Cor original do botão "Iniciar"
    else:
        e.widget.config(bg="#7289DA", fg="#FFFFFF")  # Cor original para outros botões

# Configuração da interface
root = tk.Tk()
root.title("Goodreads Scraper")
root.geometry("600x500")
root.configure(bg="#2C2F33")

# Adicionar o ícone
icon_path = os.path.join(os.path.dirname(__file__), "assets", "icon.ico")
if os.path.exists(icon_path):
    img = Image.open(icon_path)
    icon = ImageTk.PhotoImage(img)
    root.iconphoto(True, icon)
else:
    print(f"Ícone não encontrado: {icon_path}")

# Título
title_label = tk.Label(root, text="Goodreads Scraper", font=("Helvetica", 20, "bold"), bg="#2C2F33", fg="#FFFFFF")
title_label.pack(pady=20)

# Instrução para o número de páginas
instruction_label_pages = tk.Label(root, text="Número de páginas (1-100):", font=("Helvetica", 12), bg="#2C2F33", fg="#FFFFFF")
instruction_label_pages.pack(pady=5)

# Campo de entrada para o número de páginas com validação
validate_command = root.register(validar_numero)
entry_pages = tk.Entry(root, font=("Helvetica", 12), justify="center", width=10, validate="key", validatecommand=(validate_command, "%P"))
entry_pages.pack(pady=5)

# Instrução para o nome do arquivo
instruction_label_file_name = tk.Label(root, text="Nome do arquivo (sem extensão):", font=("Helvetica", 12), bg="#2C2F33", fg="#FFFFFF")
instruction_label_file_name.pack(pady=5)
entry_file_name = tk.Entry(root, font=("Helvetica", 12), justify="center", width=20)
entry_file_name.pack(pady=5)

# Opções de formato do arquivo
instruction_label_format = tk.Label(root, text="Formato do arquivo:", font=("Helvetica", 12), bg="#2C2F33", fg="#FFFFFF")
instruction_label_format.pack(pady=5)
format_var = tk.StringVar(value="json")
format_dropdown = tk.OptionMenu(root, format_var, "json", "csv")
format_dropdown.config(font=("Helvetica", 12), bg="#7289DA", fg="#FFFFFF", activebackground="#99AAB5", relief="flat")
format_dropdown.pack(pady=5)

# Botão para iniciar
start_button = tk.Button(root, text="Iniciar", font=("Helvetica", 14, "bold"), bg="#43B581", fg="#FFFFFF", relief="flat", borderwidth=0, command=iniciar_scrapy)
start_button.pack(pady=30)

# Adicionar hover ao botão de iniciar
start_button.bind("<Enter>", on_enter)
start_button.bind("<Leave>", on_leave)

# Botão para o portfólio no canto inferior esquerdo
portfolio_button = tk.Button(root, text="Visite meu portfólio", font=("Helvetica", 10, "bold"), bg="#7289DA", fg="#FFFFFF", relief="flat", borderwidth=0, command=abrir_portfolio)
portfolio_button.place(x=10, y=460)

# Adicionar hover ao botão do portfólio
portfolio_button.bind("<Enter>", on_enter)
portfolio_button.bind("<Leave>", on_leave)

# Rodapé
footer_label = tk.Label(root, text="Desenvolvido por Gabriel Suenaga", font=("Helvetica", 10), bg="#2C2F33", fg="#99AAB5")
footer_label.pack(side="bottom", pady=10)

root.mainloop()