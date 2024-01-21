from pydub import AudioSegment
import pygame
import time

# Ses dosyasını yükle
song = AudioSegment.from_file("C:/Users/Doğukan/OneDrive/Masaüstü/Gaye_Su_Akyol_İçinde_Uyanıyoruz_Hakikatin_Offical_Audio_VP_FSNcZ4ZQ.m4a", format="m4a")

# MP3 formatına dönüştür
song.export("C:/Users/Doğukan/OneDrive/Masaüstü/Gaye_Su_Akyol_İçinde_Uyanıyoruz_Hakikatin_Offical_Audio_VP_FSNcZ4ZQ.mp3", format="mp3")

pygame.mixer.init()
pygame.mixer.music.load("C:/Users/Doğukan/OneDrive/Masaüstü/Gaye_Su_Akyol_İçinde_Uyanıyoruz_Hakikatin_Offical_Audio_VP_FSNcZ4ZQ.mp3")
pygame.mixer.music.play()

# Müziğin çalma süresi boyunca bekleyin
while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)  # Küçük bir bekleme süresi ekleyin (örneğin, 10 milisaniye)

pygame.mixer.quit()