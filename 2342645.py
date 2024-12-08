import os
import socket
import datetime
from netmiko import ConnectHandler
import requests

remote_device = {
    'device_type': 'linux',
    'host': '192.168.56.101',
    'username': 'hetu2',
    'password': 'Dexter@148',
}

def show_date_time():
    print("Local Date and Time:", datetime.datetime.now())

def show_ip_address():
    try:
        hostname = socket.gethostname()
        
        ip_address = socket.gethostbyname_ex(hostname)[2][0]
        print("Local IP Address:", ip_address)
    except Exception as e:
        print("Error getting IP address:", e)

def show_remote_home_directory():
    try:
        connection = ConnectHandler(**remote_device)
        output = connection.send_command('ls ~')
        print("Remote Home Directory Listing:\n", output)
        connection.disconnect()
    except Exception as e:
        print(f"Error connecting to remote device: {str(e)}")

def backup_remote_file():
    remote_path = input("Enter full path of remote file to backup: ")
    try:
        connection = ConnectHandler(**remote_device)
        backup_command = f'cp {remote_path} {remote_path}.old'
        connection.send_command(backup_command)
        print("Backup created successfully.")
        connection.disconnect()
    except Exception as e:
        print(f"Error during backup: {str(e)}")

def save_web_page():
    url = input("Enter the full URL of the webpage: ")
    try:
        response = requests.get(url)
        if response.status_code == 200:
            filename = "webpage_backup.html"
            with open(filename, 'w', encoding='utf-8') as file:
                file.write(response.text)
            print(f"Webpage saved as {filename}")
        else:
            print("Failed to retrieve webpage. Status code:", response.status_code)
    except Exception as e:
        print(f"Error saving webpage: {str(e)}")

def main():
    while True:
        print("\nMenu:")
        print("1 - Show date and time (local computer)")
        print("2 - Show IP address (local computer)")
        print("3 - Show Remote home directory listing")
        print("4 - Backup remote file")
        print("5 - Save web page")
        print("Q - Quit")

        choice = input("Enter your choice: ").strip().upper()

        if choice == '1':
            show_date_time()
        elif choice == '2':
            show_ip_address()
        elif choice == '3':
            show_remote_home_directory()
        elif choice == '4':
            backup_remote_file()
        elif choice == '5':
            save_web_page()
        elif choice == 'Q':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
