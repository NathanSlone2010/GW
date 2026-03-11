import time
import sys
import os
import random
import platform
#REQUIRED MODULES


time.sleep(1); print("N0 ERRORS FOUND")

current_os = platform.system()
if current_os == "Windows":
	print("WINDOWS OPERATING SYSTEM")
elif current_os == "PLACEHOLFER":
	print("MAC OPERATING SYSTEM")
elif current_os == "iOS":
	print("iOS DETECTED... WELCOME, MOBILE")
elif current_os in ["NetBSD", "FreeBSD", "OpenBSD"]:
	print("BSD OPERATING SYSTEM")
elif current_os == "Linux":
	print("LINUX KERNEL BASED OPERATING SYSTEM")
elif current_os not in ["Windows", "iOS", "NetBSD", "FreeBSD", "OpenBSD", "Linux"]:
	print("UNKNOWN OPERATING SYSTEM. REPORT OS TO DEV FOR INTEGRATION.")


time.sleep(0.5); print("\nSTART GAME? Y/N")
startg = input("[INPUT] ").upper()
#ALLOWS USER TO CHOOSE TO START OR NOT


if startg == "N":
	time.sleep(0.5); print("RETURN WHEN YOU ARE READY.")
	sys.exit()

if startg not in ["Y", "N"]:
	print("INVALID, ASSUMING PLAYER IS READY")
#STARTS THE PROGRAM


print("THE GREAT WAR, Version 01.00.00")
print("VOID STUDIOS COPYRIGHT 2026")
print("WELCOME TO THE LAND OF ZABEROTH, SOLDIER.")

health = 150
damage = 25
soldier_health = 100
general_health = 150
boss_health = 155
king_health = 200
queen_health = 200
royalguard_health = 50
grunt_health = 20


print(f"\nHere are your statistics, soldier! HEALTH: {health} | DAMAGE: {damage}")
print("Would you like the enemy statistics? Y/N")
statg = input("[INPUT] ").upper()

if statg == "Y":
	print(f"\nSOLDIER HEALTH: {soldier_health} | GENERAL HEALTH: {general_health} | BOSS HEALTH: {boss_health} | KING HEALTH: {king_health} | QUEEN HEALTH: {queen_health} | ROYAL GUARD HEALTH: {royalguard_health} | GRUNT HEALTH: {grunt_health}\n")
if statg == "N":
	print("\nAlright then...\n")
if statg not in ["Y", "N"]:
	print("\nASSUMING NO, THEN?")
