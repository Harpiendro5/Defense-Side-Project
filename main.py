import os
import sys
import platform
import subprocess
import time
import random
import loading_animations as animation


def mac_terminal():
	GREEN = animation.GREEN
	RED = animation.RED
	DARK_RED = animation.DARK_RED
	ROYAL_BLUE = animation.ROYAL_BLUE
	RESET = animation.RESET

	print(f'{GREEN}This tool is designed for Windows, you are using this on mac and may be limited due to OS Restrictions.{RESET}')
	time.sleep(0.65)
	print(f'{GREEN}Strongly intended and designed for defense monitoring and system health. {RESET}')
	time.sleep(1.25)
	print(f"{ROYAL_BLUE}For help type 'help' and to exit type 'exit':{RESET}")
	time.sleep(0.5)

	while True:
		try:
			option = input("S(mac)> ").strip().lower()

			if option == "help":
				print(f"""{RED}List of Commands (mac):
abort - Exit immediately
exit - Exit the program
ls/dir - List files in current directory
start - Start process or Start system monitoring
ports - Show open network ports
health - Show system health status
processes - List running processes
integ - Run system integrity checks
netinfo - Show network information
hostname - Show machine hostname
users - List local system users{RESET}""")

			if option == "exit":
				print(f"{DARK_RED}Exiting...{RESET}")
				time.sleep(0.5)
				sys.exit()

			if option == "abort":
				sys.exit()

			if option == "ls" or option == "dir":
				try:
					for f in os.listdir():
						print(f)
				except Exception as e:
					print(f"{RED}Error listing directory: {e}{RESET}")

			if option == "ports":
				# Mac-os specific
				print(subprocess.getoutput("lsof -i -P -n | head -50"))

			if option == "netinfo":
				os.system("ifconfig")

			if option == "hostname":
				print(platform.node())

			if option == "users":
				print(subprocess.getoutput("who"))

			if option == "load":
				# Mac-os load average (1, 5, 15 min)
				print(subprocess.getoutput("uptime"))

			if option == "processes":
				print(subprocess.getoutput("ps -axo pid,comm,%cpu,%mem | head -20"))

			if option == "start":
				print("Initianton requested")
				time.sleep(0.7)
				if random.randint(0, 30) == 20:
					print(f"{DARK_RED}Initiation denied. System resources unavailable.{RESET}")
				else:
					print(f"{GREEN}Initiation accepted{RESET}")
					animation.summon_loading_bar()

			else:
				print(f"{RED}Unknown command. Type 'help' for a list of commands.{RESET}")

		except KeyboardInterrupt:
			print(f"\n{DARK_RED}Interrupted, use 'exit' to quit.{RESET}")
