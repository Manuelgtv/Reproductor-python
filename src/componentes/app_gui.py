import so
import tkinter as tk
from tkinter import filedialog
from src.config.styles import COLOR_PURPLE, COLOR_BG, COLOR_CARD_BG, COLOR_GRID_FG, COLOR_CARD_BORDER, COLOR_CARD_HOVER
from src.core.audio_player import AuidioPlayer
from src.core.card_cancion import CardCancion
from src.ui.components.player_bar import PlayerBar
from src.ui.components.navbar import Navbar


class APPMusicPlayer(tk.Tk):

    def __init__(self):
        super().__init__()
        

