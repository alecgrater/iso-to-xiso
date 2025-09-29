# ISO to XISO Converter

A simple Python GUI application for converting standard ISO files to XISO format, specifically designed for use with Xbox emulators like Xemu.

## Overview

This tool provides an easy-to-use graphical interface for converting ISO files to the XISO format required by Xbox emulators. It uses the `extract-xiso` command-line tool under the hood to perform the actual conversion process.

## Features

- **Simple GUI Interface**: User-friendly tkinter-based interface
- **File Browser**: Easy file selection with built-in file dialog
- **Automatic Conversion**: One-click conversion from ISO to XISO format
- **Error Handling**: Clear error messages and success notifications
- **Clean Output**: Automatically removes temporary files after conversion

## Requirements

- Python 3.x with tkinter support
- Windows operating system (due to included `extract-xiso.exe`)
- The included `extract-xiso.exe` binary

## Installation

1. Clone or download this repository
2. Ensure Python 3.x is installed on your system
3. No additional Python packages are required (uses only standard library)

## Usage

### Quick Start

1. Run the application:
   ```bash
   python app.py
   ```

2. Click "Browse" to select your ISO file

3. Click "Convert" to start the conversion process

4. The converted XISO file will be created in the same directory as the original ISO

### Detailed Process

The conversion process performs the following steps:
1. Extracts the contents of the ISO file
2. Renames the extracted folder with "xiso" suffix
3. Repackages the contents into XISO format
4. Cleans up temporary files
5. Removes the original ISO file

## File Structure

```
iso-to-xiso/
├── app.py              # Main GUI application
├── extract-xiso.exe    # Command-line conversion tool
└── README.md          # This file
```

## Technical Details

- **GUI Framework**: tkinter (Python standard library)
- **Conversion Tool**: extract-xiso (originally from [XboxDev/extract-xiso](https://github.com/XboxDev/extract-xiso))
- **Supported Formats**: Input: `.iso` files, Output: `.xiso` files
- **Platform**: Windows (due to included .exe binary)

## Xbox Emulation

The converted XISO files are compatible with Xbox emulators such as:
- **Xemu**: Modern, accurate Xbox emulator
- **CXBX-Reloaded**: Xbox emulator for Windows
- Other emulators that support XISO format

## Troubleshooting

### Common Issues

- **"Invalid file format" error**: Ensure you're selecting a `.iso` file
- **Conversion failed**: Check that the ISO file isn't corrupted and you have write permissions in the target directory
- **Missing extract-xiso.exe**: Ensure the `extract-xiso.exe` file is in the same directory as `app.py`

### Error Messages

The application provides clear error messages for common issues:
- File format validation
- Conversion process errors
- File system permission issues

## Credits

- **extract-xiso tool**: Originally developed by the XboxDev community
- **Source**: [https://github.com/XboxDev/extract-xiso](https://github.com/XboxDev/extract-xiso)

## License

This project uses the extract-xiso tool which has its own licensing terms. Please refer to the original project for licensing information.

## Contributing

Feel free to submit issues, feature requests, or pull requests to improve this tool.
