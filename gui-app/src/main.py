import tkinter as tk
from tkinter import messagebox
from projet import initialisation, num, genererClef, crypter, decrypter, liste, clef

def on_generate_key():
    try:
        global clef
        message = entry_message.get()
        if not message:
            raise ValueError("Veuillez entrer un message avant de générer une clé.")
        normalized_message = initialisation(message)  # Normalise le message
        taille = len(normalized_message)
        clef.clear()  # Réinitialise la clé
        genererClef(liste, taille)
        messagebox.showinfo("Clé générée", f"Clé : {clef}")
    except Exception as e:
        messagebox.showerror("Erreur", str(e))

def on_encrypt():
    try:
        message = entry_message.get()
        if not message:
            raise ValueError("Veuillez entrer un message à crypter.")
        normalized_message = initialisation(message)  # Normalise le message
        crypt = num(normalized_message)
        encrypted_message = crypter(crypt, clef)
        label_result.config(text=f"Message crypté : {''.join(encrypted_message)}")
    except Exception as e:
        messagebox.showerror("Erreur", str(e))

def on_decrypt():
    try:
        encrypted_message = entry_message.get()
        if not encrypted_message:
            raise ValueError("Veuillez entrer un message crypté à décrypter.")
        decrypted_message = decrypter(encrypted_message, clef)  # Appelle la fonction corrigée
        label_result.config(text=f"Message décrypté : {decrypted_message}")
    except Exception as e:
        messagebox.showerror("Erreur", str(e))

# Configuration de la fenêtre principale
root = tk.Tk()
root.title("Cryptage et Décryptage")

# Widgets
tk.Label(root, text="Message :").grid(row=0, column=0, padx=10, pady=10)
entry_message = tk.Entry(root, width=50)
entry_message.grid(row=0, column=1, padx=10, pady=10)

btn_generate_key = tk.Button(root, text="Générer Clé", command=on_generate_key)
btn_generate_key.grid(row=1, column=0, padx=10, pady=10)

btn_encrypt = tk.Button(root, text="Crypter", command=on_encrypt)
btn_encrypt.grid(row=1, column=1, padx=10, pady=10)

btn_decrypt = tk.Button(root, text="Décrypter", command=on_decrypt)
btn_decrypt.grid(row=2, column=0, padx=10, pady=10)

label_result = tk.Label(root, text="Résultat :")
label_result.grid(row=2, column=1, padx=10, pady=10)

# Lancement de l'application
root.mainloop()