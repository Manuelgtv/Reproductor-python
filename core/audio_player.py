import os

try:
    import pygame
    pygame.mixer.init()
    AUDIO=True

except Exception:
    AUDIO=False


class AudioPlayer:

    def reproducir(self, ruta):
        if AUDIO and ruta and os.path.exists(ruta):
            pygame.mixer.music.load(ruta)
            pygame.mixer.music.play()


    def pausar(self):
        if AUDIO:
            pygame.mixer.music.pause()

    def reudar(Self):
        if AUDIO:
            pygame.mixer.music.unpause()

    def ajustar_volumen(self, valor):
        if AUDIO:
            pygame.mixer.music.set_volume(float(valor))
            