import webbrowser
import time


def miku_sucks():
    timer = 0
    links = ["https://www.youtube.com/watch?v=9Deg7VrpHbM", "https://www.youtube.com/watch?v=tvBQFon3yas",
             "https://www.youtube.com/watch?v=4NaI0pTBJc8", "https://www.youtube.com/watch?v=gFPbjRdHWMY",
             "https://www.youtube.com/watch?v=Vp-TVkqaCrQ", "https://www.youtube.com/watch?v=QkCa--fyGjA",
             "https://www.youtube.com/watch?v=H5ExSyGTgt4", "https://www.youtube.com/watch?v=24XqFB3Ti9o",
             "https://www.youtube.com/watch?v=lEa21ZOStWQ", "https://www.youtube.com/watch?v=0FchHECNO74" ]

    webbrowser.open("https://www.youtube.com/watch?v=_-2dIuV34cs")
    time.sleep(30)
    while timer < 250000:  # fix later
        for x in links:
            webbrowser.open(x)
            time.sleep(3)
            timer += 1

miku_sucks()
