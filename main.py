import sys
from clientmanager import clientmanager
from menu import showmenu, getchoice
from utils import clearscreen, printart

def main():
    clearscreen()
    printart()
    manager = clientmanager()
    while True:
        showmenu()
        choice = getchoice()
        if choice == 0:
            print("\nexiting tool. goodbye!")
            sys.exit(0)
        elif choice == 1:
            username = input("\nenter instagram username: ").strip()
            manager.getuserinfo(username)
        elif choice == 2:
            if not manager.ensurelogin():
                continue
            try:
                amount = int(input("\nhow many people to unfollow? "))
                if amount <= 0:
                    print("enter a positive number.")
                    continue
                manager.unfollowusers(amount)
            except ValueError:
                print("invalid number.")
        elif choice == 3:
            if not manager.ensurelogin():
                continue
            posturl = input("\ninstagram post link: ").strip()
            manager.likepost(posturl)
        elif choice == 4:
            if not manager.ensurelogin():
                continue
            targetuser = input("\nusername to follow: ").strip()
            manager.followuser(targetuser)
        elif choice == 5:
            if not manager.ensurelogin():
                continue
            posturl = input("\ninstagram post link: ").strip()
            commenttext = input("\nyour comment: ").strip()
            manager.commentpost(posturl, commenttext)
        elif choice == 6:
            if not manager.ensurelogin():
                continue
            photopath = input("\nfull path to photo: ").strip()
            caption = input("\ncaption for photo: ").strip()
            manager.postphoto(photopath, caption)
        elif choice == 7:
            if not manager.ensurelogin():
                continue
            videopath = input("\nfull path to video: ").strip()
            caption = input("\ncaption for video: ").strip()
            manager.postvideo(videopath, caption)
        elif choice == 8:
            if not manager.ensurelogin():
                continue
            mediapath = input("\nfull path to photo or video: ").strip()
            mediatype = input("\ntype (photo/video): ").strip().lower()
            caption = input("\nstory caption (optional): ").strip()
            manager.poststory(mediapath, mediatype, caption)
        elif choice == 9:
            manager.logout()
        else:
            print("\ninvalid option. choose 0-9.")

if __name__ == "__main__":
    main()
