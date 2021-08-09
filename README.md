<h1 align="center"> Simple Tiktok Webscraper </h1>

Simple webscraping bot that has a set of methods to get specific and general information about a specified Tiktok user/video (e.g. follower count, like count, etc..)



## Overview

This project was started, mainly as a way for me to practice my webscraping skills and class structure knowledge. I don't expect anyone to download this but I'm still going to write a fully fleshed out README with usage tutorials and everything for completion's sake

Web scraping is a really important tool to learn, even if it's generally fround apon by companies. The problem is humans love data, which means we will stop at nothing to find ways to make data more accessible to us. Webs crapers are no exception.

I do want to preface one thing first though, I have talked to many developers about the morality behind web scraping, and learned many different opinions on if ethically it should be done. It is my belief that due to all of the data being scraped in this project's current publicly accesible state, writing a program that goes through the frontend code to scrape data goes against no moral codes. 

I do agree that mass spamming requests with hundreds of IPs in an attempt to DDOS, or even just in an attempt to retreive a huge amount of data from a company's servers (especially if the company/servers are smaller than typical big corperations) is a blatant violation of said moral codes. However Tiktok is a $250 Billion dollar compant and I am a 16 year old with a laptop.


## Table of Contents


<ul>
    <li><a href="#Installation">Intallation</a></li>
    <li><a href="#Setup">Setup</a></li>
    <li><a href="#Usage">Usage</a></li>
    <li><a href="#Inspiration">Inspiration</a></li>
    <li><a href="#CAPTCHA">CAPTCHA</a></li>
</ul>


## Installation


As usual, first you need to make sure you have Python 3 + pip installed. To check if you have these installed run `python -V` (make sure the version is python 3.X.X) and `python -m pip -V`. If you don't have these installed please read the guide below

### Installing Python3 for Windows

Click on the following link and open it once it's downloaded:

`https://www.python.org/ftp/python/3.8.0/python-3.8.0-amd64.exe`

Once you have opened the installer, make sure that you add Python 3.8 to path. Your installer should look like this:

<img align="center" src="https://i.imgur.com/SkviBw6.png">

### Installing Python3 for MacOS.

Click on the following link and install:

`https://www.python.org/ftp/python/3.8.0/python-3.8.0-macosx10.9.pkg`

### Installing Python3 for Linux

Since there are a multitude of package installers for Linux, we'll choose `apt` which is used in Debian-derived distros such as Ubuntu as an example.

Go to the terminal and type in the following:

```shell
sudo apt update && sudo apt upgrade
sudo apt install -y python3 python3-pip
```

### Installing the Required Packages


## Setup


I decided to work on this project mainly for myself, because I wanted to see 



When I was coding this bot I was faced with. as it turns out Tiktok doesn't like it when you pull a lot of data from them, so if you send a lot of get requests to their web servers, you will be profiled as a robot and asked to complete a captcha.

<img src = "https://user-images.githubusercontent.com/50222899/128652952-6a8d19a6-de15-455b-a626-0f3903b47c7d.png">

Now I've seen many different solutions to this problem. Some people actually have went through the trouble of training a nueral network to solve captchas. Unfortunatly, (as much as I would love to), I do not have the neccesary resources to achieve a similar solution however, I do have my brain.

I eventually realized that Tiktok only knows you need to be verified based off of your IP. My solution? **Proxies**

A quick google searched reaveled a website with a list of [free proxies](https://free-proxy-list.net/), and I then made the webscraper scrape this list of proxies, add them to a dictionary, and then choose a random one to use as a proxy whenever Tiktok asks for you to complete a captcha.

This may not be a solution as cool as artifical intelligence, however it's mine and I'm proud of it 
