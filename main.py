# Launch in its own terminal windows only
import os
import sys
import platform
import subprocess
import psutil
import time
import random
import loading_animations as animation


OS = platform.system()


if OS == "Windows" and not os.environ.get("MY_TOOL_CONSOLE"):
	script = os.path.abspath(__file__)
	python_exe = sys.executable

	cmd = (
		f'start "Sentinel" cmd /c "set MY_TOOL_CONSOLE=1 && '
		f'"{python_exe}" "{script}"'
		f'"'
	)

	subprocess.Popen(cmd, shell=True)
	sys.exit()

elif OS == "Darwin" and not os.environ.get("MY_TOOL_CONSOLE"):
	script = os.path.abspath(__file__)
	subprocess.Popen([
		"osascript", "-e",
		f'tell application "Terminal" to do script "export MY_TOOL_CONSOLE=1; python3 {script}"'
	])
	sys.exit()


GREEN = animation.GREEN
RED = animation.RED
DARK_RED = animation.DARK_RED
ROYAL_BLUE = animation.ROYAL_BLUE
RESET = animation.RESET

print(f'{GREEN}This tool is designed for windows defense monitoring and system health console.{RESET}')
time.sleep(1.25)
print(f"{ROYAL_BLUE}For help type 'help' and to exit type 'exit':{RESET}")
time.sleep(0.5)


while True:
	try:
		option = input("S> ").strip().lower()

		if option == "help":
			print(f"""{RED}List of Commands:
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
env - Show environment variables
temps - Show CPU temperature
firewall - Show firewall status
users - List local system users
system monitor - Start real time system monitoring and detect anomalies{RESET}""")

		elif option == "abort":
			sys.exit()

		elif option == "exit":
			print(f"{DARK_RED}Exiting...{RESET}")
			time.sleep(0.7)
			sys.exit()

		elif option == "ls" or option == "dir":
			try:
				for f in os.listdir(os.getcwd()):
					print(f)
			except Exception as e:
				print(f"{RED}Error listing files: {e}{RESET}")

		elif option == "start":
			print("initiation requested")
			time.sleep(0.7)
			if random.randint(0, 30) == 20:
				print(f"{DARK_RED}Initiation denied. System resources unavailable.{RESET}")
			else:
				print(f"{GREEN}Initiation accepted{RESET}")
				animation.summon_loading_bar()

		elif option == "ports":
			if OS == "Windows":
				print(subprocess.getoutput("netstat -an"))
			else:
				print(subprocess.getoutput("lsof -i -P -n | head -50"))

		elif option == "health":
			try:
				cpu = psutil.cpu_percent(interval=1)
				ram = psutil.virtual_memory()
				disk = psutil.disk_usage("C:\\")

				if cpu > 80:
					print(f"{DARK_RED}System Health, CPU Surge Detected: {cpu}%{RESET}")
				else:
					print(f"{GREEN}System Health:{RESET}")

				print(f"CPU Usage: {cpu}%")
				print(f"RAM Usage: {ram.percent}%")
				print(f"Disk Usage: {disk.percent}%")

			except Exception as e:
				print(f"{RED}Health check failed: {e}{RESET}")

		elif option == "processes":
			for proc in psutil.process_iter(['pid', 'name', 'username']):
				try:
					print(proc.info)
				except (psutil.NoSuchProcess, psutil.AccessDenied):
					pass

		elif option == "netinfo":
			if OS == "Windows":
				os.system("ipconfig")
			elif OS == "Darwin":
				os.system("ifconfig")
			else:
				os.system("ip addr")

		elif option == "hostname":
			print(f"Hostname: {platform.node()}")

		elif option == "temps":
			if OS == "Darwin":
				print(f"{RED}macOS does not expose temperature sensors.{RESET}")
			else:
				temps = psutil.sensors_temperatures()
				if not temps:
					print(f"{RED}No temperature sensors detected.{RESET}")
				for name, entries in temps.items():
					print(f"{ROYAL_BLUE}{name}{RESET}")
					for entry in entries:
						print(f"  {entry.label or 'Sensor'}: {entry.current}°C")

		elif option == "users":
			print(subprocess.getoutput("query user"))

		elif option == "clear" or option == "cls":
			os.system("cls" if OS == "Windows" else "clear")

		else:
			print(f"{RED}Unknown command. Type 'help' for a list of commands.{RESET}")

	except KeyboardInterrupt:
		print(f"\n{DARK_RED}Interrupted. Use 'exit' to quit.{RESET}")
