# axomic instagram tool

A free open sourced Instagram tool made for info,automation,etc
it is made by axom

## features
- get public user info  
- unfollow multiple people  
- like and comment on posts  
- follow users  
- upload photo/video to feed  
- upload photo/video to story  
- session persistence  

## installation 

termux :

`pkg update && pkg upgrade`
`pkg install python git`
`git clone https://github.com/axomtools/axomic-instagram-tool.git`
`cd axomic-instagram-tool`
`pip install -r requirements.txt`
`python main.py`
Here's how to install and run the axomic instagram tool on different devices:

Installation Guide for All Devices

Termux (Android)

setup storage before running. 

then use paths like /sdcard/DCIM/photo.jpg or /storage/emulated/0/Download/video.mp4

---

Linux (Ubuntu/Debian/Kali/Parrot)


sudo apt update
sudo apt install python3 python3-pip git
git clone https://github.com/axomtools/axomic-instagram-tool.git
cd axomic-instagram-tool
pip3 install -r requirements.txt
python3 main.py


fedora/rhel/centos:


sudo dnf install python3 python3-pip git
git clone https://github.com/axomtools/axomic-instagram-tool.git
cd axomic-instagram-tool
pip3 install -r requirements.txt
python3 main.py


arch linux/manjaro:

```bash
sudo pacman -S python python-pip git
git clone https://github.com/axomtools/axomic-instagram-tool.git
cd axomic-instagram-tool
pip install -r requirements.txt
python main.py
```

---

Windows

option 1 - windows terminal (python installed):

```cmd
git clone https://github.com/axomtools/axomic-instagram-tool.git
cd axomic-instagram-tool
pip install -r requirements.txt
python main.py
```


windows path examples for media:

```
C:\Users\yourname\Pictures\photo.jpg
C:\Users\yourname\Videos\video.mp4
```

---

MacOS (Intel/Apple Silicon)


/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
brew axomic-instagram-tool.git
cd axomic-instagram-tool
pip3 install -r requirements.txt
python3 main.py


macos path examples:


/Users/yourname/Pictures/photo.jpg
/Users/yourname/Downloads/video.mp4


---

iOS (iSH Shell)


apk update
apk add python3 py3-pip git
git clone https://github.com/axomtools/axomic-instagram-tool.git
cd axomic-instagram-tool
pip install -r requirements.txt
python3 main.py


ios path examples (iSH):


/root/photo.jpg
or use photos via files app sharing

---

ChromeOs (Linux Container)

sudo apt update
sudo apt install python3 python3-pip git
git clone https://github.com/axomtools/axomic-instagram-tool.git
cd axomic-instagram-tool
pip3 install -r requirements.txt
python3 main.py


## Troubleshooting

if you faced "error: instagrapi not found"

`pip uninstall instagrapi`
`pip install instagrapi==2.0.2`

if you faced "error: permission denied"

`termux-setup-storage`
`python -m pip install --user --upgrade pip`

if you faced "error: tls/ssl problem" =

`pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org instagrapi`

`py -m pip install -r requirements.txt`
`py main.py`

Quick Run (after clone)


`cd axomic-instagram-tool`
`python main.py`

usage

· choose an option from the options menu
· actions that need a login will ask you for username/password
· session is saved. you stay logged in until you choose logout
· for uploading media, provide the path to the file (e.g. /sdcard/photo.jpg) or the link of the photo or video 

notes

· be careful with rate limits – the tool includes short delays
· instagram may temporarily block some actions for rate limiting
