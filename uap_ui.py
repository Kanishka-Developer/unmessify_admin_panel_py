import tkinter as tk
from tkinter import ttk

from uap_at import AirtableClient

class UAP_UI:
    def __init__(self, root):
        self.root = root
        self.root.title('Unmessify Admin Panel')
        self.root.geometry('1700x1050')

        self.hostel_blocks = ["A", "B", "C Boys", "C Girls", "D1", "D2"]
        self.caterers = {
            "A": ["CRCL", "Fusion", "Mother", "Proodle"],
            "B": ["ABFC", "Shakti", "SRRC", "Zenith"],
            "C Boys": ["SRRC", "Zenith"],
            "C Girls": ["SRRC", "Zenith", "ABFC", "Shakti"],
            "D1": ["CRCL", "Fusion", "Mother", "Proodle"],
            "D2": ["CRCL", "Fusion", "Mother", "Proodle"],
        }
        self.mess_types = ["Veg", "Non-Veg", "Special"]
        self.meals = ["Breakfast", "Lunch", "Snacks", "Dinner"]
        self.days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

        self.hostel_block = tk.StringVar()
        self.hostel_type = tk.StringVar()
        self.caterer = tk.StringVar()
        self.mess_type = tk.StringVar()

        self.at = AirtableClient()

        self.create_widgets()

    def create_widgets(self):
        
        self.hostel_block_label = ttk.Label(self.root, text="Hostel Block")
        self.hostel_block_label.grid(row=0, column=1, sticky='w', padx=(70, 10))
        self.hostel_block_combobox = ttk.Combobox(self.root, values=self.hostel_blocks, textvariable=self.hostel_block)
        self.hostel_block_combobox.grid(row=0, column=1, sticky='w', padx=(190, 10))

        self.caterer_label = ttk.Label(self.root, text="Caterer")
        self.caterer_label.grid(row=0, column=2, sticky='w', padx=(340, 10))
        self.caterer_combobox = ttk.Combobox(self.root, values=[], textvariable=self.caterer)
        self.caterer_combobox.grid(row=0, column=3, sticky='w', padx=(30, 10))

        self.mess_type_label = ttk.Label(self.root, text="Mess Type")
        self.mess_type_label.grid(row=0, column=4, sticky='w', padx=(90, 10))
        self.mess_type_combobox = ttk.Combobox(self.root, values=self.mess_types, textvariable=self.mess_type)
        self.mess_type_combobox.grid(row=0, column=4, sticky='w', padx=(190, 10))

        self.meal_labels = []
        self.text_boxes = []
        for i, meal in enumerate(self.meals):
            meal_label = ttk.Label(self.root, text=meal)
            meal_label.grid(row=1, column=i+1)
            self.meal_labels.append(meal_label)

            for j, day in enumerate(self.days):
                if i == 0:
                    day_label = ttk.Label(self.root, text=day)
                    day_label.grid(row=j+2, column=0)

                text_box = tk.Text(self.root, height=8, width=50)
                text_box.grid(row=j+2, column=i+1)
                self.text_boxes.append(text_box)

        self.refresh_button = ttk.Button(self.root, text="Refresh", command=self.refresh_menu, style="Accent.TButton")
        self.refresh_button.grid(row=9, column=1, pady=(20, 0))

        self.update_button = ttk.Button(self.root, text="Update", command=self.upload_menu, style="Accent.TButton")
        self.update_button.grid(row=9, column=4, pady=(20, 0))

        self.hostel_block_combobox.bind("<<ComboboxSelected>>", self.on_hostel_block_selected)
        self.mess_type_combobox.bind("<<ComboboxSelected>>", self.on_mess_type_selected)

    def on_hostel_block_selected(self, event):
        hostel_block = self.hostel_block.get()
        self.hostel_type = "W" if self.hostel_block.get() in ["B", "C Girls"] else "M"
        caterers = self.caterers[hostel_block]
        self.caterer_combobox['values'] = caterers
        self.caterer.set(caterers[0])
        self.mess_type.set(self.mess_types[0])

        self.update_menu()

    def on_mess_type_selected(self, event):
        self.update_menu()

    def update_menu(self):
        mess_type = self.mess_type.get()
        menu = self.at.get_menu(self.hostel_type, mess_type[0])
        for i, meal in enumerate(self.meals):
            for j, day in enumerate(self.days):
                text_box = self.text_boxes[i*len(self.days)+j]
                if isinstance(text_box, tk.Text):
                    text_box.delete("1.0", tk.END)
                    text_box.insert("1.0", menu[day][meal])
                else:
                    print(f"Error: Expected tk.Text, but got {type(text_box)}")
    
    def refresh_menu(self):
        self.at.fetch_menu(self.hostel_type, self.mess_type.get()[0])
        self.at.transform_menu(f"VITC-{self.hostel_type}-{self.mess_type.get()[0]}")
        self.update_menu()

    def upload_menu(self):
        new_menu = {}
        for i, meal in enumerate(self.meals):
            for j, day in enumerate(self.days):
                text_box = self.text_boxes[i*len(self.days)+j]
                new_menu[day] = new_menu.get(day, {})
                new_menu[day][meal] = text_box.get("1.0", tk.END)
                new_menu[day]['id'] = self.at.get_menu(self.hostel_type, self.mess_type.get()[0])[day]['id']
        self.at.update_menu(self.hostel_type, self.mess_type.get()[0], new_menu)

if __name__ == "__main__":
    print("Don't run this file directly. Run main.py instead.")
