# Pie Break
#### An attention-grabbing break timer to keep you fresh.

pie_break optionally takes a number of minutes x and a url as arguments. It alerts you every time x minutes have passed by opening a random url in your default web browser. The default work time is 50 minutes.

<br>

## Requires
 - Python 3.8.13 (probably fine on earlier versions)
 - Optionally, a urls.txt file - containing space separated urls - placed in the same directory as pie_break.py. This feature has not yet been implemented in any useful way.

<br>

## Install and run

`pip install pie_break`

To be prompted for schedule details, run:

`piebreak`

Run with only a time to use the default url:

`piebreak 45`

or use your own:

`piebreak 90 https://bit.ly/1QVSIYb`

<br>


Improvements:
- Improve the readability of this readme and on pypi
- Add a reset command
- Fix: keyboardinterrupt is ignored
- Fix: cli runs without any schedulers after the timing is interrupted
- Refactor playlist integration
- Refactor for truly complex scheduling (APS[https://apscheduler.readthedocs.io/en/3.x/index.html])