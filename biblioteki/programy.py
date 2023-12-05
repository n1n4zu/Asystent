import psutil
import os


def program(programy):
    for program in programy:
        for proc in psutil.process_iter(['pid', 'name']):
            if program.lower() in proc.info['name'].lower():
                try:
                    os.kill(proc.info['pid'], 9)
                    print(f"Zamknięto {proc.info['name']} (PID: {proc.info['pid']})")
                except PermissionError as e:
                    print(e)