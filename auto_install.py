#!/usr/bin/env python3
"""
Auto Install Script

This script automatically detects missing Python modules and installs them
via pip. It restarts the target script after installing dependencies.

Usage:
    python auto_install.py your_script.py [args...]

Requirements:
    Python 3.8 or higher
"""

import sys
import subprocess
import os
from typing import List, Optional


def main() -> None:
    """
    Main function to handle auto-installation of missing Python modules.

    This function attempts to run a target script and automatically installs
    any missing dependencies through pip when ModuleNotFoundError is caught.
    """
    if len(sys.argv) < 2:
        print("Usage: python auto_install.py your_script.py [args...]")
        return

    target_script: str = sys.argv[1]
    script_args: List[str] = sys.argv[2:]

    while True:
        try:
            subprocess.check_call(
                [sys.executable, target_script] + script_args
            )
            print("\nAll dependencies have been successfully installed!")
            break
        except subprocess.CalledProcessError as e:
            print(f"Error running the script: {e}")
            return
        except subprocess.SubprocessError as e:
            print(f"Subprocess error: {e}")
            return
        except ModuleNotFoundError as e:
            module_name: Optional[str] = e.name
            if not module_name:
                print("Unknown module error occurred")
                return

            print(f"\nMissing module detected: {module_name}")
            response = input(
                f"Do you want to install '{module_name}' via pip? [Y/n] "
            ).lower()
            if response in ["", "y", "yes"]:
                try:
                    # Use --user flag for safer installation
                    subprocess.check_call(
                        [
                            sys.executable,
                            "-m",
                            "pip",
                            "install",
                            "--user",
                            module_name,
                        ]
                    )
                    print(f"{module_name} installed successfully.")
                except subprocess.CalledProcessError as e:
                    print(f"Failed to install {module_name}. Error: {e}")
                    continue
            else:
                print("Installation canceled.")
                return

            print("Restarting to apply changes...")
            os.execv(sys.executable, [sys.executable] + sys.argv)


if __name__ == "__main__":
    main()
