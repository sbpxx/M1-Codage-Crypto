import tkinter as tk
from tkinter import messagebox
from projet import initialisation, num, genererClef, crypter, decrypter, liste, clef
import tkinter.filedialog as fd

# Fonction pour générer une clé de cryptage
def on_generate_key():
    try:
        global clef, liste
        # Récupère le message à crypter depuis la zone de texte
        message = entry_message_encrypt.get("1.0", "end-1c")
        if not message:
            raise ValueError("Veuillez entrer un message avant de générer une clé.")
        # Normalise le message et calcule la taille nécessaire pour la clé
        normalized_message = initialisation(message)
        taille = len(normalized_message)
        # Réinitialise la clé et génère une nouvelle clé basée sur la pile de cartes actuelle
        clef.clear()
        liste = genererClef(liste, taille)
        # Affiche la clé générée dans l'interface
        formatted_key = ' '.join(map(str, clef))
        label_key.config(text=f"Clé de cryptage :\n{formatted_key}")
    except Exception as e:
        # Affiche une erreur en cas de problème
        messagebox.showerror("Erreur", str(e))

# Fonction pour crypter un message
def on_encrypt():
    try:
        # Récupère le message à crypter depuis la zone de texte
        message = entry_message_encrypt.get("1.0", "end-1c")
        if not message:
            raise ValueError("Veuillez entrer un message à crypter.")
        # Normalise le message et le convertit en une liste de nombres
        normalized_message = initialisation(message)
        crypt = num(normalized_message)
        # Crypte le message en utilisant la clé générée
        encrypted_message = crypter(crypt, clef)
        # Affiche le message crypté dans l'interface
        label_result.config(text=f"Message crypté : {''.join(encrypted_message)}")
        # Insère le message crypté dans la zone de texte pour le décryptage
        entry_message_decrypt.delete("1.0", "end")
        entry_message_decrypt.insert("1.0", ''.join(encrypted_message))
    except Exception as e:
        # Affiche une erreur en cas de problème
        messagebox.showerror("Erreur", str(e))

# Fonction pour décrypter un message
def on_decrypt():
    try:
        # Récupère le message crypté depuis la zone de texte
        encrypted_message = entry_message_decrypt.get("1.0", "end-1c").upper()
        if not encrypted_message:
            raise ValueError("Veuillez entrer un message crypté à décrypter.")
        # Décrypte le message en utilisant la clé générée
        decrypted_message = decrypter(encrypted_message, clef)
        # Affiche le message décrypté dans l'interface
        label_result_decrypted.config(text=f"Message décrypté : {decrypted_message}")
    except Exception as e:
        # Affiche une erreur en cas de problème
        messagebox.showerror("Erreur", str(e))

# Fonction pour charger un fichier texte et insérer son contenu dans la zone de texte
def on_select_file():
    try:
        # Ouvre une boîte de dialogue pour sélectionner un fichier texte
        file_path = fd.askopenfilename(filetypes=[("Fichiers texte", "*.txt")])
        if not file_path:
            return
        # Lit le contenu du fichier et l'insère dans la zone de texte
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        entry_message_encrypt.delete("1.0", "end")
        entry_message_encrypt.insert("1.0", content)
        messagebox.showinfo("Fichier chargé", "Le contenu du fichier a été inséré dans le champ d'entrée.")
    except Exception as e:
        # Affiche une erreur en cas de problème
        messagebox.showerror("Erreur", f"Impossible de lire le fichier : {str(e)}")

# Configuration de la fenêtre principale
root = tk.Tk()
root.title("Cryptage et Décryptage")

# Widgets pour l'interface utilisateur
tk.Label(root, text="Message à crypter :").grid(row=0, column=1, padx=10, pady=10)
entry_message_encrypt = tk.Text(root, width=50, height=10)
entry_message_encrypt.grid(row=0, column=2, pady=10)

label_key = tk.Label(root, text="Clé de cryptage:", wraplength=400, justify="left")
label_key.grid(row=2, column=1, columnspan=2)

btn_generate_key = tk.Button(root, text="Générer Clé", command=on_generate_key)
btn_generate_key.grid(row=2, column=0, padx=10, pady=10)

btn_encrypt = tk.Button(root, text="Crypter", command=on_encrypt)
btn_encrypt.grid(row=0, column=0, padx=10, pady=10)

tk.Label(root, text="Message à décrypter :").grid(row=3, column=1, padx=10, pady=10)
entry_message_decrypt = tk.Text(root, width=50, height=10)
entry_message_decrypt.grid(row=3, column=2, padx=10, pady=10)

btn_decrypt = tk.Button(root, text="Décrypter", command=on_decrypt)
btn_decrypt.grid(row=3, column=0, padx=10, pady=10)

label_result = tk.Label(root, text="Résultat cryptage:", wraplength=400, justify="left")
label_result.grid(row=1, column=2, columnspan=2, padx=10, pady=10)

label_result_decrypted = tk.Label(root, text="Résultat décryptage:", wraplength=400, justify="left")
label_result_decrypted.grid(row=4, column=2, columnspan=2, padx=10, pady=10)

btn_select_file = tk.Button(root, text="Charger un fichier", command=on_select_file)
btn_select_file.grid(row=5, column=0, columnspan=2, pady=10)

# Lancement de la boucle principale de l'interface
root.mainloop()