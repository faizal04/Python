# import pandas as pd
import pygame
import os
import random

pygame.mixer.init()

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

class Valorant:
    def __init__(self,name,ability):
        self.name = name
        self.ability = ability
        self.voice_lines ={
            "viper": ['voices/viper1.mpeg'],
            "reyna":['voices/reyna1.mpeg'],
            "omen":['voices/omen1.mpeg']
        }

    def __str__(self):
        return f"Name:{self.name} | Ability:{self.ability}"
        
    def voice(self):
        if(self.name in self.voice_lines):
            files = self.voice_lines[self.name]
            chosen = files[0]
            pygame.mixer.music.load(os.path.join(SCRIPT_DIR, chosen))
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy():
                continue
        else:
            print(f"No voice lines for {self.name}")

viper = Valorant("viper","poison")
print(viper)
# viper.voice()
reyna = Valorant("reyna","empress")
reyna.voice()
omen = Valorant('omen',"Teleport")
# omen.voice()