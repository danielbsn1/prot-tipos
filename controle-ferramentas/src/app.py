import tkinter as tk
from tkinter import messagebox
import sqlite3
from db import criar_banco
from qr_reader import ler_qr_code

criar_banco()

def inserir_ferramenta():
    conn = sqlite3.connect("ferramentas.db")
    cursor = conn.cursor()
    try:
        cursor.execute("""
            INSERT INTO ferramentas (nome, codigo, categoria, localizacao, responsavel, data_aquisicao, situacao)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (
            nome_entry.get(),
            codigo_entry.get(),
            categoria_entry.get(),
            localizacao_entry.get(),
            responsavel_entry.get(),
            data_entry.get(),
            situacao_entry.get()
        ))
        conn.commit()
        messagebox.showinfo("Sucesso", "Ferramenta cadastrada com sucesso!")
        limpar_campos()
    except sqlite3.IntegrityError:
        messagebox.showerror("Erro", "Código de patrimônio duplicado!")
    conn.close()

def ler_qr():
    codigo = ler_qr_code()
    if codigo:
        codigo_entry.delete(0, tk.END)
        codigo_entry.insert(0, codigo)
        buscar_ferramenta()  # Busca automaticamente após ler o QR

def limpar_campos():
    for entry in [nome_entry, codigo_entry, categoria_entry, localizacao_entry, responsavel_entry, data_entry, situacao_entry]:
        entry.delete(0, tk.END)

def mostrar_ferramentas():
    consulta = tk.Toplevel(root)
    consulta.title("Ferramentas cadastradas")
    lista = tk.Listbox(consulta, width=100)
    lista.pack(padx=10, pady=10)

    conn = sqlite3.connect("ferramentas.db")
    cursor = conn.cursor()
    cursor.execute("SELECT nome, codigo, responsavel, situacao FROM ferramentas")
    ferramentas = cursor.fetchall()
    conn.close()

    for f in ferramentas:
        lista.insert(tk.END, f"Nome: {f[0]} | Código: {f[1]} | Responsável: {f[2]} | Situação: {f[3]}")

def buscar_ferramenta():
    codigo = codigo_entry.get()
    if not codigo:
        messagebox.showwarning("Aviso", "Digite ou leia um código para buscar.")
        return

    conn = sqlite3.connect("ferramentas.db")
    cursor = conn.cursor()
    cursor.execute("SELECT nome, codigo, categoria, localizacao, responsavel, data_aquisicao, situacao FROM ferramentas WHERE codigo = ?", (codigo,))
    ferramenta = cursor.fetchone()
    conn.close()

    if ferramenta:
        # Preenche os campos com os dados encontrados
        nome_entry.delete(0, tk.END)
        nome_entry.insert(0, ferramenta[0])
        codigo_entry.delete(0, tk.END)
        codigo_entry.insert(0, ferramenta[1])
        categoria_entry.delete(0, tk.END)
        categoria_entry.insert(0, ferramenta[2])
        localizacao_entry.delete(0, tk.END)
        localizacao_entry.insert(0, ferramenta[3])
        responsavel_entry.delete(0, tk.END)
        responsavel_entry.insert(0, ferramenta[4])
        data_entry.delete(0, tk.END)
        data_entry.insert(0, ferramenta[5])
        situacao_entry.delete(0, tk.END)
        situacao_entry.insert(0, ferramenta[6])
    else:
        messagebox.showinfo("Não encontrado", "Ferramenta não encontrada para este código.")

root = tk.Tk()
root.title("Controle de Ferramentas")

labels = ["Nome", "Código", "Categoria", "Localização", "Responsável", "Data de Aquisição", "Situação"]
entries = []

for i, label_text in enumerate(labels):
    label = tk.Label(root, text=label_text)
    label.grid(row=i, column=0)
    entry = tk.Entry(root, width=40)
    entry.grid(row=i, column=1)
    entries.append(entry)

nome_entry, codigo_entry, categoria_entry, localizacao_entry, responsavel_entry, data_entry, situacao_entry = entries

tk.Button(root, text="Salvar", command=inserir_ferramenta).grid(row=7, column=0, columnspan=2, pady=10)
tk.Button(root, text="Ler QR Code", command=ler_qr).grid(row=8, column=0, columnspan=2, pady=10)
tk.Button(root, text="Consultar Ferramentas", command=mostrar_ferramentas).grid(row=9, column=0, columnspan=2, pady=10)
tk.Button(root, text="Buscar pelo Código", command=buscar_ferramenta).grid(row=10, column=0, columnspan=2, pady=10)

root.mainloop()