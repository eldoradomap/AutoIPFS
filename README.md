# Local File Monitor and IPFS Uploader using QuickNode

This project includes a Python script that monitors a specified file for changes and uploads it to a server using an API key. The script uses Tkinter to provide an extremely basic graphical user interface (GUI) for user input.

## Features

- **File Change Monitoring**: Automatically detects changes in the specified file by calculating its hash at regular intervals.

- **File Upload**: On detecting a file change, the script uploads the file to a predefined server endpoint using an API key for authentication.

- **Tkinter GUI**: Simple and user-friendly GUI for inputting the file path and API key.

- **CID Retrieval and Blockchain Integration**: After uploading the file, the script retrieves the Content Identifier (CID) from IPFS. This CID can be integrated into a smart contract to store the IPFS address of the uploaded file on a blockchain by storing the hash of the CID, enabling decentralized and tamper-proof record-keeping.

## Capabilities 

- **File Size**: Dependent upon your QuickNode plan

## QuickNode Compatibility

This script is specifically designed for use with QuickNode's IPFS service. It follows the guidelines and specifications provided in QuickNode's API documentation to ensure seamless file uploads. Please note that this script may not be compatible with other IPFS providers without modifications. If you don't have a QuickNode account, you can create one at https://www.quicknode.com/

## Prerequisites

Before running this script, ensure that you have Python3.11^ installed on your system. The script has been tested on Python 3.11

Additionally, the `requests` library is required for HTTP requests. This can be installed using pip:

```bash
pip install requests
```
Tkinter is used for the GUI, which usually comes bundled with Python. If it's not present, install it from https://docs.python.org/3/library/tkinter.html

## Workflow

- **Start the Program**: Run the script to launch the GUI.

- **Input File Path**: Enter the full path of the file you wish to monitor, including its extension.

- **Enter API Key**: Provide your QuickNode API key when prompted.

- **Enter New Name For File**: Type a name for the file, this is what the file will be named in the QuickNode GUI. (Currently, to change the name of the file a new instance of the script would have to be ran.)

- **Monitoring in Action**: The program will now monitor the specified file. It will remain idle until the file is modified and saved.

- **Automatic Upload and Notification**: Once you save changes to the file, the script automatically uploads it to QuickNode's IPFS service. A notification window then confirms the successful upload and displays the CID of the uploaded file.

- **Repeat Monitoring and Automatic Upload**: The file will continue to be re-uploaded to IPFS after every saved change until the program is killed. A notification window will confirm each successful upload and display the CID.

## License

This project is licensed under the MIT License.
