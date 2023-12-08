import tkinter as tk
from tkinter import simpledialog, messagebox
import threading
import requests
import hashlib
import time
import json

def calculate_hash(file_path):
    """
    Calculate the SHA256 hash of a file.

    Args:
    file_path (str): The path of the file whose hash is to be calculated.

    Returns:
    str: The calculated SHA256 hash in hexadecimal format.
    """
    sha256_hash = hashlib.sha256()
    with open(file_path, "rb") as f:
        # Read and update hash in chunks of 4K for efficiency
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
    return sha256_hash.hexdigest()

def upload_file(file_path, api_key, gui_name, callback):
    """
    Upload a file to the server.

    Args:
    file_path (str): The path of the file to be uploaded.
    api_key (str): API key for authentication.
    gui_name (str): The name to be displayed on the QuickNode GUI.
    """
    url = "https://api.quicknode.com/ipfs/rest/v1/s3/put-object"
    payload = {'Key': gui_name, 'ContentType': 'text'}  # Use gui_name for the Key
    files = [('Body', (gui_name, open(file_path, 'rb'), 'text/html'))]  # Use gui_name for the file name
    headers = {'x-api-key': api_key}

    try:
        # Attempt to upload the file and raise an error if the response is an error
        response = requests.post(url, headers=headers, data=payload, files=files)
        response.raise_for_status()  # Raises an HTTPError if the response was an error
        response_dict = json.loads(response.text)
        cid = response_dict['pin']['cid']
        print("Upload successful, CID:", cid)
        callback(cid)  # Call the callback function with the CID

    except requests.exceptions.RequestException as e:
        # Handle exceptions during the upload process
        print("Error during upload:", e)
        callback(None, e)  # Call the callback with an error

def monitor_and_upload(file_path, api_key, gui_name, interval=10, callback=None):
    last_hash = None
    while True:
        current_hash = calculate_hash(file_path)
        if last_hash is not None and current_hash != last_hash:
            print("File has changed, uploading...")
            upload_file(file_path, api_key, gui_name, callback)  # Pass gui_name to the upload function
        else:
            print("File has not changed or is the first run, skipping upload.")
        last_hash = current_hash
        time.sleep(interval)

def update_gui_with_cid(cid, error=None):
    # Update the GUI with the CID or an error message
    if cid:
        messagebox.showinfo("Upload Successful", f"File uploaded successfully!\nCID: {cid}")
    elif error:
        messagebox.showerror("Upload Error", f"Error during file upload: {error}")

def main():
    root = tk.Tk()
    root.withdraw()  # Hide the main window

    file_path = simpledialog.askstring("Input", "Enter the file path:")
    api_key = simpledialog.askstring("Input", "Enter the API key:")
    gui_name = simpledialog.askstring("Input", "Enter the name for the file to be uploaded as:")

    if file_path and api_key and gui_name:
        thread = threading.Thread(target=monitor_and_upload, args=(file_path, api_key, gui_name, 10, update_gui_with_cid))
        thread.daemon = True
        thread.start()
    else:
        print("File path, API key, or new name for file not provided. Exiting.")
        root.destroy()
        return

    root.mainloop()

if __name__ == "__main__":
    main()