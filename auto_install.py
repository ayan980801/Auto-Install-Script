import sys
import subprocess
import os

def main():
    if len(sys.argv) < 2:
        print("Usage: python auto_install.py your_script.py [args...]")
        return

    target_script = sys.argv[1]
    script_args = sys.argv[2:]

    while True:
        try:
            subprocess.check_call([sys.executable, target_script] + script_args)
            print("\nAll dependencies have been successfully installed!")
            break
        except subprocess.CalledProcessError as e:
            print(f"Error running the script: {e}")
            return
        except subprocess.SubprocessError as e:
            print(f"Subprocess error: {e}")
            return
        except ModuleNotFoundError as e:
            module_name = e.name
            print(f"\nMissing module detected: {module_name}")
            response = input(f"Do you want to install '{module_name}' via pip? [Y/n] ").lower()
            if response in ['', 'y', 'yes']:
                try:
                    subprocess.check_call([sys.executable, '-m', 'pip', 'install', module_name])
                    print(f"{module_name} installed successfully.")
                except subprocess.CalledProcessError as e:
                    print(f"Failed to install {module_name}. Error: {e}")
                    continue
            else:
                print("Installation canceled.")
            
            print("Restarting to apply changes...")
            os.execv(sys.executable, [sys.executable] + sys.argv)

if __name__ == "__main__":
    main()