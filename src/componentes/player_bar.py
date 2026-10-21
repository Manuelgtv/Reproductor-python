from tkinter import ttk
from src.config.styles import COLOR_BAR_BG
from turtle import left, right


class PlayerBar(tk.Frame):
    def __init__(Self, root, on_toggle_play, on_volume):
        super().__init__(root, bg=COLOR_BAR_BG, height=60)
        Self.pack_propagate(False)



        self.icon_corazon=tk.PhotoImage(file=os.path.join(ICONS_DIR,"heart.svg"))
        self.icon_anterior=tk.PhotoImage(file=os.path.join(ICONS_DIR,"previous.svg"))
        self.icon_reproducir=tk.PhotoImage(file=os.path.join(ICONS_DIR,"play.svg"))
        self.icon_pausar=tk.PhotoImage(file=os.path.join(ICONS_DIR,"pause.svg"))
        self.icon_siguente=tk.PhotoImage(file=os.path.join(ICONS_DIR,"next.svg"))
        self.icon_volumen=tk.PhotoImage(file=os.path.join(ICONS_DIR,"volume.svg"))



        #CONTROLES CENTRALES
        controles= tk.Frame(Self,bg=COLOR_BAR_BG)
        controles.pack(pady=(6,2))


        #Btotones centrales

        btn_corazon= tk.Button(
            controles,image= Self.icon_corazon,bd=0, relief="flat", bg=COLOR_BAR_BG, cursor="hand2"
            ).grid(row=0, column=0, padx=8)


        btn_anterior= tk.Button(
            controles,image= Self.icon_anterior,bd=0, relief="flat", bg=COLOR_BAR_BG, cursor="hand2"
            ).grid(row=0, column=1, padx=6)

        btn_play= tk.Button(
            controles,image= Self.icon_reproducir,bd=0, relief="flat", bg=COLOR_BAR_BG, cursor="hand2"
            ).grid(row=0, column=3, padx=6)

        btn_siguente= tk.Button(
            controles,image= Self.icon_siguente,bd=0, relief="flat", bg=COLOR_BAR_BG, cursor="hand2"
            ).grid(row=0, column=3, padx=6)

        btn_volumen= tk.Button(
            controles,image= Self.icon_volumen,bd=0, relief="flat", bg=COLOR_BAR_BG, cursor="hand2"
            ).grid(row=0, column=4, padx=8)

 
     #TIEMPO Y BARRA DE PROGRESO
        track = tk.Frame(Self, bg=COLOR_BAR_BG)
        track.pack(fill="x", padx=30, pady=(2,6))
    
        tk.Label(track, text="0:00", bg=COLOR_BAR_BG, font= ("Arial", 10, "bold")).pack(side="left", padx=5)
        tk.Scale(track, from_=0, to=100, orient="horizontal", showvalue=False).pack(side="center", extend=True, padx=8)
        tk.Label(track, text="0:00", bg=COLOR_BAR_BG, font= ("Arial", 10, "bold")).pack(side="right", padx=5)



    def set_play_icon(self, reproduciendo):
        nuevo_icono= self.icon_pausar if reproduciendo else self.icon_reproducir
        self.btn_play.confing(image= nuevo_icono)
        self.btn_play.image=nuevo_icono
        










        #tk.Button(controles, text="❤️", bg="#222222", font=("arial",12)cursor="hand2").grid(row=0,column=0, padx=8)
        #tk.Button(controles, text="⏸️", bg="#222222", font=("arial",12)cursor="hand2").grid(row=0,column=1, padx=6)

       # Self.btn_play = tk.Button(
           # controles, text="⏸️", bg="#222222", bg=1, relief="flat").grid(row=0,column=3, padx=6)

 






























