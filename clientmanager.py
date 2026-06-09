import time
import os
from instagrapi import Client
from instagrapi.exceptions import LoginRequired, ClientError

class clientmanager:
    def __init__(self):
        self.client = Client()
        self.loggedin = False
        self._loadsession()

    def _loadsession(self):
        sessionfile = "axomicsession.json"
        if os.path.exists(sessionfile):
            try:
                self.client.load_settings(sessionfile)
                self.client.get_timeline_feed()
                self.loggedin = True
                print("session loaded. logged in as", self.client.user_id)
            except:
                self.loggedin = False
                print("saved session invalid. please login manually.")

    def _savesession(self):
        self.client.dump_settings("axomicsession.json")

def login(self, username=None, password=None, verification_code=None):
    if not username:
        username = input("\nlogin username: ").strip()
    if not password:
        password = input("login password: ").strip()
    try:
        self.client.login(username, password, verification_code=verification_code)
        self.loggedin = True
        self._savesession()
        print("login successful. welcome", username)
        return True
    except Exception as e:
        if "two_factor" in str(e).lower() or "challenge" in str(e).lower():
            code = input("enter 2fa verification code from authenticator app or sms: ").strip()
            return self.login(username, password, code)
        print("login failed:", str(e))
        self.loggedin = False
        return False

    def ensurelogin(self):
        if self.loggedin:
            return True
        print("\nthis option requires login - please input your account username and password in order to login")
        return self.login()

    def logout(self):
        if self.loggedin:
            self.client.logout()
            self.loggedin = False
            if os.path.exists("axomicsession.json"):
                os.remove("axomicsession.json")
            print("logged out and session removed.")
        else:
            print("you are not logged in.")

    def getuserinfo(self, username):
        try:
            user = self.client.user_info_by_username(username)
            print(f"\nuser information for @{username}")
            print(f"    full name : {user.full_name}")
            print(f"    user id   : {user.pk}")
            print(f"    bio       : {user.biography}")
            print(f"    posts     : {user.media_count}")
            print(f"    followers : {user.follower_count}")
            print(f"    following : {user.following_count}")
            print(f"    private   : {user.is_private}")
            print(f"    verified  : {user.is_verified}")
        except Exception as e:
            print("could not fetch user info:", str(e))

    def unfollowusers(self, amount):
        try:
            userid = self.client.user_id
            following = self.client.user_following(userid, amount=amount)
            if not following:
                print("no following users found or you already unfollowed everyone.")
                return
            count = 0
            for user in following:
                try:
                    self.client.user_unfollow(user.pk)
                    count += 1
                    print(f"unfollowed {user.username} ({count}/{len(following)})")
                    time.sleep(2)
                except Exception as e:
                    print(f"failed to unfollow {user.username}: {str(e)}")
            print(f"done. unfollowed {count} people.")
        except Exception as e:
            print("error during unfollow:", str(e))

    def likepost(self, posturl):
        try:
            mediaid = self.client.media_pk_from_url(posturl)
            self.client.media_like(mediaid)
            print("liked the post!")
        except Exception as e:
            print("could not like post:", str(e))

    def followuser(self, targetusername):
        try:
            userid = self.client.user_id_from_username(targetusername)
            self.client.user_follow(userid)
            print(f"now following @{targetusername}")
        except Exception as e:
            print("could not follow user:", str(e))

    def commentpost(self, posturl, commenttext):
        try:
            mediaid = self.client.media_pk_from_url(posturl)
            self.client.media_comment(mediaid, commenttext)
            print("comment posted successfully.")
        except Exception as e:
            print("could not post comment:", str(e))

    def postphoto(self, photopath, caption):
        if not os.path.exists(photopath):
            print("photo file not found.")
            return
        try:
            self.client.photo_upload(photopath, caption=caption)
            print("photo uploaded to feed.")
        except Exception as e:
            print("photo upload failed:", str(e))

    def postvideo(self, videopath, caption):
        if not os.path.exists(videopath):
            print("video file not found.")
            return
        try:
            self.client.video_upload(videopath, caption=caption)
            print("video uploaded to feed.")
        except Exception as e:
            print("video upload failed:", str(e))

    def poststory(self, mediapath, mediatype, caption):
        if not os.path.exists(mediapath):
            print("media file not found.")
            return
        try:
            if mediatype == "photo":
                self.client.photo_upload_to_story(mediapath, caption=caption)
                print("photo story uploaded.")
            elif mediatype == "video":
                self.client.video_upload_to_story(mediapath, caption=caption)
                print("video story uploaded.")
            else:
                print("unknown media type. use 'photo' or 'video'.")
        except Exception as e:
            print("story upload failed:", str(e))
