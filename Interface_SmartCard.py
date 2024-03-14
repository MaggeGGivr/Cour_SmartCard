import tkinter as tk
import smartcard

windows = tk.Tk()
windows.title("Interface SmartCard")

# Définir une taille minimale pour la fenêtre
windows.minsize(400, 500)

# Définir une taille initiale pour la fenêtre (largeur x hauteur)
windows.geometry("800x600")

# Créer un widget Text pour afficher les informations de la carte
card_info = tk.Text(windows)
card_info.pack(side=tk.TOP, fill=tk.BOTH, expand=True, padx=10, pady=10)

# Créer une Frame pour les boutons
button_frame = tk.Frame(windows)
button_frame.pack(side=tk.BOTTOM, fill=tk.X, padx=10, pady=10)

# Ajouter un bouton "Quitter"
button_quit = tk.Button(button_frame, text="Quitter", command=windows.destroy, bg="red", fg="black")
button_quit.pack(side=tk.RIGHT, padx=10, pady=10)

#detection d'un carte branché
def detect_card():
    try:
        # Ecrire la carte
        connection = smartcard.System.detect_card()
        # Afficher les informations dans le widget Text
        card_info.insert(tk.END, str(connection) + "\n")
    except Exception as e:
        card_info.insert(tk.END, str(e) + "\n")

# Ajouter un bouton "Lire"
def read_card():
    try:
        # Lire la carte
        connection = smartcard.System.read_card()
        # Afficher les informations dans le widget Text
        card_info.insert(tk.END, str(connection) + "\n")
    except Exception as e:
        card_info.insert(tk.END, str(e) + "\n")

# Ajouter un bouton "Lire"
button_read = tk.Button(button_frame, text="Lire", command=read_card, bg="green", fg="black")
button_read.pack(side=tk.LEFT, padx=10, pady=10)

def write_card():
    try:
        # Ecrire la carte
        connection = smartcard.System.write_card()
        # Afficher les informations dans le widget Text
        card_info.insert(tk.END, str(connection) + "\n")
    except Exception as e:
        card_info.insert(tk.END, str(e) + "\n")

# Ajouter un bouton "Ecrire"
button_write = tk.Button(button_frame, text="Ecrire", command=write_card, bg="white", fg="black")
button_write.pack(side=tk.BOTTOM, padx=10, pady=10)

windows.mainloop()