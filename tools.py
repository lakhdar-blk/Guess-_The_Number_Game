from pygame import mixer
import random

mixer.init()

def play_music():
    
    mixer.music.load("btsn.wav")
    mixer.music.play()

def play_music2():
    
    mixer.music.load("error.wav")
    mixer.music.play()

def play_music3():
    
    mixer.music.load("suc.mp3")
    mixer.music.play()
    
def play_music4():
    
    mixer.music.load("lose.wav")
    mixer.music.play()

def check_entry(entry):

    if entry.isdigit():
        return True
    else:
        return False

def generate_number(range):

    if range == 1:
        return random.randint(1, 10)
    elif range == 2:
        return random.randint(1, 100)
    elif range == 3:
        return random.randint(1, 1000)

