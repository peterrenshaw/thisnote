
     ________ __________  _  ______  __________
    /_  __/ // /  _/ __/ / |/ / __ \/_  __/ __/
     / / / _  // /_\ \  /    / /_/ / / / / _/  
    /_/ /_//_/___/___/ /_/|_/\____/ /_/ /___/  


♬ ain't singin' for miller / don't sing for bud / I won't sing for politicians / ain't singin' for spuds / this note's for you ♬

![The Third Watch](https://live.staticflickr.com/65535/50221760826_2ed4dceebe.jpg)

I hate ADVERTS. I hate them so much I created a RaspberryPi PiHole to suck them away. I added a nifty Pimoroni InkyPHAT to display the results. Total rip-off of the fabulous InkyHole.

2020AUG15
* defect: try/except called, no corresponding arg for print.
- noticed exception call, no matching arg.
- fix
* sys.exit
- change to 1, cause "Unix programs generally use 2 for command line syntax errors and 1 for all other kind of errors."

  <https://docs.python.org/3/library/sys.html?highlight=sys.exit#module-sys>

2020AUG13
* created a new set of images showing the watch
- the tools.py file contains datetime methods to 
  determine localtime. 
- dt_get_watch: works out which watch is current


    Watch       i24     24 Hour
    1           00      0000 - 0600   
    2           06      0600 - 1200
    3           12      1200 - 2100
    4           21      2100 - 0000

* added images to 'img' directory.
- call files img/fn 

* build image by adding watch number to the filename.
- file is called, fn = 'logoneek.png'
- file is called by 'watch #' + '-' + fn
- for first watch,  '1' + '-' + 'logoneek.png'
+ call '1-logoneek.png'
- for second watch, '2' + '-' + 'logoneek.png'
+ call '2-logoneek.png'
- etc..

* move images to img/

* testing

2020AUG12
* artwork to do
* testing required
* worked on
- watch logic to determine which image to display
- datetime functions

* sorc

    <https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior>
    <https://docs.python.org/3/library/time.html#time.struct_time>
    <http://pleac.sourceforge.net/pleac_python/datesandtimes.html>
    <https://learn.pimoroni.com/tutorial/sandyj/getting-started-with-inky-phat>


2020JUL05
* cleaned up code
* checked onto laptop

2020JUL04
* reminder for strftime
  <https://docs.python.org/3/library/time.html#time.strftime>

* this is the json feedback for http://127.0.0.1/admin/api.php

     {"domains_being_blocked":84597,"dns_queries_today":22814,"ads_blocked_today":4689,"ads_percentage_today":20.553169,"unique_domains":3011,"queries_forwarded":14586,"queries_cached":3539,"clients_ever_seen":4,"unique_clients":4,"dns_queries_all_types":22814,"reply_NODATA":3446,"reply_NXDOMAIN":232,"reply_CNAME":6648,"reply_IP":11554,"privacy_level":0,"status":"enabled","gravity_last_updated":{"file_exists":true,"absolute":1593883762,"relative":{"days":0,"hours":8,"minutes":39}}}


* soln for importlib for python3
  <https://stackoverflow.com/questions/2792650/import-error-no-module-name-urllib2>

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
