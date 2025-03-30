# Auto Install Script

This project contains a Python script (`auto_install.py`) that helps you automatically install missing dependencies for your Python scripts. It detects missing modules, prompts the user to install them, and restarts the script to apply changes.

## Features

- Automatically detects missing Python modules.
- Prompts the user to install missing modules via `pip`.
- Restarts the target script after installing dependencies.

## Usage

1. Place the `auto_install.py` script in the same directory as your target Python script.
2. Run the `auto_install.py` script with the following command:

    ```bash
    python auto_install.py your_script.py [args...]
    ```

    Replace `your_script.py` with the name of the Python script you want to run, and `[args...]` with any arguments required by your script.

3. If a missing module is detected, the script will prompt you to install it. You can confirm by typing `Y` or cancel by typing `N`.

## Example

Suppose you have a script named `example.py` that requires the `requests` module. Run the following command:

```bash
python auto_install.py example.py
```

If the `requests` module is not installed, the script will prompt:

```
Missing module detected: requests
Do you want to install 'requests' via pip? [Y/n]
```

Type `Y` to install the module, and the script will restart `example.py` automatically.

## Requirements

- Python 3.6 or higher
- `pip` installed and configured

## Notes

- Ensure you have an active internet connection to install dependencies.
- The script will restart itself after installing missing modules, so any unsaved changes in your environment may be lost.

## License

This project is licensed under the MIT License. See the LICENSE file for details. [![GitHub License](https://img.shields.io/github/license/mr0miner/Auto-Install-Script)](https://github.com/mr0miner/Auto-Install-Script/blob/main/LICENSE)

## Related Documentation

For the Persian version of this README, refer to [README fa.md](./README%20fa.md).