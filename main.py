# Launch in its own terminal windows only
import os
import sys
import platform
import subprocess
import psutil
import time
import random
import loading_animation as animation

if platform.system() == "Windows" and not os.environ.get("MY_TOOL_CONSOLE"):
	script = os.path.abspath(__file__)
	python_exe = sys.executable

	cmd = (
		f'start "Sentinel" cmd /c "set MY_TOOL_CONSOLE=1 && '
		f'"{python_exe}" "{script}"'
		f'"'
	)

	subprocess.Popen(cmd, shell=True)
	sys.exit()

GREEN = animation.GREEN
RED = animation.RED
DARK_RED = animation.DARK_RED
ROYAL_BLUE = animation.ROYAL_BLUE
RESET = animation.RESET
DOWN = animation.DOWN
UP = animation.UP
CLEAR = animation.CLEAR

print(f'{GREEN}This tool is designed for windows defense monitoring and system health console.{RESET}')
time.sleep(1.25)
print(f"{ROYAL_BLUE}For help type 'help' and to exit type 'exit':{RESET}")
time.sleep(.5)

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
				files = os.listdir(os.getcwd())
				print(f"{ROYAL_BLUE}-----{RESET}")
				for f in files:
					if f == "ideas.txt":
						continue
					else:
						print(f)
				print(f"{ROYAL_BLUE}-----{RESET}")
			except Exception as e:
				print(f"{RED}Error listing files: {e}{RESET}")
		
		elif option == "start":
			print(f"initiation requested")
			time.sleep(.7)
			if random.randint(0, 30) == 20:
				print(f"{DARK_RED}Initiation denied. System resources unavailable.{RESET}")
				continue
			else:
				print(f"{GREEN}Initiation accepted{RESET}")
				time.sleep(.25)
				animation.summon_loading_bar()
			
		elif option == "ports":
			netstat = subprocess.getoutput("netstat -an")
			print(netstat)
		
		elif option == "health":
			try:
				cpu = psutil.cpu_percent(interval=1)
				ram = psutil.virtual_memory()
				disk = psutil.disk_usage('C:\\')

				if cpu > 80:
					print(f"{DARK_RED}System Health, CPU Surge Detected: {cpu}%{RESET}")
				else:
					print(f"{GREEN}System Health:{RESET}")
				
				print(f"CPU Usage: {cpu}%")
				print(f"RAM Usage: {ram.percent}% ({ram.used // (1024 ** 2)} MB / {ram.total // (1024 ** 2)} MB)`")
				print(f"Disk/NVMe Usage: {disk.percent}% ({disk.used // (1024 ** 3)} GB / {disk.total // (1024 ** 3)} GB)")

			except Exception as e:
				print(f"{RED}Health check failed: {e}{RESET}")
		
		elif option == "processes":
			print(f"{RED}The formatting of this function still needs work{RESET}")
			time.sleep(2.5)
			for proc in psutil.process_iter(['pid', 'name', 'username']):
				try:
					# Grab details as a dictionary
					print(proc.info)
				except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
					pass
			pass
		
		elif option == "integ":
			print(f"{RED}This function is currently under construction.{RESET}")
			# Run system integrity checks and detect file changes
			pass

		elif option == "admin integ":
			print(f"{RED}This function is currently under construction and needs permission.{RESET}")
			# Run advanced integrity checks on logs and FIM files
			pass
		
		elif option == "netinfo":
			def show_ip():
				os_name = platform.system()
				if os_name == "Windows":
					print("Running ipconfig")
					os.system("ipconfig")
				if os_name in ['Linux', 'Darwin']:
					print("Running ip addr")
					os.system("ip addr")
				else:
					print("Unkown OS")
			
			if __name__ == "__main__":
				show_ip()
		
		elif option == "hostname":
			print(f"Hostname: {platform.node()}")

		elif option == "env" or option == "env show":
			print(f"{RED}This function is currently under construction.{RESET}")
			# Show environment variables
			pass
		
		elif option == "temps":
			print("DEBUG: Entered temps command")
			print("DEBUG: psutil version:", psutil.__version__)
			print("DEBUG: platform:", platform.platform())

			try:
					temps = psutil.sensors_temperatures()
					print("DEBUG: Raw temps object:", temps)
					print("DEBUG: Type:", type(temps))

					if not temps:
							print(f"{RED}No system temperature sensors exposed by hardware.{RESET}")
					else:
							for name, entries in temps.items():
									print(f"{ROYAL_BLUE}{name}{RESET}")
									for entry in entries:
											print(f"  {entry.label or 'Sensor'}: {entry.current}°C")

			except Exception as e:
					import traceback
					print(f"{RED}Temperature read failed (exception raised):{RESET}")
					traceback.print_exc()
			

		elif option == "firewall":
			print(f"{RED}This function is currently under construction.{RESET}")
			# Show firewall status
			pass

		elif option == "users":
			try:
				user_output = subprocess.getoutput("query user")
				print(f"{ROYAL_BLUE}Active Users;{RESET}")
				print(user_output)
				print(f"-----------------")

			except Exception as e:
				print(f"{RED}Error retrieving users: {e}{RESET}")

		elif option == "permissions":
			print(f"{RED}This function is currently under construction.{RESET}")
			# Show permissions of a file
			pass

		elif option == "log show":
			print(f"{RED}This function is currently under construction and needs permission.{RESET}")
			# Ask for password then print Sentinels log file
			pass

		elif option == "log clear":
			"""
			STILL NEEDS FINISHING
			while True:
				
				if security:
					option = (f"{RED}Are you sure? (y/n){RESET}")
					if option == "y":
						print(f"{GREEN}Logs have been successfully cleared.{RESET}")
						pass
					if option == "n"
						continue
				else:
					password = input("Enter admin password: ").strip()
					if password == admin_password:
						option = (f"{RED}Are you sure? (y/n){RESET}")
						if option == "y":
							print(f"{GREEN}Logs have been successfully cleared.{RESET}")
							pass
						if option == "n"
							continue
					else:
						print(f"{DARK_RED}Incorrect password, 2 more attempts.{RESET}")
						continue
				   
			
			"""
			print(f"{DARK_RED}This option is currently unavailable and needs permission.{RESET}")

		elif option == "clear" or option == "cls":
			os.system("cls")
			

		elif option == "snapshot":
			print(f"{RED}This function is currently under construction.{RESET}")
			# Save current system state to a file
			pass

		elif option == "iso protocol":
			print(f"{RED}This function is currently under construction and needs permission.{RESET}")
			# Disable network interfaces (local only)
			pass

		elif option == "system monitor":
			print(f"{RED}This function is currently under construction.{RESET}")
			# Start real time monitoring of system resources and determine if there are any anomalies
			pass

		elif option == "sudo privileges":
			print(f"""{RED}These are the commands that require either sudo permission or admin password to run:
log show - View Sentinels log file
log clear - Clear sentinels log file
report backup - View the backup of the last system report and integrity check
admin integ - Run advanced integrity checks on logs and FIM files
iso protocol - Disable network interfaces and all network connections (local only){RESET}""")
		
		elif option == "report backup":
			print(f"{RED}This function is currently under construction and needs permission.{RESET}")
			# Show backup of last system report and integrity check
			pass
		
		else:
			print(f"{RED}Unknown command. Type 'help' for a list of commands.{RESET}")
			
	except KeyboardInterrupt:
		print(f"\n{DARK_RED}Interrupted. Use 'exit' to quit.{RESET}")
	