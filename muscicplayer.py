#Musicplayer project in Python.

#Importing Necessary Modules
import pygame
import tkinter as tkr
from tkinter.filedialog import askdirectory
import os

#creating window (interface) for player
musicplayer = tkr.Tk()

#setting dimensions of tkinter window
musicplayer.geometry('650x550')

#adding title for interface
musicplayer.title("Music Player")

#askdirectory() prompt the user to choose a directory(music directory)
directory = askdirectory()

#os.chdir() method in python is used to change the current working directory to specified path.
# It takes only a single argument as new directory path
os.chdir(directory)

#os.listdir() returns a list conatining the names of the entries in the directory given by path.
songlist = os.listdir()
playlist = tkr.Listbox(musicplayer, font ="Cambria 14 bold", bg="cyan2", selectmode = tkr.SINGLE)
for item in songlist:
    pos=0
    playlist.insert(pos, item)
    pos = pos + 1
pygame.init()
pygame.mixer.init()

def play():
    pygame.mixer.music.load(playlist.get(tkr.ACTIVE))
    var.set(playlist.get(tkr.ACTIVE))
    pygame.mixer.music.play()
    
def ExitMusicPlayer():
        pygame.mixer.music.stop()
        
def pause():
        pygame.mixer.music.pause()
        
def resume():
        pygame.mixer.music.unpause()
 
#Creating buttons
Button1 = tkr.Button(musicplayer, width=5,height=3, font="Cambria 20 bold", text="Play Music", command=play, bg="lime green", fg="black")
Button2 = tkr.Button(musicplayer, width=5, height=3, font="Cambria 20 bold", text="Stop Music", command=ExitMusicPlayer, bg="red", fg="black")
Button3 = tkr.Button(musicplayer, width=5, height=3, font="Cambria 16 bold", text="Pause Music", command=pause, bg="yellow", fg="black")
Button4 = tkr.Button(musicplayer, width=5, height=3, font="Cambria 16 bold", text="Resume Music", command=resume, bg="skyblue", fg="black")
var = tkr.StringVar()
songtitle = tkr.Label(musicplayer, font="Helvetica 12 bold", textvariable=var)
songtitle.pack()

Button1.pack(fill="x")
Button2.pack(fill="x")
Button3.pack(fill="x")
Button4.pack(fill="x")
playlist.pack(fill="both", expand="yes")
musicplayer.mainloop()