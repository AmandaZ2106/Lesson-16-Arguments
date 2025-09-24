import os
import platform

def shutdown():
    system_platform = platform.system()

    if system_platform == "Windows":
        os.system("shutdown /s /t 1")  # shuts down immediately
    elif system_platform == "Linux" or system_platform == "Darwin":  # Darwin = macOS
        os.system("sudo shutdown -h now")
    else:
        print("Unsupported operating system")

if __name__ == "__main__":
    shutdown()