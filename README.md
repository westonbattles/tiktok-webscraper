# tiktok-webscraper

Simple webscraping bot that has a set of methods to get specific and general information about a specified user/video (e.g. follower count, like count, etc..)




When I was coding this bot, I ran into a huge problem, as it turns out Tiktok (A $250 billion dollar company) isn't stupid and if you send enough get requests to it's web servers, you will be asked to complete a captcha.

Now I've seen many different solutions to this problem. Some people actually have went through the trouble of training a nueral network to solve captchas. Unfortunatly, I don't have the neccesary resources to achieve a similar solution, however I do have my brain.

I eventually realized that Tiktok only knows you need to be verified based off of your IP. My solution? **Proxies**

A quick google searched reaveled a website with a list of [free proxies](https://free-proxy-list.net/), and I then made the webscraper scrape this list of proxies, add them to a dictionary, and then choose a random one to use as a proxy whenever Tiktok sends you to the captcha page.

This may not be a solution as cool as artifical intelligence, however it's mine and I'm proud of it 
