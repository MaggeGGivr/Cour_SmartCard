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


# Load the image
image = tk.PhotoImage(file="c:\\Users\\dfalco\\isen.png")

# Create a label with the image
image_label = tk.Label(windows, image=image)
image_label.pack()

# Keep a reference to the image to prevent it from being garbage collected
image_label.image = image

#detection d'un carte branché
def detect_card():
    try:
        # Get the list of available readers
        r = readers()
        if len(r) > 0:
            # Create a connection with the first reader
            connection = r[0].createConnection()
            # Connect to the card
            connection.connect()
            # Display the reader information in the Text widget
            card_info.insert(tk.END, str(r[0]) + "\n")
        else:
            card_info.insert(tk.END, "No smart card readers detected.\n")
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

# Ajouter un bouton "Détecter"
button_detect = tk.Button(button_frame, text="Détecter", command=detect_card, bg="White", fg="black")
button_detect.pack(side=tk.BOTTOM, padx=10, pady=10)

windows.mainloop()

# def read_card():
#     try:
#         # Get the list of available readers
#         r = readers()
#         # Create a connection with the first reader
#         connection = r[0].createConnection()
#         # Connect to the card
#         connection.connect()
#         # Define the SELECT APDU command
#         SELECT = [0xA0, 0xA4, 0x00, 0x00, 0x02]
#         DF_TELECOM = [0x7F, 0x10]
#         # Send the SELECT APDU command to the card
#         data, sw1, sw2 = connection.transmit(SELECT + DF_TELECOM)
#         # Display the response in the Text widget
#         card_info.insert(tk.END, "%x %x\n" % (sw1, sw2))
#     except Exception as e:
#         card_info.insert(tk.END, str(e) + "\n")

# def write_card():
#     try:
#         # Get the list of available readers
#         r = readers()
#         # Create a connection with the first reader
#         connection = r[0].createConnection()
#         # Connect to the card
#         connection.connect()
#         # Define the WRITE APDU command (replace with your actual command)
#         WRITE = [0xA0, 0xD6, 0x00, 0x00, 0x02]
#         DATA = [0x01, 0x02]  # Replace with your actual data
#         # Send the WRITE APDU command to the card
#         data, sw1, sw2 = connection.transmit(WRITE + DATA)
#         # Display the response in the Text widget
#         card_info.insert(tk.END, "%x %x\n" % (sw1, sw2))
#     except Exception as e:
#         card_info.insert(tk.END, str(e) + "\n")