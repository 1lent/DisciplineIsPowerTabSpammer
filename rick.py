import webbrowser
import time

timer = 0

webbrowser.open("https://www.youtube.com/watch?v=_-2dIuV34cs")
time.sleep(60)
while timer < 100:
    time.sleep(1)
    webbrowser.open("https://www.youtube.com/watch?v=AbtpZvC8aT4")
    timer = timer + 1