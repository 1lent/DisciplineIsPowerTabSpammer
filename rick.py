import webbrowser
import time

def miku_sucks():
    timer = 0
    webbrowser.open("https://www.youtube.com/watch?v=_-2dIuV34cs")
    time.sleep(5)
    while timer < 250000:
        time.sleep(1)
        if (timer % 2) == 0:
            webbrowser.open_new("https://www.youtube.com/watch?v=9Deg7VrpHbM")
        else:
            webbrowser.open_new("https://www.youtube.com/watch?v=tvBQFon3yas")
        timer += 1
miku_sucks()