
# axomic instagram tool

A free open sourced Instagram tool made for info, automation, etc. it is made by axom

---

## features

- get public user info
- unfollow multiple people
- like and comment on posts
- follow users
- upload photo/video to feed
- upload photo/video to story
- session persistence (no repeated login)

---

## installation guide for all devices

### termux (android)

```bash
pkg update && pkg upgrade
pkg install python git
termux-setup-storage
git clone https://github.com/axomtools/axomic-instagram-tool.git
cd axomic-instagram-tool
pip install -r requirements.txt
python main.py
```

media path example: /sdcard/DCIM/photo.jpg or /storage/emulated/0/Download/video.mp4

---

linux (ubuntu/debian/kali/parrot)

```bash
sudo apt update
sudo apt install python3 python3-pip git
git clone https://github.com/axomtools/axomic-instagram-tool.git
cd axomic-instagram-tool
pip3 install -r requirements.txt
python3 main.py
```

---

linux (fedora/rhel/centos)

```bash
sudo dnf install python3 python3-pip git
git clone https://github.com/axomtools/axomic-instagram-tool.git
cd axomic-instagram-tool
pip3 install -r requirements.txt
python3 main.py
```

---

linux (arch/manjaro)

```bash
sudo pacman -S python python-pip git
git clone https://github.com/axomtools/axomic-instagram-tool.git
cd axomic-instagram-tool
pip install -r requirements.txt
python main.py
```

---

windows (command prompt or powershell)

```cmd
git clone https://github.com/axomtools/axomic-instagram-tool.git
cd axomic-instagram-tool
pip install -r requirements.txt
python main.py
```

media path example: C:\Users\yourname\Pictures\photo.jpg or C:\Users\yourname\Videos\video.mp4

---

macos (intel/apple silicon)

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
brew install python git
git clone https://github.com/axomtools/axomic-instagram-tool.git
cd axomic-instagram-tool
pip3 install -r requirements.txt
python3 main.py
```

media path example: /Users/yourname/Pictures/photo.jpg or /Users/yourname/Downloads/video.mp4

---

ios (ish shell)

```bash
apk update
apk add python3 py3-pip git
git clone https://github.com/axomtools/axomic-instagram-tool.git
cd axomic-instagram-tool
pip install -r requirements.txt
python3 main.py
```

media path example: /root/photo.jpg (use files app sharing)

---

chromebook / chromeos (linux container)

```bash
sudo apt update
sudo apt install python3 python3-pip git
git clone https://github.com/axomtools/axomic-instagram-tool.git
cd axomic-instagram-tool
pip3 install -r requirements.txt
python3 main.py
```

---

quick run (after install)

```bash
cd axomic-instagram-tool
python main.py
```

---

usage

- choose an option from the menu
- actions that need a login will ask you for username and password 
- session is saved. you stay logged in until you choose logout
- for uploading media, provide the full path to the file

---

menu options

option description
1 get user info (public)
2 unfollow people
3 like a post
4 follow a user
5 comment on a post
6 post photo
7 post video
8 post story
9 logout
0 exit

---

troubleshooting

error: instagrapi not found

```bash
pip uninstall instagrapi
pip install instagrapi==2.0.2
```

error: permission denied (termux)

```bash
termux-setup-storage
python -m pip install --user --upgrade pip
```

error: tls/ssl problem

```bash
pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org instagrapi
```

---

notes

- be careful with rate limits. the tool includes short delays to help
- instagram may temporarily block actions

---

author

axom

---

star the repo

if you find this tool useful, please star it on github

`
