# Dencrypter by 74lg0
from cryptography.fernet import Fernet # type: ignore
from pystyle import Colorate, Colors # type: ignore
import sys
import os
from colorama import Fore # type: ignore

def decryptor(op):
    if op == 1:
        text = input('TXT ⇒ ').encode()
        key = input('Key ⇒ ').encode()
        e = Fernet(key)
        decryp = e.decrypt(text).decode()
        os.system('cls' if os.name == 'nt' else 'clear')
        print(Fore.BLUE+'[!] '+Fore.WHITE+f'Text decode ⇒ {decryp}')
    
    elif op == 2:
        # Direcctorio del archivo original
        arch = input("Direccion del archivo ⇒ ")
        # Leemos el archivo en bit
        with open(arch, 'rb') as earch:
            lines = earch.read()
        # Codificamos la clave Fernet en Bytes
        key = input('Key ⇒ ').encode()
        print(Fore.BLUE+'[!]'+Fore.WHITE+f' Fernet Key ⇒ {key.decode()}')
        e = Fernet(key)
        # Decodificamos en bytes las lineas del archivo
        enc = e.decrypt(lines)
        file_path = 'decrypt_file'
        # Creamos un nuevo archivo y escribimos los datos en bytes
        with open(file_path, 'wb') as dc_file:
            dc_file.write(enc)
        print(Fore.BLUE+'[!] '+Fore.WHITE+f'Encrypter file save with name ⇒ {file_path}')

def encrypted(op):
    if op == 1:
        text = input('TXT ⇒ ')
        os.system('cls' if os.name == 'nt' else 'clear')
        key = Fernet.generate_key()
        print(Fore.BLUE+'[!]'+Fore.WHITE+f' Fernet Key ⇒ {key.decode()}')
        e = Fernet(key)
        text = text.encode()
        enc = e.encrypt(text)
        print(Fore.BLUE+'[!]'+Fore.WHITE+f' Encrypted txt ⇒ {enc.decode()}')
    
    elif op == 2:
        # Direcctorio del archivo original
        arch = input("Direccion del archivo ⇒ ")
        os.system('cls' if os.name == 'nt' else 'clear')
        # Abrimos el archivo en bits
        with open(arch, 'rb') as darch:
            lines = darch.readline()
        key = Fernet.generate_key()
        print(Fore.BLUE+'[!]'+Fore.WHITE+f' Fernet Key ⇒ {key.decode()}')
        e = Fernet(key)
        enc = e.encrypt(lines)
        # Abrimos o creamos un nuevo archivo y escribimos en bit
        with open('enc_archive.zlo', 'wb') as enc_file:
            enc_file.write(enc)
        print(Fore.BLUE+'[!] '+Fore.WHITE+'Encrypter file save with name ⇒ enc_archive.zlo')

    elif op == 3:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(Colorate.Horizontal(Colors.rainbow, banner))
        print(Colorate.Vertical(Colors.rainbow, '[1] Text\n[2] Archive'))
        op = int(input('⇒ '))
        decryptor(op)

#Clear console
os.system('cls' if os.name == 'nt' else 'clear')

banner = '''
 .S_sSSs      sSSs   .S_sSSs      sSSs   .S_sSSs     .S S.    .S_sSSs    sdSS_SSSSSSbs    sSSs   .S_sSSs
.SS~YS%%b    d%%SP  .SS~YS%%b    d%%SP  .SS~YS%%b   .SS SS.  .SS~YS%%b   YSSS~S%SSSSSP   d%%SP  .SS~YS%%b
S%S   `S%b  d%S'    S%S   `S%b  d%S'    S%S   `S%b  S%S S%S  S%S   `S%b       S%S       d%S'    S%S   `S%b
S%S    S%S  S%S     S%S    S%S  S%S     S%S    S%S  S%S S%S  S%S    S%S       S%S       S%S     S%S    S%S
S%S    S&S  S&S     S%S    S&S  S&S     S%S    d*S  S%S S%S  S%S    d*S       S&S       S&S     S%S    S&S
S&S    S&S  S&S_Ss  S&S    S&S  S&S     S&S   .S*S   SS SS   S&S   .S*S       S&S       S&S_Ss  S&S    S&S
S&S    S&S  S&S~SP  S&S    S&S  S&S     S&S_sdSSS     S S    S&S_sdSSS        S&S       S&S~SP  S&S    S&S
S&S    S&S  S&S     S&S    S&S  S&S     S&S~YSY%b     SSS    S&S~YSSY         S&S       S&S     S&S    S&S
S*S    d*S  S*b     S*S    S*S  S*b     S*S   `S%b    S*S    S*S              S*S       S*b     S*S    d*S
S*S   .S*S  S*S.    S*S    S*S  S*S.    S*S    S%S    S*S    S*S              S*S       S*S.    S*S   .S*S
S*S_sdSSS    SSSbs  S*S    S*S   SSSbs  S*S    S&S    S*S    S*S              S*S        SSSbs  S*S_sdSSS
SSS~YSSY      YSSP  S*S    SSS    YSSP  S*S    SSS    S*S    S*S              S*S         YSSP  SSS~YSSY
                    SP                  SP            SP     SP               SP
                    Y                   Y             Y      Y                Y
                                       Created by: 74lg0
'''
try:
    print(Colorate.Horizontal(Colors.rainbow, banner))
    print(Colorate.Vertical(Colors.rainbow, '[1] Text\n[2] Archive\n[3] Decryptor'))
    op = int(input('=> '))
    encrypted(op)

except KeyboardInterrupt:
    sys.exit()

except Exception as e:
    print(Colorate.Horizontal(Colors.red_to_green, f'Un error ha ocurrido => {e}'))