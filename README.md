Manjaro Dark Concky -Abhishek Munagekar
=======================================

![Screenshot](https://github.com/munagekar/MJRDarkConcky/blob/master/MJRDarkConcky.png)
This is a dark conky manager theme which was tested with the following concky version.

    conky 1.10.6_pre compiled Tue May 16 08:25:34 UTC 2017 for Linux 4.10.9-1-ARCH x86_64

This theme was tested on Manjaro 17.04 64 bit XFCE but should work fine with any other distro and desktop environment.

CMTHEME
-------

The cmtheme contents are as follows 

    ~/.conky/ConkyWhiteTilesv2/news
    ~/.conky/ConkyWhiteTilesv2/temp
    ~/.conky/Green Apple Desktop/Gotham
    ~/.conky/TeejeeTech/CPU Panel (4-core)
    ~/.conky/TeejeeTech/Network Panel
    ~/.conky/TeejeeTech/Process Panel
    ~/.conky/TransparentTilesv3/weather_forecast
    ~/.conky/AbhishekManjaro/wallpaper.jpg
    wallpaper-scaling:none

Wallpaper
---------

Use any dark wallpaper should be black. Texture & Gradients will look cool.
Any dark minimalistic wallpaper should also do
The Wallpaper is also attached
I have used the following wallpaper.
![Wallpaper](https://rvc-2011.deviantart.com/art/Manjaro-Monochrome-WS-Wallpaper-625242850)

Dependencies
------------

These have been attached in the zip file.

    ConkyWhiteTilesv2
    Green Apple Desktop
    Teejee Tech
    Transparent Tilesv3

I have changed the content of the files in these Themes & Widgets - Such as colors & broken widgets - Yahoo & News
You will have to overwrite these themes in case you already have these themes.
You could also create a backup in case you decide to revert back.

Python Dependencies
-------------------

Make sure you have the following packages installed for Python2

    urllib
    json
    feedparser

You can get them using pip.

Python Issues
-------------

Since Manjaro uses python3 by default and the theme has two python files which had to be called using python2 however is if you are using Ubuntu you will have to edit these files and use python instead of python 2.
Make changes in the following files

    ~/.conky/TransparentTilesv3/weather_forecast
    ~/.conky/ConkyWhiteTilesv2/news

News & Weather Issues
---------------------

I have fixed yahoo weather api issues.
News is retrieved from Times of India Headlines RSS feed
Weather is retrieved from Yahoo Weather. With City: Katraj Country:India
You might want to change these settings in

    ~/.conky/TransparentTilesv3/weather.py

    ~/.conky/ConkyWhiteTilesv2/news.py


Installation & Using the Theme
------------------------------

This theme has the following dependencies

Conky package 
Conky manager package
Python
Lua(Not sure but might be required)

Extract the archive the ~/.conky folder and use conky manager to select this theme.
Manage Weather Configuration by making changes in `~/.conky/TransparentTilesv3/weather.py`
Manage News RSS stream by making changes in `~/.conky/ConkyWhiteTilesv2/news.py`
And select the theme using Conky Manager.



Screenshot
----------

This screenshot was taken on Manjaro 17.04 XFCE desktop so you might get slightly different results
I have also installed plank and set background to bg for my dock.
The default XFCE Panel has been moved to the top
And Numix Circular Icon Theme has been used to get circular icons.




