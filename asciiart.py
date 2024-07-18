#   _____ _____   _____ _      _____ 
#  / ____|  __ \ / ____| |    |_   _|
# | |    | |__) | |    | |      | |  
# | |    |  _  /| |    | |      | |  
# | |____| | \ \| |____| |____ _| |_ 
#  \_____|_|  \_\\_____|______|_____|
#
# Cyberpunk: RED CLI Character Manager
# by nowherekydd // v0d
# ASCII Holder

import txtfrm

def mainheader():
    print(r"""
       ______      __                                __        ____  __________ 
      / ____/_  __/ /_  ___  _________  __  ______  / /___    / __ \/ ____/ __ \
     / /   / / / / __ \/ _ \/ ___/ __ \/ / / / __ \/ //_(_)  / /_/ / __/ / / / /
    / /___/ /_/ / /_/ /  __/ /  / /_/ / /_/ / / / / ,< _    / _, _/ /___/ /_/ / 
    \____/\__, /_.___/\___/_/  / .___/\__,_/_/ /_/_/|_(_)  /_/ |_/_____/_____/  
         /____/               /_/                                               

          Python-based CLI Character Sheet/Roller by nowherekydd // v0d
""")

def charheaderdiv():
    print(txtfrm.bgblack(r"                                                                                      "))

def charsheetheader():
    print(txtfrm.bgblack(txtfrm.cred(r"""                                                                                      
       ______      __                                __        ____  __________       
      / ____/_  __/ /_  ___  _________  __  ______  / /___    / __ \/ ____/ __ \      
     / /   / / / / __ \/ _ \/ ___/ __ \/ / / / __ \/ //_(_)  / /_/ / __/ / / / /      
    / /___/ /_/ / /_/ /  __/ /  / /_/ / /_/ / / / / ,< _    / _, _/ /___/ /_/ /       
    \____/\__, /_.___/\___/_/  / .___/\__,_/_/ /_/_/|_(_)  /_/ |_/_____/_____/        
         /____/               /_/                                                     """)))

def charsheetdiv():
    chardiv = "▬▬ι═════════════════════════════════════════ι▬▬"
    chardCenter = chardiv.center(82)
    print(chardCenter)