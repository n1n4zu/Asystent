import os
import platform
import psutil


def zamknij():
    PROGRAMY = ['pycharm64.exe', 'cmd.exe', 'asystent.exe', 'terminal', 'pycharm64']
    if platform.system() == "Windows":
        os.system('shutdown /s /t 10')
        for program in PROGRAMY:
            for proc in psutil.process_iter(['pid', 'name']):
                if program.lower() in proc.info['name'].lower():
                    try:
                        os.kill(proc.info['pid'], 9)
                        print(f"Zamknięto {proc.info['name']} (PID: {proc.info['pid']})")
                    except PermissionError as e:
                        print(e)

    elif platform.system() == "Linux":
        os.system('poweroff')
        for program in PROGRAMY:
            for proc in psutil.process_iter(['pid', 'name']):
                if program.lower() in proc.info['name'].lower():
                    try:
                        os.kill(proc.info['pid'], 9)
                        print(f"Zamknięto {proc.info['name']} (PID: {proc.info['pid']})")
                    except PermissionError as e:
                        print(e)
