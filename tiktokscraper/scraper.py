import requests
import random
import time
import json
import re
from bs4 import BeautifulSoup
from datetime import datetime
from unidecode import unidecode

BASEURL = "https://www.tiktok.com/"

class create():

    INSTANCE = None

    def __init__(self):

        if create.INSTANCE == None:
            create.INSTANCE = self
        else:
            raise Exception("Only one Tiktok API Instance allowed")


        self.user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36"


    #Helper Methods
    def soupify(self, url):

        page = requests.get(url, headers={'User-Agent': self.user_agent})
        soup = BeautifulSoup(page.content, "html.parser")

        if self.is_captcha(soup):

            print("Captcha required, retrying with proxy in:", end =" ")
            proxy = self.get_proxy()
            for i in range(5,0,-1):
                time.sleep(1)
                print(str(i), end = " ")

            time.sleep(1)


            page = requests.get(url, headers={'User-Agent': self.user_agent}, proxies=proxy)
            soup = BeautifulSoup(page.content, "html.parser")

        return soup

    def get_user_info(self, user):

        url = BASEURL + user
        soup = self.soupify(url)

        data = soup.find("script", id="__NEXT_DATA__")
        jsondata = json.loads(str(data.string))

        return jsondata["props"]["pageProps"]["userInfo"]

    def is_captcha(self, soup):
        desc = soup.find("p", class_="page-desc")

        if desc is None:
            return False

        return desc.get("id") == "verifyEle"

    def get_proxy(self):
        url = 'https://free-proxy-list.net/anonymous-proxy.html'
        regex = "^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$"
        ip_addresses = []

        page = requests.get(url)
        soup = BeautifulSoup(page.content, "html.parser")

        td = soup.find_all("td")

        for i in range(len(td)):
            if re.search(regex, td[i].text):
                ip_addresses.append(td[i].text+":"+td[i+1].text)

        index = random.randint(0, len(ip_addresses)-1)
        proxy = {
            "http": ip_addresses[index],
            "https": ip_addresses[index]
        }

        return proxy

    def account_exists(self, user):

        url = BASEURL + user
        soup = self.soupify(url)
        if soup.find(class_="jsx-2275266356 title") is not None:
            return soup.find(class_="jsx-2275266356 title").text != "Couldn't find this account"
        return True

    def is_private_account(self, user):

        if not self.account_exists(user):
            raise Exception("That account does not exist")

        user_info = self.get_user_info(user)
        return user_info["user"]['privateAccount']

    def unix_to_datetime(self, unix):

        return datetime.utcfromtimestamp(unix).strftime('%Y-%m-%d %I:%M:%S %p')


    #Getters
    def get_follower_count(self, user):

        if self.account_exists(user) is False:
            raise Exception("That account does not exist")

        user_info = self.get_user_info(user)
        return user_info["stats"]['followerCount']

    def get_following_count(self, user):

        if self.account_exists(user) is False:
            raise Exception("That account does not exist")

        user_info = self.get_user_info(user)
        return user_info["stats"]['followingCount']

    def get_like_count(self, user):

        if self.account_exists(user) is False:
            raise Exception("That account does not exist")

        user_info = self.get_user_info(user)
        return user_info["stats"]['heartCount']

    def get_video_count(self, user):
        if self.account_exists(user) is False:
            raise Exception("That account does not exist")

        user_info = self.get_user_info(user)
        return user_info["stats"]['videoCount']

    def get_videos(self, user):

        video_info = []

        if self.account_exists(user) is False:
            raise Exception("That account does not exist")

        url = BASEURL + user
        soup = self.soupify(url)

        data = soup.find("script", id="__NEXT_DATA__")
        jsondata = json.loads(str(data.string))

        video_list = jsondata["props"]["pageProps"]["items"]
        for video in video_list:

            to_add = {}
            desc = u'{}'.format(video['desc'])
            audio_title = u'{}'.format(video['music']['title'])
            audio_author = u'{}'.format(video['music']['authorName'])

            to_add['link'] = url + "/video/" + video['id']
            to_add['description'] = unidecode(desc)
            to_add['video created'] = self.unix_to_datetime(video['createTime']) + " (Unix " + str(video['createTime']) +")"
            to_add['audio'] = unidecode(audio_title) + " - " + unidecode(audio_author) + " (" + video['music']['playUrl']+")"



            video_info.append(to_add)

        return json.dumps(video_info, indent=4)


    def get_uid(self, user):

        if not self.account_exists(user):
            raise Exception("That account does not exist")

        user_info = self.get_user_info(user)
        return user_info["user"]['id']

    def get_avatar(self, user):

        if not self.account_exists(user):
            raise Exception("That account does not exist")

        user_info = self.get_user_info(user)
        return user_info["user"]['avatarLarger']

    def get_nickname(self, user):

        if not self.account_exists(user):
            raise Exception("That account does not exist")

        user_info = self.get_user_info(user)
        return user_info["user"]["nickname"]

    def get_bio(self, user):

        if not self.account_exists(user):
            raise Exception("That account does not exist")

        user_info = self.get_user_info(user)
        return user_info["user"]['signature']

    def get_create_time(self, user):

        if not self.account_exists(user):
            raise Exception("That account does not exist")

        user_info = self.get_user_info(user)

        unix = int(user_info["user"]['createTime'])
        date = self.unix_to_datetime(unix)

        return user + " account created: " + date + " GMT (Unix: " + str(unix) +")"

    def is_verified(self, user):

        if not self.account_exists(user):
            raise Exception("That account does not exist")

        user_info = self.get_user_info(user)
        return user_info["user"]['verified']


