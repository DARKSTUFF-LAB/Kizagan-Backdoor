import random
import subprocess
import os
import time

yazi1 = ""

██╗░░██╗██╗███████╗░█████╗░░██████╗░░█████╗░███╗░░██╗
██║░██╔╝██║╚════██║██╔══██╗██╔════╝░██╔══██╗████╗░██║
█████═╝░██║░░███╔═╝███████║██║░░██╗░███████║██╔██╗██║
██╔═██╗░██║██╔══╝░░██╔══██║██║░░╚██╗██╔══██║██║╚████║
██║░╚██╗██║███████╗██║░░██║╚██████╔╝██║░░██║██║░╚███║
╚═╝░░╚═╝╚═╝╚══════╝╚═╝░░╚═╝░╚═════╝░╚═╝░░╚═╝╚═╝░░╚══╝"""
yazi2 = """
__  __     __     ______     ______     ______     ______     __   __    
/\ \/ /    /\ \   /\___  \   /\  __ \   /\  ___\   /\  __ \   /\ "-.\ \   
\ \  _"-.  \ \ \  \/_/  /__  \ \  __ \  \ \ \__ \  \ \  __ \  \ \ \-.  \  
 \ \_\ \_\  \ \_\   /\_____\  \ \_\ \_\  \ \_____\  \ \_\ \_\  \ \_\\"\_\ 
  \/_/\/_/   \/_/   \/_____/   \/_/\/_/   \/_____/   \/_/\/_/   \/_/ \/_/ 

        """
yazi3 = """
888    d8P  8888888 8888888888P        d8888  .d8888b.         d8888 888b    888 
888   d8P     888         d88P        d88888 d88P  Y88b       d88888 8888b   888 
888  d8P      888        d88P        d88P888 888    888      d88P888 88888b  888 
888d88K       888       d88P        d88P 888 888            d88P 888 888Y88b 888 
8888888b      888      d88P        d88P  888 888  88888    d88P  888 888 Y88b888 
888  Y88b     888     d88P        d88P   888 888    888   d88P   888 888  Y88888 
888   Y88b    888    d88P        d8888888888 Y88b  d88P  d8888888888 888   Y8888 
888    Y88b 8888888 d8888888888 d88P     888  "Y8888P88 d88P     888 888    Y888 """
yazi4 = """
  _  _______ ______         _____          _   _ 
 | |/ /_   _|___  /   /\   / ____|   /\   | \ | |
 | ' /  | |    / /   /  \ | |  __   /  \  |  \| |
 |  <   | |   / /   / /\ \| | |_ | / /\ \ | . ` |
 | . \ _| |_ / /__ / ____ \ |__| |/ ____ \| |\  |
 |_|\_\_____/_____/_/    \_\_____/_/    \_\_| \_|                                 
        """
yazi5 = """
$$\   $$\ $$$$$$\ $$$$$$$$\  $$$$$$\   $$$$$$\   $$$$$$\  $$\   $$\ 
$$ | $$  |\_$$  _|\____$$  |$$  __$$\ $$  __$$\ $$  __$$\ $$$\  $$ |
$$ |$$  /   $$ |      $$  / $$ /  $$ |$$ /  \__|$$ /  $$ |$$$$\ $$ |
$$$$$  /    $$ |     $$  /  $$$$$$$$ |$$ |$$$$\ $$$$$$$$ |$$ $$\$$ |
$$  $$<     $$ |    $$  /   $$  __$$ |$$ |\_$$ |$$  __$$ |$$ \$$$$ |
$$ |\$$\    $$ |   $$  /    $$ |  $$ |$$ |  $$ |$$ |  $$ |$$ |\$$$ |
$$ | \$$\ $$$$$$\ $$$$$$$$\ $$ |  $$ |\$$$$$$  |$$ |  $$ |$$ | \$$ |
\__|  \__|\______|\________|\__|  \__| \______/ \__|  \__|\__|  \__|


                                                                    """
yazilar = [yazi1, yazi2, yazi3, yazi4, yazi5]

os.system("clear")
print(random.choice(yazilar))
time.sleep(1)
print("\nAvrupa Hunlarının Savaş Tanrısı./God of War of the European Huns.\n")
time.sleep(1)
print("\t\t\t\t\t\tAuthor : Yiğit Aydemir\n\n\n\n")
subprocess.call(["pip","install","colorama"],shell=True)
subprocess.call(["pip","install","simplejson"],shell=True)
subprocess.call(["pip","install","datetime"],shell=True)
subprocess.call(["pip","install","tk"],shell=True)
subprocess.call(["pip","install","pynput"],shell=True)
subprocess.call(["pip","install","pyttsx3"],shell=True)
subprocess.call(["pip","install","pillow"],shell=True)
subprocess.call(["pip","install","opencv-python"],shell=True)
subprocess.call(["pip","install","pipwin"],shell=True)
subprocess.call(["pipwin","install","pyaudio"],shell=True)
subprocess.call(["pip","install","wave"],shell=True)
print("\n\n[+]Setup completed successfully./Kurulum başarıyla tamamlandı.")
exit()
