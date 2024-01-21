from tkinter import filedialog
from tkinter import *
from PIL import Image, ImageTk
import pygame
import os

root = Tk()
root.title('Dodo Music Player')
root.geometry('500x300')

pygame.mixer.init()

menubar = Menu(root)
root.config(menu=menubar)

songs = []
current_song = ""
paused = False

def load_music():
    global current_song
    root.directory = filedialog.askdirectory()

    for song in os.listdir(root.directory):
        name, ext = os.path.splitext(song)
        if ext == '.mp3':
            songs.append(song)
            songlist.insert(END, song)

    for song in songs:
        songlist.insert(END, song)

    songlist.selection_set(0)
    current_song = songs[songlist.curselection()[0]]

def play_music():
    global current_song, paused

    if not paused:
        pygame.mixer.music.load(os.path.join(root.directory, current_song))
        pygame.mixer.music.play()
        print('Müzik oynatılıyor...')
    else:
        pygame.mixer.music.unpause()
        paused = False
        print('Müzik devam ediyor...')


def pause_music():
    global paused
    paused = True
    pygame.mixer.music.pause()
    print('Müzik duraklatıldı.')

def next_music():
    global current_song, paused

    try:
        songlist.selection_clear(0, END)
        songlist.selection_set(songs.index(current_song) + 1)
        current_song = songs[songlist.curselection()[0]]
        play_music()
    except:
        pass

def previous_music():
    global current_song, paused

    try:
        songlist.selection_clear(0, END)
        songlist.selection_set(songs.index(current_song) - 1)
        current_song = songs[songlist.curselection()[0]]
        play_music()
    except:
        pass

organise_menu = Menu(menubar, tearoff=False)
organise_menu.add_command(label="Dosya Seç", command=load_music)
menubar.add_cascade(label="Organize", menu=organise_menu)

songlist = Listbox(root, bg="black", fg="white", width=100, height=15)
songlist.pack()

control_frame = Frame(root)
control_frame.pack()

play_btn_image = ImageTk.PhotoImage(Image.open("play.png").resize((32, 32)))
pause_btn_image = ImageTk.PhotoImage(Image.open("pause.png").resize((32, 32)))
previous_btn_image = ImageTk.PhotoImage(Image.open("previous.png").resize((32, 32)))
next_btn_image = ImageTk.PhotoImage(Image.open("next.png").resize((32, 32)))

play_btn = Button(control_frame, image=play_btn_image, borderwidth=2, command=play_music, bg = "green", fg = "white")
pause_btn = Button(control_frame, image=pause_btn_image, borderwidth=2, command=pause_music)
previous_btn = Button(control_frame, image=previous_btn_image, borderwidth=2, command=previous_music)
next_btn = Button(control_frame, image=next_btn_image, borderwidth=2, command=next_music)

play_btn.image = play_btn_image
pause_btn.image = pause_btn_image
previous_btn.image = previous_btn_image
next_btn.image = next_btn_image

play_btn.grid(row=0, column=1, padx=7, pady=10)
pause_btn.grid(row=0, column=2, padx=7, pady=10)
previous_btn.grid(row=0, column=0, padx=7, pady=10)
next_btn.grid(row=0, column=3, padx=7, pady=10)

root.mainloop()
