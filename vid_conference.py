from vidstream import *
import tkinter as tk
import socket
import threading
import requests

# Get Local & Public IP
local_ip_address = socket.gethostbyname(socket.gethostname())
public_ip_address = requests.get('https://api.ipify.org').text

#print(public_ip_address)
print(local_ip_address)

#Start Streaming Server (For Receiving)
server = StreamingServer(local_ip_address, 9999)
receiver = AudioReceiver(local_ip_address, 8888)

def start_listening():
    threading.Thread(target=server.start_server, daemon=True).start()
    threading.Thread(target=receiver.start_server, daemon=True).start()

def start_camera_and_audio():
    target_ip = text_target_ip.get(1.0, 'end-1c')
    #target_ip = "172.18.230.156"
    
    camera_client = CameraClient(target_ip, 9999)
    audio_sender = AudioSender(target_ip, 8888)

    threading.Thread(target=camera_client.start_stream, daemon=True).start()
    threading.Thread(target=audio_sender.start_stream, daemon=True).start()

def start_screen_and_audio():
    target_ip = text_target_ip.get(1.0, 'end-1c')
    #target_ip = "172.18.230.156"

    
    screen_client = ScreenShareClient(target_ip, 9999)
    audio_sender = AudioSender(target_ip, 8888)

    threading.Thread(target=screen_client.start_stream, daemon=True).start()
    threading.Thread(target=audio_sender.start_stream, daemon=True).start()

def start_full_duplex_camera():
    start_listening()  # Start receiving
    start_camera_and_audio()  # Start sending

def start_full_duplex_screen():
    start_listening()  # Start receiving
    start_screen_and_audio()  # Start sending

# GUI
window = tk.Tk()
window.title('Gestura Video Conference')
window.geometry('350x300')

label_own_ip = tk.Label(window, text=f'Your Public IP: {public_ip_address}')
label_own_ip.pack()

label_target_ip = tk.Label(window, text='Target IP:')
label_target_ip.pack()

text_target_ip = tk.Text(window, height=1)
text_target_ip.pack()

btn_camera_audio = tk.Button(window, text="Start 2-Way Camera & Audio", width=50, command=start_full_duplex_camera)
btn_camera_audio.pack(anchor=tk.CENTER, expand=True)

btn_screen_audio = tk.Button(window, text="Start 2-Way Screen & Audio", width=50, command=start_full_duplex_screen)
btn_screen_audio.pack(anchor=tk.CENTER, expand=True)

window.mainloop()