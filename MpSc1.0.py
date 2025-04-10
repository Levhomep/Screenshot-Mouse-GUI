import customtkinter as ctk
import time
import pyautogui

#  Start
time.sleep(2)

# Function to get Position and Pixel-colour of mouse
def piXpoS(_):
    p = pyautogui.position()  # Mouseposition
    try:
        c = pyautogui.pixel(p[0], p[1])  # Colour of Pixel
        text = f"Position: {p}, Colour: {c}"  # Text Collecting
        label_info.configure(text=text)  # refresh of Text Label
    except OSError:
        label_info.configure(text="Position out of Range!")
# Funktion for Screenshot
def screen_shot():
    screenshot = pyautogui.screenshot()  # create Screenshot (x,y,widght,high) add parameter for section Screenshot, empty "()" takes fullscreen
    screenshot.save("1.png")  # saving Screenshot in same folder as the script
    label_info.configure(text="Screenshot saved as '1.png'")

# Create Mainwindow
ctk.set_appearance_mode("Dark")  #  (System, Dark, Light)
hauptfenster = ctk.CTk()  # Creation Mainwindow
hauptfenster.geometry("500x200")
hauptfenster.title("MpSc 1.0")  # Titel of the Window
hauptfenster.eval('tk::PlaceWindow . center')  # Mainwindow starts in Center Position
# Infotext-Label at Start
label_info = ctk.CTkLabel(hauptfenster, text="Press 'h', to see Mousepostion and Pixelcolour!", font=("Arial", 14 ,"bold"))
label_info.pack(pady=20)

# Button for Screenshot
button_screenshot = ctk.CTkButton(hauptfenster, text="Take Screenshot", width=200, height=40, command=screen_shot)
button_screenshot.pack(pady=10)

# Beenden-Button
button_exit = ctk.CTkButton(hauptfenster, text="Close", width=200, height=40, command=hauptfenster.destroy)
button_exit.pack(pady=10)

# Key-Binding for 'h'
hauptfenster.bind('<h>', piXpoS)

# Mainloop start
hauptfenster.mainloop()

