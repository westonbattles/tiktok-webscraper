<h1 align="center"> Simple Tiktok Webscraper </h1>

Simple webscraping bot that has a set of methods to get specific and general information about a specified Tiktok user/video (e.g. follower count, like count, etc..)



## Overview

This project was started, mainly as a way for me to practice my webscraping skills and class structure knowledge. I don't expect anyone to download this but I'm still going to write a fully fleshed out README with usage tutorials and everything for completion's sake

Web scraping is a really important tool to learn, even if it's generally frowned upon by many companies. The problem is humans love data, which means we will stop at nothing to find ways to make data more accessible to us. Web scrapers are no exception.

I do want to preface one thing first though, I have talked to many developers about the morality behind webscraping, and learned many different opinions on the ethical dilemmas surrounding it. It is my belief that due to all of the data being scraped in this project's current publicly accesible state, writing a program that goes through the front-end code to scrape data goes against no moral codes. 

I do agree that mass spamming requests with hundreds of IPs in an attempt to DDOS, or even just in an attempt to retreive a huge amount of data from a company's servers (especially if the company/company's servers are smaller than typical big corperation/big corperation's servers) is a blatant violation of said moral codes. However Tiktok is a $250 Billion company and I am a 16 year old with a laptop.


## Table of Contents


<ul>
    <li><a href="#Installation">Intallation</a></li>
    <li><a href="#Setup">Setup</a></li>
    <li><a href="#Usage">Usage</a></li>
    <li><a href="#Inspiration">Inspiration</a></li>
    <li><a href="#The-CAPTCHA-Problem">The CAPTCHA Problem</a></li>
    <li><a href="#Contact">Contact</a></li>
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

This step is fairly easy, all you're going to want to do is navigate to your command line and copy and paste the following command:

```shell
pip install tiktokscraper requests bs4 datetime unidecode
```

then, all you have to do is wait and then the requried packages should be installed and you should be ready for the next step


## Setup

Before you setup your ```.py``` file, I recomend creating a folder named ```Tiktok``` or something else that you'll remember. Make sure it's easily accessible.

Next, navigate to that folder (or whever you decide to put this file) and create a new python file. You can name it whatever you want, for this demonstration we'll call it ```tiktokwebscraper.py```

In this py file, copy and paste the following code in:

```python

from tiktokscraper import scrape

Tiktok = scrape.create()

```

And that's all you need to do to setup your webscraper!

Now do keep in mind that you can use this in any way in your own python scripts, however I just told you to make a new one just for the purposes of this demo.



## Usage

Whenever you call a function with this scraper, for example: 
```python
Tiktok.get_follwer_count('@example_user')
```
the value will be returned to you.

This means that if you want the value to be outputted to the console, you have to print it.

For our example, we'll simply set what gets returned to us into a variable, and print that:



```python
total_followers = Tiktok.get_follwer_count('@example_user')

print(total_followers)
```

This should be enough to get you started on incorporating this API into whatever programs you wish to make.

<br>

Full documentation available [here](#)


## Inspiration


I decided to work on this project mainly for myself, because I wanted to see who the most popular person that followed me on Tiktok was.

Initially, my plan was to write a simple app using the official Tiktok API that just checked the follower count for each of my followers but I soon came to realize that Tiktok had no official API

I had already heard about how it's possible to make API's for websites using a term what's known as [web-scraping](https://en.wikipedia.org/wiki/Web_scraping), however I didn't have any knowledge on the matter.
I then started doing research and came to the realization that it may be possible for me to try and make one.

I plan to continue updating this as I keep adding more and more features, and learn more about how websites handle data

## The CAPTCHA Problem


When I first started coding this bot I was faced with a big problem. As it turns out Tiktok doesn't like it when you pull a lot of data from them, so if you send a lot of get requests to their web servers, you will be profiled as a robot and asked to complete a [CAPTCHA](https://en.wikipedia.org/wiki/CAPTCHA).

<img src = "https://user-images.githubusercontent.com/50222899/128652952-6a8d19a6-de15-455b-a626-0f3903b47c7d.png">

This was bad news, a CAPTCHA is essentially a test web developers make for their users to make sure that the user is human and not a robot stealing their data. These tests usually include identifying common objects or typing letters that are played through speakers.

Now I've seen many different solutions to the CAPTCHA problem. (Some people actually have went through the trouble of using [machine learning](https://medium.com/@ageitgey/how-to-break-a-captcha-system-in-15-minutes-with-machine-learning-dbebb035a710) to solve captchas). Unfortunatly, (as much as I would love to), I do not have the neccesary resources to achieve a similar solution. I do have one thing that Tiktok unfortuantly doesn't have though; **A Brain**

<br>

I eventually realized that Tiktok only knows you need to be verified based off of your IP. My solution? **Proxies**

A quick google searched reaveled a website with a list of [free proxies](https://free-proxy-list.net/), and I then made the webscraper scrape this list of proxies, add them to a dictionary, and then choose a random one to use as a proxy whenever Tiktok asks for you to complete a CAPTCHA.

This may not be a solution as cool as artifical intelligence, however it's mine and I'm proud of it 

## Contact
You can email me at westonb.work@gmail.com
