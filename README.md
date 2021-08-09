<h1 align="center"> Simple Tiktok Webscraper </h1>

Simple webscraping bot that has a set of methods to get specific and general information about a specified user/video (e.g. follower count, like count, etc..)



## Overview

When I was coding this bot, I ran into a huge problem, as it turns out Tiktok (A $250 billion dollar company) isn't stupid and if you send a lot of get requests to it's web servers, you will be profiled as a robot and asked to complete a captcha.

<img src = "https://user-images.githubusercontent.com/50222899/128652952-6a8d19a6-de15-455b-a626-0f3903b47c7d.png">

Now I've seen many different solutions to this problem. Some people actually have went through the trouble of training a nueral network to solve captchas. Unfortunatly, (as much as I would love to), I do not have the neccesary resources to achieve a similar solution however, I do have my brain.

I eventually realized that Tiktok only knows you need to be verified based off of your IP. My solution? **Proxies**

A quick google searched reaveled a website with a list of [free proxies](https://free-proxy-list.net/), and I then made the webscraper scrape this list of proxies, add them to a dictionary, and then choose a random one to use as a proxy whenever Tiktok asks for you to complete a captcha.

This may not be a solution as cool as artifical intelligence, however it's mine and I'm proud of it 
