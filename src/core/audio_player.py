
import tkinter as tk 
from src.config.styles import COLOR_PURPLE


class Navbar(tk.Frame):
    def __init__(self,root):
        super().__init__(root,bg="#ffffff",height=60)
        self.pack_propagate(False)


        frame_buscar= tk.Frame(self,bg=COLOR_PURPLE, padx=12, pady=6)
        frame_buscar.pack(side="left", padx=25,pady=10)


        lbl_buscar_icono= tk.Label(frame_buscar, text="🔎" bg= COLOR_PURPLE, fg="white", font=("Arial", 16, "blod"))
        lbl_buscar_icono.pack(side="left", padx=(0, 8))

        self.entry_buscar = tk.Entry(

            frame_buscar,
            bg= COLOR_PURPLE,
            fg="white",
            font=("arial",12),
            bd=0,
            relief="flat",
            placeholder="buscar",
            insertbackground="white",
)
self.entry_buscar.pack(side="left")

btn_config=tk.BUTTOM(
    self,text="ajuste", bg="#FFFFFF", fg="#444444", bg=0, font=("arial",16),cursor="hand2")
btn_config.pack(side="right", padx=25)