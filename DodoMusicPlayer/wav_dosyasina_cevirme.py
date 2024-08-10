from pydub import AudioSegment
import pygame
import time

# Ses dosyasını yükle
song = AudioSegment.from_file("C:/Users/Doğukan/OneDrive/Masaüstü/muzik.m4a", format="m4a")

# WAV formatına dönüştür
song.export("C:/Users/Doğukan/OneDrive/Masaüstü/muzik.wav", format="wav")

pygame.mixer.init()
pygame.mixer.music.load("C:/Users/Doğukan/OneDrive/Masaüstü/muzik.wav")
pygame.mixer.music.play()

# Müziğin çalma süresi boyunca bekleyin
while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)  # Küçük bir bekleme süresi ekleyin (örneğin, 10 milisaniye)

pygame.mixer.quit()

