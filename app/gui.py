from tkinter import *
from tkinter import ttk
from app.data.db import DB
from app.parser.file_grabber import ParseFile as bl
from tinydb import TinyDB, Query

db = TinyDB("data/db.json")

#todo WIP gui

root = Tk()
root.title("Zeus Model Editor")
root.geometry("900x400")

types = ["house", "building"]
subtypes = [
    {"type": "house", "subtypes": ["common_house", "elite_house"]},
    {"type": "building", "subtypes": ["food", "raw", "workshop", "service", "storage", "culture", "gov", "sanctuary", "decor"]}
]

#global building_selected
#building_selected = None

def pick_subtype(e):
    if type_combo.get() == "house":
        subtype_combo.config(values=subtypes[0]["subtypes"])
        subtype_combo.current(0)
        building_selector.set('')
    elif type_combo.get() == "building":
        subtype_combo.config(values=subtypes[1]["subtypes"])
        subtype_combo.current(0)
        building_selector.set('')
    else:
        subtype_combo.config(values=[" "])
        building_selector.config(values=["  "])

def pick_building(e):
    selected = subtype_combo.get()
    options = getattr(bl,selected)
    building_selector.config(values=options)
    building_selector.current(0)

#def get_building(e):
#    building_selected = building_selector.get()
#    print(building_selected)

type_combo = ttk.Combobox(root, values=types)
type_combo.grid(row=0,column=0, padx=10, pady=4)
type_combo.bind("<<ComboboxSelected>>", pick_subtype)

subtype_combo = ttk.Combobox(root, values=[" "])
subtype_combo.grid(row=0, column=1, padx=10, pady=4)
subtype_combo.bind("<<ComboboxSelected>>", pick_building)

building_selector = ttk.Combobox(root, values = [" "])
building_selector.grid(row=0, column=2, padx=10, pady=4)
#building_selector.bind('<<ComboboxSelected>>', get_building)

frame = LabelFrame(root)
frame.grid(row=1, column=0)

def click():
    building_selected = building_selector.get()
    building = DB.get_building_by_name(db, building_selected)
    for widget in frame.winfo_children():
        widget.destroy()

    for i, value in enumerate(building["default_values"]):
            v = StringVar(frame, value=value["values"][0])
            Label(frame, text=value["name"]).grid(row=i+1+1, padx=2, pady=4, sticky='w')
            Entry(frame, textvariable=v).grid(row=i+1+1, column=1, padx=4, pady=4, sticky='e')
            Label(frame, text=value["description"]).grid(row=i+1+1, column=2, padx=2, pady=4, sticky='w')

#TODO finish save function
def save():
    values = []
    children_widgets = frame.winfo_children()
    for child_widget in children_widgets:
        if child_widget.winfo_class() == 'Entry':
            values.append(child_widget.get())
    print(values)

Button(text='click',command=click).grid(row=0, column=3)
Button(text='save',command=save).grid(row=2, column=1)

if __name__ == '__main__':
    root.mainloop()

