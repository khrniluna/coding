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
        ("tuhan tolong yakinkan diriku", 0.1),
        ("bahwa dia bukan lah untukku?", 0.1),
        ("tolong hilangkan perasaan ku", 0.1),
        ("agar ku tak lagi memikirirkan dia", 0.2),
        ("telah ku coba melupakan diri mu", 0.08),
        ("namun apa daya hati ini sulit terima", 0.1),
        ("tuhan tolong yakinkan diriku", 0.1),
        ("bhawa dia bukan lah untukku", 0.1),
        ("tolong hilangkan perasaanku ", 0.1)
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
