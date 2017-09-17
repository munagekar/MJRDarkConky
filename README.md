Manjaro Dark Conky -Abhishek Munagekar
=======================================

![Screenshot](https://github.com/munagekar/MJRDarkConcky/blob/master/MJRDarkConky.png)
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
I have used the following wallpaper : https://pre00.deviantart.net/c84a/th/pre/f/2016/213/c/a/manjaro_monochrome_ws_wallpaper_by_rvc_2011-dac94gy.jpg
![Wallpaper](https://pre00.deviantart.net/c84a/th/pre/f/2016/213/c/a/manjaro_monochrome_ws_wallpaper_by_rvc_2011-dac94gy.jpg)

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

 - Conky Package
 - Conky Manager
 - Python
 - Lua(Not sure possibly required by Conky)
Use your package manager to get theme if they aren't installed on your machine.

Extract the archive inside ~/.conky folder and use conky manager to select this theme.

Manage Weather Configuration by making changes in `~/.conky/TransparentTilesv3/weather.py`

Manage News RSS stream by making changes in `~/.conky/ConkyWhiteTilesv2/news.py`
And select the theme using Conky Manager.



Screenshot
----------

This screenshot was taken on Manjaro 17.04 XFCE desktop so you might get slightly different results
I have also installed plank and set background to transparent for my dock.
The default XFCE Panel has been moved to the top
And Numix Circular Icon Theme has been used to get circular icons.

Future Development
----------

 1. Ubuntu Fork for The Theme to make it easy for beginners. This more efforts on my parts as I will have to replicate the work there. - Low Priority
 2. Bitcoin Price Widget - High Priority
 3. Forex Widget - High Priority
 4. Repackaging the dependencies the folder and striping down the dependency folders to just required things. Currently its bloated & creates conflicts. - Low Priority

Version History
----------
 1.0 : Came with Weather Forecast Widget , Modified Gotham Style Panel, Network Panel, Modified CPU Temperature Panel, News Widget. 

