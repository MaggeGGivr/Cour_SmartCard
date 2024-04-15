import tkinter as tk
import smartcard
from smartcard.System import readers
from smartcard.util import toHexString

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

# Charger l'image
image = tk.PhotoImage(file="isen.png")

# Créer un label avec l'image
image_label = tk.Label(windows, image=image)
image_label.pack()

# Garder une référence à l'image pour éviter qu'elle ne soit pas collectée par le garbage collector
image_label.image = image

# Détection d'une carte branchée
def detect_card():
    try:
        # Obtenir la liste des lecteurs disponibles
        r = readers()
        if len(r) > 0:
            # Créer une connexion avec le premier lecteur
            connection = r[0].createConnection()
            # Se connecter à la carte
            connection.connect()
            # Obtenir l'ATR
            atr = connection.getATR()
            # Afficher les informations du lecteur et l'ATR dans le widget Text
            card_info.insert(tk.END, str(r[0]) + "\n")
            card_info.insert(tk.END, "ATR: " + toHexString(atr) + "\n")
        else:
            card_info.insert(tk.END, "Aucun lecteur de carte à puce détecté.\n")
    except Exception as e:
        card_info.insert(tk.END, str(e) + "\n")

def read_card():
    try:
        # Obtenir la liste des lecteurs disponibles
        r = readers()
        # Créer une connexion avec le premier lecteur
        connection = r[0].createConnection()
        # Se connecter à la carte
        connection.connect()
        # Obtenir l'ATR
        atr = connection.getATR()
        # Afficher l'ATR dans le widget Text
        card_info.insert(tk.END, "ATR: " + toHexString(atr) + "\n")
        # Définir la commande APDU SELECT
        SELECT = [0xA0, 0xA4, 0x00, 0x00, 0x02]
        DF_TELECOM = [0x7F, 0x10]
        # Envoyer la commande APDU SELECT à la carte
        data, sw1, sw2 = connection.transmit(SELECT + DF_TELECOM)
        # Afficher la réponse dans le widget Text
        card_info.insert(tk.END, "%x %x\n" % (sw1, sw2))
    except Exception as e:
        card_info.insert(tk.END, str(e) + "\n")

# Ajouter un bouton "Lire"
button_read = tk.Button(button_frame, text="Lire", command=read_card, bg="green", fg="black")
button_read.pack(side=tk.LEFT, padx=10, pady=10)

# Ajouter un bouton "Ecrire"
button_write = tk.Button(button_frame, text="Ecrire", command="write_card", bg="white", fg="black")
button_write.pack(side=tk.BOTTOM, padx=10, pady=10)

# Ajouter un bouton "Détecter"
button_detect = tk.Button(button_frame, text="Détecter", command=detect_card, bg="White", fg="black")
button_detect.pack(side=tk.BOTTOM, padx=10, pady=10)

windows.mainloop()

# def write_card():
#     try:
#         # Obtenir la liste des lecteurs disponibles
#         r = readers()
#         # Créer une connexion avec le premier lecteur
#         connection = r[0].createConnection()
#         # Se connecter à la carte
#         connection.connect()
#         # Définir la commande APDU WRITE (remplacer par votre véritable commande)
#         WRITE = [0xA0, 0xD6, 0x00, 0x00, 0x02]
#         DATA = [0x01, 0x02]  # Remplacer par vos véritables données
#         # Envoyer la commande APDU WRITE à la carte
#         data, sw1, sw2 = connection.transmit(WRITE + DATA)
#         # Afficher la réponse dans le widget Text
#         card_info.insert(tk.END, "%x %x\n" % (sw1, sw2))
#     except Exception as e:
#         card_info.insert(tk.END, str(e) + "\n")