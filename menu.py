def showmenu():
    print("\n" + "="*45)
    print("  [1]  get user info (public)")
    print("  [2]  unfollow people")
    print("  [3]  like a post")
    print("  [4]  follow a user")
    print("  [5]  comment on a post")
    print("  [6]  post photo")
    print("  [7]  post video")
    print("  [8]  post story")
    print("  [9]  logout")
    print("  [0]  exit")
    print("="*45)

def getchoice():
    try:
        return int(input("\nchoose option: "))
    except ValueError:
        return -1
