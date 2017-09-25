Manjaro Dark Conky -Abhishek Munagekar
=======================================

![Screenshot](https://github.com/munagekar/MJRDarkConcky/blob/master/MJRDarkConky2.png)
This is a dark conky manager theme which was tested with the following concky version.

    conky 1.10.6_pre compiled Tue May 16 08:25:34 UTC 2017 for Linux 4.10.9-1-ARCH x86_64

This theme was tested on Ubuntu 14.04 LTS & Manjaro 17.0.5 64 bit XFCE but should work fine with any other distro and desktop environment.
It is fully modular and can be easily customized,comes with widgets for Time, Day of Week, Weather Forecast, News, And Real Time Bitcoin Value. I am also Planning to add a forex & live cricket & stock indice plugin. If you want a cool desktop definitely give this theme a try. This theme has been completely developed and expect no more future commits to this project unless something breaks

Wallpaper
---------

Use any dark wallpaper, should be really black. Texture & Gradients will look cool.
Any dark minimalistic wallpaper should also do
The Wallpaper shown in the screenshot is also attached however you can change it anything you prefer.
I have used the following wallpaper : https://pre00.deviantart.net/c84a/th/pre/f/2016/213/c/a/manjaro_monochrome_ws_wallpaper_by_rvc_2011-dac94gy.jpg
![Wallpaper](https://pre00.deviantart.net/c84a/th/pre/f/2016/213/c/a/manjaro_monochrome_ws_wallpaper_by_rvc_2011-dac94gy.jpg)

CPU Temperature Issues
-------------------
A minor correction is required in ~/.conky/AbhishekManjaro/temp. As a result a new ubuntu-temp file was created. Just replace the word temp with ubuntu-temp in the cmtheme file : ~/.conky/AbhishekManjaro/AbhishekManjaro.cmtheme and you should be good to go

Python Dependencies
-------------------

Make sure you have the following packages installed for Python2

    urllib
    json
    feedparser
    dateutil
    datetime
    bs4 (BeautifulSoup)
    

You can get them using pip.

Python Issues
-------------

Since Manjaro uses python3 by default and the theme has two python files which had to be called using python2.This would work perfectly fine with distros like Ubuntu and Manjaro(I have personally tested it). If you are using any other distro fire the command python2 and see if you get a Python 2 interpretter. 
Else make changes in the command python2 in the following files

    ~/.conky/TransparentTilesv3/weather_forecast
    ~/.conky/ConkyWhiteTilesv2/news
    ~/.conky/ConkyWhiteTilesv2/forex
    ~/.conky/ConkyWhiteTilesv2/stocks

New, Weather, Forex & Stock Indice Configurations
---------------------

I have fixed yahoo weather api issues.
News is retrieved from Times of India Headlines RSS feed
Weather is retrieved from Yahoo Weather. With City: Katraj Country:India
Forex converts USD to INR by default. This can easily be changed
BSE Indice is retrieved using Web Scrapping. You can easily scrape any other indice value using the current widget as a template. Programming knowledge is required for this modification.
You might want to change these settings in

    ~/.conky/AbhishekManjaro/weather.py

    ~/.conky/AbhishekManjaro/news.py
    
    ~/.conky/AbhishekManjaro/forex.py
   
   ~/.conky/AbhishekManjaro/stocks.py


Installation & Using the Theme
------------------------------

This theme has the following dependencies

 - Conky Package
 - Conky Manager
 - Python
 - Lua(Not sure possibly required by Conky)
Use your package manager to get theme if they aren't installed on your machine.

Clone the repository and copy the AbhishekManjaro folder into ~/.conky.

Manage Weather Configuration by making changes in `weather.py`

Manage News RSS stream by making changes in `news.py`

Make Forex Widget changes by making changes in `forex.py`

Make Stocks Widget changes by making changes in `stocks.py`
Note: I only provide Icon for indian rupee for forex widget. I would not be creating any additional icons. Anyone interested in creating icons should go ahead and fork this repository.
Finally select the theme using Conky Manager.



Screenshot
----------

This screenshot was taken on Manjaro 17.0.5 XFCE desktop so you might get slightly different results
I have also installed plank and set background to transparent for my dock.
The default XFCE Panel has been moved to the top & a small XFCE-Weather Widget is added to the top
And Numix Circular Icon Theme has been used to get circular icons.

Future Development
----------

 1. Addition of 2 and 8 core CPU Widget along with nvidia GPU widget from TeeJee Tech Theme

Version History

 - 1.0 : Came with Weather Forecast Widget , Modified Gotham Style Panel, Network Panel, Modified CPU Temperature Panel, News Widget.
 - 2.0 : Moved cache to AbhishekManjaro folder instead of /tmp. This corrects the weather bug, since weather data fetching requires internet. Now old weather data can be used till new data is fetched. 
   Cool New Real Time Bitcoin Price Widget. Reduced the size of theme by
   removing unnecessary files.
 - 2.0.1 : Bitcoin Update Time Bug Fixed & Minor Change in CPU Temp Gadget. 
  - 2.1 : New Forex Widget Added. Now see you a currency factor on your screen.
  - 2.2 : New Bear Icon Added. Coming soon a Stocks Widget. Minor Change in the Weather_Forecast
  - 3.0 : Battery Optimizations. New Bull Icon Added. Stocks(BSE) Widget Added. New Dependency: Beautiful Soup Python Package for Web Scrapping
  - 3.1 : Added support for Ubuntu after testing on a Ubuntu Machine. New Ubuntu Temperature Widget
  
