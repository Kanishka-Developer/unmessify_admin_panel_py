import tkinter as tk
from tkinter import ttk

from uap_at import AirtableClient

from uap_fb import FirebaseClient

from datetime import datetime

class UAP_UI:
    def __init__(self, root):
        self.root = root
        self.root.title('Unmessify Admin Panel')
        self.root.geometry('1700x1050')

        self.hostel_types = ["M", "W"]
        self.hostel_blocks = ["A", "B", "C Boys", "C Girls", "D1", "D2"]
        self.mess_types = ["Veg", "Non-Veg", "Special"]
        self.caterers = {
            "A": {
                "Veg": ["CRCL", "Fusion", "Proodle", "Mother"],
                "Non-Veg": ["CRCL", "Fusion", "Mother"],
                "Special": ["Fusion", "Mother"]
            },
            "B": {
                "Veg": ["ABFC", "Shakti", "SRRC", "Zenith"],
                "Non-Veg": ["ABFC", "Shakti", "SRRC", "Zenith"],
                "Special": ["ABFC", "Shakti", "SRRC", "Zenith"]
            },
            "C Boys": {
                "Veg": ["SRRC", "Zenith"],
                "Non-Veg": ["SRRC", "Zenith"],
                "Special": ["SRRC", "Zenith"]
            },
            "C Girls": {
                "Veg": ["ABFC", "Shakti", "SRRC", "Zenith"],
                "Non-Veg": ["ABFC", "Shakti", "SRRC", "Zenith"],
                "Special": ["ABFC", "Shakti", "SRRC", "Zenith"]
            },
            "D1": {
                "Veg": ["CRCL", "Fusion", "Proodle", "Mother"],
                "Non-Veg": ["CRCL", "Fusion", "Mother"],
                "Special": ["Fusion", "Mother"]
            },
            "D2": {
                "Veg": ["CRCL", "Fusion", "Proodle", "Mother"],
                "Non-Veg": ["CRCL", "Fusion", "Mother"],
                "Special": ["Fusion", "Mother"]
            }
        }
        self.caterer_codes = {
            "A": {
                "Veg": {
                    "CRCL": "A1",
                    "Fusion": "A2",
                    "Proodle": "A3",
                    "Mother": "A4"
                },
                "Non-Veg": {
                    "CRCL": "A1",
                    "Fusion": "A2",
                    "Mother": "A3"
                },
                "Special": {
                    "Fusion": "A1",
                    "Mother": "A2"
                }
            },
            "B": {
                "Veg": {
                    "ABFC": "B1",
                    "Shakti": "B2",
                    "SRRC": "B3",
                    "Zenith": "B4"
                },
                "Non-Veg": {
                    "ABFC": "B1",
                    "Shakti": "B2",
                    "SRRC": "B3",
                    "Zenith": "B4"
                },
                "Special": {
                    "ABFC": "B1",
                    "Shakti": "B2",
                    "SRRC": "B3",
                    "Zenith": "B4"
                }
            },
            "C Boys": {
                "Veg": {
                    "SRRC": "CB1",
                    "Zenith": "CB2"
                },
                "Non-Veg": {
                    "SRRC": "CB1",
                    "Zenith": "CB2"
                },
                "Special": {
                    "SRRC": "CB1",
                    "Zenith": "CB2"
                }
            },
            "C Girls": {
                "Veg": {
                    "ABFC": "CG1",
                    "Shakti": "CG2",
                    "SRRC": "CG3",
                    "Zenith": "CG4"
                },
                "Non-Veg": {
                    "ABFC": "CG1",
                    "Shakti": "CG2",
                    "SRRC": "CG3",
                    "Zenith": "CG4"
                },
                "Special": {
                    "ABFC": "CG1",
                    "Shakti": "CG2",
                    "SRRC": "CG3",
                    "Zenith": "CG4"
                }
            },
            "D1": {
                "Veg": {
                    "CRCL": "D11",
                    "Fusion": "D12",
                    "Proodle": "D13",
                    "Mother": "D14"
                },
                "Non-Veg": {
                    "CRCL": "D11",
                    "Fusion": "D12",
                    "Mother": "D13"
                },
                "Special": {
                    "Fusion": "D11",
                    "Mother": "D12"
                }
            },
            "D2": {
                "Veg": {
                    "CRCL": "D21",
                    "Fusion": "D22",
                    "Proodle": "D23",
                    "Mother": "D24"
                },
                "Non-Veg": {
                    "CRCL": "D21",
                    "Fusion": "D22",
                    "Mother": "D23"
                },
                "Special": {
                    "Fusion": "D21",
                    "Mother": "D22"
                }
            }
        }

        self.meals = ["Breakfast", "Lunch", "Snacks", "Dinner"]
        self.days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

        self.hostel_type = tk.StringVar()
        self.hostel_block = tk.StringVar()
        self.mess_type = tk.StringVar()
        self.caterer = tk.StringVar()

        self.at = AirtableClient()
        self.fb = FirebaseClient()

        self.create_widgets()

    def create_widgets(self):
        
        self.hostel_block_label = ttk.Label(self.root, text="Hostel Block")
        self.hostel_block_label.grid(row=0, column=1, sticky='w', padx=(50, 10))
        self.hostel_block_combobox = ttk.Combobox(self.root, values=self.hostel_blocks, textvariable=self.hostel_block)
        self.hostel_block_combobox.grid(row=0, column=1, sticky='w', padx=(160, 10))

        self.mess_type_label = ttk.Label(self.root, text="Mess Type")
        self.mess_type_label.grid(row=0, column=2, sticky='w', padx=(315, 10))
        self.mess_type_combobox = ttk.Combobox(self.root, values=self.mess_types, textvariable=self.mess_type)
        self.mess_type_combobox.grid(row=0, column=3, sticky='w', padx=(15, 10))

        self.caterer_label = ttk.Label(self.root, text="Caterer")
        self.caterer_label.grid(row=0, column=4, sticky='w', padx=(70, 10))
        self.caterer_combobox = ttk.Combobox(self.root, values=[], textvariable=self.caterer)
        self.caterer_combobox.grid(row=0, column=4, sticky='w', padx=(150, 10))

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
        self.mess_type.set(self.mess_types[0])
        caterers = self.caterers[hostel_block][self.mess_type.get()]
        self.caterer_combobox['values'] = caterers
        self.caterer.set(caterers[0])
        self.update_menu()

    def on_mess_type_selected(self, event):
        self.update_menu()
        caterers = self.caterers[self.hostel_block.get()][self.mess_type.get()]
        self.caterer_combobox['values'] = caterers
        self.caterer.set(caterers[0])

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
        time = datetime.now().strftime("%m/%d/%Y %H:%M:%S")
        updated_caterers = []
        if self.hostel_type.get() == "M" or self.caterer.get() in ["SRRC", "Zenith"]:
            for block in ["A", "C Boys", "D1", "D2"]:
                for caterer in self.caterers[block][self.mess_type.get()]:
                    code = self.caterer_codes[block][self.mess_type.get()][caterer]
                    if code not in updated_caterers:
                        self.fb.update(f"org-backup/vitc/mess/{self.caterer_codes[block][self.mess_type.get()][caterer]}-{self.mess_type.get()[0]}", {"menuUpdated": time})
                        updated_caterers.append(code)
            for block in ["B", "C Girls"]:
                for caterer in ["SRRC", "Zenith"]:
                    code = self.caterer_codes[block][self.mess_type.get()][caterer]
                    if code not in updated_caterers:
                        self.fb.update(f"org-backup/vitc/mess/{self.caterer_codes[block][self.mess_type.get()][caterer]}-{self.mess_type.get()[0]}", {"menuUpdated": time})
                        updated_caterers.append(code)
        else:
            for block in ["B", "C Girls"]:
                for caterer in ["ABFC", "Shakti"]:
                    code = self.caterer_codes[block][self.mess_type.get()][caterer]
                    if code not in updated_caterers:
                        self.fb.update(f"org-backup/vitc/mess/{self.caterer_codes[block][self.mess_type.get()][caterer]}-{self.mess_type.get()[0]}", {"menuUpdated": time})
                        updated_caterers.append(code)

if __name__ == "__main__":
    print("Don't run this file directly. Run main.py instead.")
