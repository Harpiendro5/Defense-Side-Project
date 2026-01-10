import time
import loading_animation as animation


def mac_terminal():
  GREEN = animation.GREEN
  RED = animation.RED
  DARK_RED = animation.DARK_RED
  ROYAL_BLUE = animation.ROYAL_BLUE
  RESET = animation.RESET

  print(f'{GREEN}This tool is desgined for Windows, you are using this on mac and may be limited due to OS Restrictions.{RESET}')
  time.sleep(0.65)
  print(f'{GREEN}Strongly intended and designed for defense monitoring and system health. {RESET}')
  time.sleep(1.25)
  print(f"{ROYAL_BLUE}For help type 'help' and to exit type 'exit':{RESET}")
  time.sleep(.5)

  while True:
    try:
      option = input()
    except KeyboardInterrupt:
      print(f"\m{DARK_RED}")
