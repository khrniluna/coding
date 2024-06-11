import time
from threading import Thread, Lock
import sys

lock = Lock()

def animate_text(text, delay=0.1):
    with lock:
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(delay)
        print()

def sing_lyric(lyric, delay, speed):
    time.sleep(delay)
    animate_text(lyric, speed)

def sing_song():
    lyrics = [
        ("ku tak pandai berdusta", 0.1),
        ("jujur saja kau boleh juga", 0.1),
        ("tak bisa ku pungkiri", 0.1),
        ("hati nyaman tiap kau ada", 0.2),
        ("caramu tersenyum", 0.08),
        ("tertawa dan merangkai canda", 0.1),
        ("buatku terpesona", 0.1),
        ("dan dapat kau baca", 0.1),
        ("mataku bicaraaaaaaa", 0.1)
    ]
    delays = [0.3, 5.0, 10.0, 15.0, 20.3, 25.0, 27.0, 30.2, 33.3]
    
    threads = []
    for i in range(len(lyrics)):
        lyric, speed = lyrics[i]
        t = Thread(target=sing_lyric, args=(lyric, delays[i], speed))
        threads.append(t)
        t.start()
    
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    sing_song()
