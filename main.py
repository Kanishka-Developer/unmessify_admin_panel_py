# requirements: requests, airtable, tkinter, sv-ttk, darkdetect, pywinstyles

import tkinter as tk
from uap_ui import UAP_UI

import sv_ttk, darkdetect

import pywinstyles, sys

def apply_theme_to_titlebar(root):
    version = sys.getwindowsversion()
    if version.major == 10 and version.build >= 22000:
        pywinstyles.change_header_color(root, "#1c1c1c" if sv_ttk.get_theme() == "dark" else "#fafafa")
    elif version.major == 10:
        pywinstyles.apply_style(root, "dark" if sv_ttk.get_theme() == "dark" else "normal")
        root.wm_attributes("-alpha", 0.99)
        root.wm_attributes("-alpha", 1)

def main():
    root = tk.Tk()
    app = UAP_UI(root)
    sv_ttk.set_theme(darkdetect.theme())
    apply_theme_to_titlebar(root)
    root.mainloop()

if __name__ == "__main__":
    main()
