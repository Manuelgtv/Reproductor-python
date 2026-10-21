class Navbar(tk.Frame):
    def __init__(self, root):


        #Buscar
        frame_buscar=tk.Frame(self, bg=COLOR_PURPLE, padx=12, pady=6)
        frame_buscar.pack(side="left", padx=25, pady=10)

        #lbl_buscar_icono=tk.Label(frame_buscar, text="🔎", bg=COLOR_PURPLE, fg="white",font=("Arial", 16, "bold"))
        #lbl_buscar_icono.pack(side="left", padx=(0,8))

        #boton configuración
        #btn_confing= tk.BOTTOM(
        # self, text="⚙️", bg="#ffffff", fg="#444444", bg=0, font=("Arial", 16), cursor="hand2")
        #btn_coinfig.pack(side="right", padx=25)






        self.icon_buscar=tk.PhotoImage(file=os.path.join(ICONS_DIR, "search.svg"))
        self.icon_configuracion=tk.PhotoImage(file=os.path.join(ICONS_DIR,"settings.svg"))


        #BOTON DE CONFIGURACIÓN
        btn_config=tk.Button(
            self,
            image=self.icon_configuracion,
            bg=0,
            relief="flat",
            cursor="hand2"
        )
        btn_config.pack(side="right", padx=25)



        btn_buscar= tk.Button(
            frame_buscar,
            bg=COLOR_PURPLE,
            bd=0,
            relief="flat",
            cursor="hand2"
        )
        btn_buscar.pack(side="left")  


        self.entry_buscar = tk.Entry(
            frame_buscar,
            bg=COLOR_PRUPLE,
            fg="white",
            font=("Arial",12),
            bd=0,
            relief="flat",
            planceholder="Buscar",
            insertbackground= "white"
        )
        self.entry_buscar.pack(side="left")










