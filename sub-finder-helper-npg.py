#!/usr/bin/env python3
# PYTHON SCRIPT THAT DOESN'T CONTAIN THE GAUDY PROGRESS BAR!!!!

import os
import sys
import click
from tqdm import tqdm
from time import sleep

# Exception Handling for First Argument, Which Needs To Be A URL
try:
    url = sys.argv[1]
except:
    os.system("echo '\033[1;38;2;255;0;0mYou forgot the URL argument... Please run the program like the example below: \033[0m\npython assetfinder.py ct-cybersec.com'")
    sys.exit(1)

# Make Sure To Use The Correct URL Formatting For URL Argument. This If Statement Also Disallows A Second Argument. Will Add Special Characters Later
if (url.startswith(".")) | (url.endswith(".")):
    os.system("echo '\033[1;38;2;255;0;0mPlease use the correct scheme for a URL (i.e. ct-cybersec.com)\033[0m'")
    sys.exit(1)

# ARRRRTTTTTT
print("""
\033[1;38;2;250;250;110m  ___ _   _ ___   ___ ___ _  _ ___  ___ ___ \033[0m
\033[1;38;2;170;228;121m / __| | | | _ ) | __|_ _| \| |   \| __| _ \\\033[0m
\033[1;38;2;100;201;135m \__ \ |_| | _ \ | _| | || .` | |) | _||   /\033[0m
\033[1;38;2;35;170;143m |___/\___/|___/_|_| |___|_|\_|___/|___|_|_\\\033[0m
\033[1;38;2;0;137;138m        | || | __| |  | _ \ __| _ \ |       \033[0m
\033[1;38;2;23;104;119m        | __ | _|| |__|  _/ _||   /_|       \033[0m
\033[1;38;2;42;72;88m        |_||_|___|____|_| |___|_|_(_)                     
\033[0m
\033[1mAn Automation Tool To Help Discover Subdomains,\n       Check Alive Subdomains, & More!\n\n          Created By: ct-cybersec\033[0m
""")
sleep(1)

# Start Of Main Code
os.system("echo '\n\033[1;38;2;250;250;110mStarting The Process For '" + url.upper() + "'!\033[0m'")
sleep(0.05)
os.system("echo '\033[1;38;2;209;240;114m(1) Verifying The \"URL\" Folder Exists\033[0m'")

# Creating A Directory That Is Labelled As The Url You, The User, Has Put As The Argument
if not os.path.exists(url):
    os.mkdir(url)
os.system("echo '\033[1;38;2;209;240;114mFinished Verification, Moving On\033[0m'")
sleep(0.05)
os.system("echo '\033[1;38;2;170;228;121m(2) Verifying The \"Recon\" Folder Exists\033[0m'")

# Creating A Directory That Is Labelled "Recon" Inside The URL Folder
if not os.path.exists(url + "/recon"):
    os.mkdir(url + "/recon")
os.system("echo '\033[1;38;2;170;228;121mFinished Verification, Moving On\033[0m'")
sleep(0.05)
os.system("echo '\033[1;38;2;134;215;128m(3) Creating A File Named \"Assets.txt\" & \"Amass.txt\"\033[0m'")

# Creating & Opening A File Named "Assets.txt" For Later Use
open(url + "/recon/assets.txt", "w+")
open(url + "/recon/amass.txt", "w+")
os.system("echo '\033[1;38;2;134;215;128mFinished Creating Files, Moving On\033[0m'")
sleep(0.05)
os.system("echo '\033[1;38;2;100;201;135m(4) Running Assetfinder By TomNomNom For '" + url.upper() + "' & Placing Results Into \"Assets.txt\"\033[0m'")

# Running Assetfinder, Created By TomNomNom, Using The URL Supplied & Placing Results Into The "Assets.txt" File
os.system("assetfinder " + url + " >> " + url + "/recon/assets.txt")
os.system("echo '\033[1;38;2;100;201;135mFinished Running Assetfinder, Moving On\033[0m'")
sleep(0.05)
os.system("echo '\033[1;38;2;68;185;141m(5) Running Amass For '" + url.upper() + "' & Placing Results Into \"Amass.txt\"\nNOTE: Be Patient, Amass Takes A While!\033[0m'")

# Running Amass Using The URL Supplied & Placing Results Into The "Amass.txt" File
os.system("amass enum -max-dns-queries 200 -silent -o " + url + "/recon/amass.txt -d " + url)
os.system("echo '\033[1;38;2;68;185;141mFinished Running Amass, Moving On\033[0m'")
sleep(0.05)
os.system("echo '\033[1;38;2;35;170;143m(6) Opening \"Assets.txt\" & \"Amass.txt\" Files For Reading\033[0m'")

# Reading "Assets.txt" File To Transfer Non-Duplicates & Results That Contain The URL Given
with open(url + "/recon/assets.txt", "r") as f, open(url + "/recon/amass.txt", "r") as f2:
    asset_lines = f.readlines()
    amass_lines = f2.readlines()
asset_lines_set = set(asset_lines)
amass_lines_set = set(amass_lines)
os.system("echo '\033[1;38;2;35;170;143mFinished Opening Files For Reading, Moving On\033[0m'")
sleep(0.05)
os.system("echo '\033[1;38;2;0;153;143m(7) Transferring Results From Initial Results To Final Results (i.e. Getting Rid of Duplicates & Any Result Without '" + url.upper() + "')\033[0m'")

# Transferring The Above URL Results To Their Respective Final Results File
with open(url + "/recon/assets_final.txt", "w") as f, open(url + "/recon/amass_final.txt", "w") as f2:
    for asset_new_line in asset_lines_set:
        if url in asset_new_line:
            f.write(asset_new_line)
    for amass_new_line in amass_lines_set:
        if url in amass_new_line:
            f2.write(amass_new_line)
os.system("echo '\033[1;38;2;0;153;143mFinished Transferring Results, Moving On\033[0m'")
sleep(0.05)
os.system("echo '\033[1;38;2;0;137;138m(8) Verifying The \"HTTProbe\" Folder Exists\033[0m'")

# Creating A Directory Called "HTTProbe" for HTTProbe Results
if not os.path.exists(url + "/recon/httprobe"):
    os.mkdir(url + "/recon/httprobe")
os.system("echo '\033[1;38;2;0;137;138mFinished Verification, Moving On\033[0m'")
sleep(0.05)
os.system("echo '\033[1;38;2;0;120;130m(9) Running HTTProbe To Check For Live Domains & Placing Results Into Their Respective \"Alive\" Files\033[0m'")

# Running HTTProbe To Check For Live Domains By Reading (Cat) The Two Result Files
os.system("cat " + url + "/recon/assets_final.txt | sort -u | sed \'s/https\?:\/\///\' | sed \'s/http\?:\/\///\' | tr -d \':443\' | tr -d \':80\' >> " + url + "/recon/httprobe/a1.txt")
os.system("cat " + url + "/recon/amass_final.txt | sort -u | sed \'s/https\?:\/\///\' | sed \'s/http\?:\/\///\' | tr -d \':443\' | tr -d \':80\' >> " + url + "/recon/httprobe/a2.txt")
os.system("sort -u " + url + "/recon/httprobe/a1.txt > " + url + "/recon/httprobe/alive_assets.txt")
os.system("sort -u " + url + "/recon/httprobe/a2.txt > " + url + "/recon/httprobe/alive_amass.txt")
os.system("rm " + url + "/recon/httprobe/a1.txt")
os.system("rm " + url + "/recon/httprobe/a2.txt")
os.system("echo '\033[1;38;2;0;120;130mFinished Running HTTProbe, Moving On\033[0m'")
os.system("echo '\033[1;38;2;0;120;130m(10) Transferring Alive Results To A Combined File\033[0m'")

# Reading & Transferring The Two Alive Files To A Combined Alive File
files = (url + "/recon/httprobe/alive_assets.txt", url + "/recon/httprobe/alive_amass.txt")
all_lines = []
for f in files:
    with open(f,"r") as fi:
        all_lines += fi.readlines()
all_lines = set(all_lines)
with open(url + "/recon/httprobe/alive_combined.txt", "w") as fo:
    fo.write("".join(all_lines))
            
os.system("echo '\033[1;38;2;0;120;130mFinished Combining Alive Results, Moving On\033[0m'")
sleep(0.05)
os.system("echo '\033[1;38;2;23;104;119mCleaning Everything Up\033[0m'")
sleep(0.05)
os.system("echo '\033[1;38;2;23;104;119mFinished Running The Program!\033[0m'")
sleep(0.05)
os.system("echo '\n""'Question [In Dwight Schrute's Voice]: Would You Like To Delete The Original \"Assets.txt\" & \"Amass.txt\" Files (Keeping The Final Files)? Blank = Yes\033[0m'")

# Using Click Library, Asking If You, The User, Want To Delete The Original Result Files Or Keep Them
if (click.confirm("", default=True)):
    os.remove(url + "/recon/assets.txt")
    os.remove(url + "/recon/amass.txt")
    os.system("echo '\nRemoved Assets.txt & Amass.txt & Kept The Final Files!\033[0m'")
    os.system("echo 'Continuing On...\033[0m'")
else:
    os.system("echo 'Continuing On...\033[0m'")
sleep(0.5)
os.system("echo '\n'""'Last Question: Would You Like To Delete The Original Alive Files (Keeping The Combined File)? Blank = Yes\033[0m'")

# Using Click Library, Asking If You, The User, Want To Delete The Original Result Files Or Keep Them
if (click.confirm("", default=True)):
    os.remove(url + "/recon/httprobe/alive_assets.txt")
    os.remove(url + "/recon/httprobe/alive_amass.txt")
    os.system("echo '\nRemoved Original Alive Files & Kept The Combined File!\033[0m'")
    os.system("echo 'Done! Buh-Bye 👋\033[0m'")
else:
    os.system("echo '\nDone! Buh-Bye 👋\033[0m'")
