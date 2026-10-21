import os 
import tkinter as tk
from src.cinfig.styles import COLOR_CARD_FG, COLOR_CARD_BORDER, COLOR_CARD_HOVER, COLOR_CARD_BG

class CardCancion(tk.Frame):

    _icon_play= None

    def __init__( self, root, cancion, onplay,on_favorito):
        super().__init__(root,bg=COLOR_CARD_BG , bd=1, relief="solid", width=200, height=175)
        self.grid_propagate(False)

        footer = tk.Label(self, bg= COLOR_CARD_BG, height=55, padx=8,pady=6)
        footer.pack(Side="bottom", fil="x")

        tk.Label(footer,text=cancion.titulo, bg=COLOR_CARD_BG, fg= COLOR_CARD_FG, font=("Arial",10)).pack(side="left", padx=(0,6))

        info=tk.Frame(footer, bg=COLOR_CARD_BG)
        info.pack(side="left", fill="x",expand=True)

        titulo=cancion["titulo"]
        if len(titulo) > 16:
            titulo=titulo[:16]+"..."

        tk.Label(info, text=titulo, bg=COLOR_CARD_BG, fg=COLOR_CARD_FG, font=("arial", 10)).pack(side="top",anchor="w")
        tk.Label(info, text=cancion)