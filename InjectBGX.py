from pymem import *

pm: Pymem = Pymem("League of Legends.exe")

# Offsets for League of Legends 13.5
of_localPlayer = 0x3172ABC
of_playerName = 0x54

if pm:
    base = pm.process_base.lpBaseOfDll
    localplayer = pm.read_int(base + of_localPlayer)
    nameAdress = pm.read_int(localplayer + of_playerName)
    pm.write_string(nameAdress, "L9 Lover\0")
