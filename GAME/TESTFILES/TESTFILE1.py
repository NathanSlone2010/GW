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


print("\n\nTHE WAR OF COLLAPSE, Version 01.01.00")
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


print("\nWhat is your desired name?")
name = input("NAME: ")

print("\nAre you ready to start the war, soldier?")
start = input("[CHOICE] ").upper()

if start == "Y":
      print("Onward, soldiers! Fight for your nation!")
if start == "N":
      print("You are not willing to fight for your nation, even though you willingly signed?! Treasonist!\n")

time.sleep(3); print("\n\n\nThrough the charge of time, our nation has done many, many thing. As a child, I used to be proud of her... No more... There is nothing of her left that is to be.")
print("\nA man walks in. 'Sir, they breached the gates. More reinforcements will pile in!'")
print(f"\n'Well, {name}, ready?")

print("1. Pick up sword")
print("2. Pick up dagger")
print("3. Pick up bow")
weapon = input("[INPUT] ")


if weapon == "1":
    time.sleep(0.5); print("You grab the sword, taking a look at it... [YOU] I am ready, Commander Newman")
if weapon == "2":
    time.sleep(0.5); print("You grab the dagger, taking it in your hand, allowing blood to come out. [YOU] Yes, sir, I am ready.")
if weapon == "3":
    time.sleep(0.5); print("You pick up the bow, grabbing the quiver alongside it. [YOU] Yes, Commander.. I am ready.")
