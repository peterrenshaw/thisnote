
     ________ __________  _  ______  __________
    /_  __/ // /  _/ __/ / |/ / __ \/_  __/ __/
     / / / _  // /_\ \  /    / /_/ / / / / _/  
    /_/ /_//_/___/___/ /_/|_/\____/ /_/ /___/  


![This Note](https://live.staticflickr.com/65535/50077822611_677cb12e23.jpg)

♬ ain't singin' for miller / don't sing for bud / I won't sing for politicians / ain't singin' for spuds / this note's for you ♬

I hate ADVERTS. I hate them so much I created a RaspberryPi PiHole to suck them away. I added a nifty Pimoroni InkyPHAT to display the results. Total rip-off of the fabulous InkyHole: https://github.com/neauoire/inky-hole

2020JUL05
* added image to README
- you can read more at [flickr]()

* cron added
- update 0600, 1200, 1800 and 2300 daily

  0 6,12,18,23 * * * /home/pi/work/thisnote/main.py

* added new logo
* cleaned up code
* checked onto laptop

2020JUL04
* getting there, cleaned up
* hacked around today 
- done... see the code with test.py

2020JUN25
* sorc

  <https://learn.pimoroni.com/tutorial/sandyj/getting-started-with-inky-phat>
  <https://github.com/pimoroni/inky/blob/master/library/inky/inky.py>
  <https://github.com/neauoire/inky-hole/blob/master/main.py>
  <https://learn.pimoroni.com/tutorial/sandyj/getting-started-with-inky-phat>
  <https://docs.python.org/3/howto/urllib2.html?highlight=urllib>
  <https://pillow.readthedocs.io/en/stable/reference/ImageFont.html>
  <https://pillow.readthedocs.io/en/stable/reference/ImageDraw.html>
  <https://www.dafont.com/font-comment.php?file=bebas_neue>

* bugs and problems galore
- not sure why not working
- tested against BLINKT so the GPIO pins are OK

* initial checkin
