import time
import webbrowser

my_breaks = 0
break_count = 1

while my_breaks < break_count:
    time.sleep(5)
    webbrowser.get('safari').open_new('www.youtube.com/watch?v=kDhptBT_-VI')
    my_breaks += 1