import customtkinter as ctk
import modules.work_with_json as work_w_json
import modules.find_path as find
from PIL import Image

app = ctk.CTk(fg_color = "#000000")
# print(type(app), app)
app.geometry("448x515")
app.title("APP")
name, surname, age = "", "", ""

background = ctk.CTkFrame(master = app, width = 448, height = 515, corner_radius = 15, fg_color = "#403A3A", border_width = 5, border_color = "#FCA625")

image = Image.open(find.path_finder("images\\bg.png"))
bg_image = ctk.CTkImage(light_image = image, size = (375, 375))
background_image = ctk.CTkLabel(master = background, width = 375, height = 375, image = bg_image)

text_create = ctk.CTkLabel(master = background, width = 211, height = 30, text = "CREATE", font = ("Inter", 30))
text_json   = ctk.CTkLabel(master = background, width = 100, height = 20, text = "JSON", font = ("Inter", 30), bg_color = "#1e1e1e")

entry_font = ctk.CTkFont("Inter", 16)

name_entry = ctk.CTkEntry(master = background_image, width = 307, 
                          height = 66, textvariable = name, 
                          corner_radius = 15, fg_color = "#4F4F4F",
                          border_width = 5, border_color = "#FCA625",
                          placeholder_text = "Enter your name...", font = entry_font, bg_color = "#1e1e1e")

surname_entry = ctk.CTkEntry(master = background_image, width = 307,
                            height = 66, textvariable = surname,
                            corner_radius = 15,fg_color ="#4F4F4F",
                            border_width = 5,border_color= "#FCA625",
                            placeholder_text = "Enter your surname...", font = entry_font, bg_color = "#1e1e1e")

age_entry = ctk.CTkEntry(master = background_image, width = 307,
                        height = 66, textvariable = age,
                        corner_radius = 15, fg_color = "#4F4F4F",
                        border_width = 5, border_color = "#FCA625",
                        placeholder_text = "Enter your age...", font = entry_font, bg_color = "#1e1e1e")

warning_label_cors = [600, 600]

def warning_label_edit(text = None):
    global warning_label, warning_label_cors
    if text != None:
        print("warn on screen")
        warning_label = ctk.CTkLabel(master = background, width = 150, height = 25, corner_radius = 10, fg_color = "#363636", text = text, font = ("Inter", 16), bg_color = "#1e1e1e")
        warning_label_cors = [112, 410]
        app.after(3000, warning_label_edit)
    else:
        warning_label_cors = [600, 600]
    warning_label.place(x = warning_label_cors[0], y = warning_label_cors[1])

def save_data():
    name, surname, age = name_entry.get(), surname_entry.get(), age_entry.get()
    if name == "" or surname == "" and age == "":
        warning_label_edit("One or more entry field is blank")
        return
    try:
        age = int(age)
        warning_label_edit("Save succesful!")
        work_w_json.create_json("New_json_file.json", {"name": name, "surname": surname, "age": age})
    except:
        warning_label_edit("Age must be a number")
        
button_save = ctk.CTkButton(master = background, width = 144,
                            height = 47, corner_radius = 15,
                            border_width = 2, fg_color = "#4F4F4F",
                            hover_color = "#6b6a6a", border_color = "#FCA625",
                            text = "SAVE", hover = True, font = ("Arial", 20),
                            command = save_data)

background.place(x = 0, y = 0)
background_image.place(x = 37, y = 64)
name_entry.place(x = 35, y = 40)
surname_entry.place(x = 35, y = 151)
age_entry.place(x = 35, y = 262)
button_save.place(x = 150, y = 440)
text_create.place(x = 115,y = 29)
text_json.place(x = 168, y = 66)

app.mainloop()