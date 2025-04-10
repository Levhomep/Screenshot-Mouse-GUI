import customtkinter as ctk
import time
import pyautogui

# Startzeitverzögerung
time.sleep(2)

# Funktion zur Aktualisierung der Position und Farbe
def piXpoS(_):
    p = pyautogui.position()  # Mausposition
    try:
        c = pyautogui.pixel(p[0], p[1])  # Farbe des Pixels
        text = f"Position: {p}, Farbe: {c}"  # Text zusammenstellen
        label_info.configure(text=text)  # Text des Labels aktualisieren
    except OSError:
        label_info.configure(text="Position außerhalb des Bildschirms!")
# left = X-Position des linken oberen Punkts   
# top = Y-Position des oberen Punkts
# width = Breite des Screenshots
# height = Höhe des Screenshots
# region=(left, top, width, height)
# Funktion für Screenshot
def screen_shot():
    screenshot = pyautogui.screenshot()  # Screenshot erstellen
    screenshot.save("1.png")  # Screenshot speichern
    label_info.configure(text="Screenshot gespeichert als '1.png'")

# Hauptfenster erstellen
ctk.set_appearance_mode("Dark")  # Erscheinungsmodus (System, Dark, Light)
hauptfenster = ctk.CTk()  # Erstellen des Hauptfensters
hauptfenster.geometry("500x200")
hauptfenster.title("MpSc 1.0")  # Titel des Fensters
hauptfenster.eval('tk::PlaceWindow . center')  # Fenster zentrieren
# Hinweistext-Label für Position und Farbe
label_info = ctk.CTkLabel(hauptfenster, text="Drücke 'h', um die Position und Farbe der Maus zu sehen!", font=("Arial", 14 ,"bold"))
label_info.pack(pady=20)

# Button für Screenshot
button_screenshot = ctk.CTkButton(hauptfenster, text="Take Screenshot", width=200, height=40, command=screen_shot)
button_screenshot.pack(pady=10)

# Beenden-Button
button_exit = ctk.CTkButton(hauptfenster, text="Beenden", width=200, height=40, command=hauptfenster.destroy)
button_exit.pack(pady=10)

# Key-Binding für 'h'
hauptfenster.bind('<h>', piXpoS)

# Hauptloop starten
hauptfenster.mainloop()

