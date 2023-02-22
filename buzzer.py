import RPi.GPIO as GPIO
import time
from datetime import datetime


BUZZER = 14
frequencies = {
    "a3f"  :  208,
    "b3f"  :  233,
    "b3"   : 247,
    "c4"   : 261,
    "c4s"  :  277,
    "e4f"  :  311,
    "f4"   : 349,
    "a4f"  :  415,
    "b4f"  :  466,
    "b4"   : 493,
    "c5"   : 523,
    "c5s"  :  554,
    "e5f"  :  622,
    "f5"   : 698,
    "f5s"  :  740,
    "a5f"  :  831,
    "rest"  :  -1
}

# Intro
intro_melody = ["c5s", "e5f", "e5f", "f5", "a5f", "f5s", "f5", "e5f", "c5s", "e5f", "rest", "a4f", "a4f"]
intro_rhythmn = [6, 10, 6, 6, 1, 1, 1, 1, 6, 10, 4, 2, 10]
lyrics_intro = ["", "", "", "", "", "", "", "", "", "", "", "", "", ""]

# verse
verse1_melody = [ "rest", "c4s", "c4s", "c4s", "c4s", "e4f", "rest", "c4", "b3f", "a3f",
                "rest", "b3f", "b3f", "c4", "c4s", "a3f", "a4f", "a4f", "e4f",
                "rest", "b3f", "b3f", "c4", "c4s", "b3f", "c4s", "e4f", "rest", "c4", "b3f", "b3f", "a3f",
                "rest", "b3f", "b3f", "c4", "c4s", "a3f", "a3f", "e4f", "e4f", "e4f", "f4", "e4f",
                "c4s", "e4f", "f4", "c4s", "e4f", "e4f", "e4f", "f4", "e4f", "a3f",
                "rest", "b3f", "c4", "c4s", "a3f", "rest", "e4f", "f4", "e4f"]

verse1_rhythmn = [ 2, 1, 1, 1, 1, 2, 1, 1, 1, 5,
  1, 1, 1, 1, 3, 1, 2, 1, 5,
  1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 3,
  1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 4,
  5, 1, 1, 1, 1, 1, 1, 1, 2, 2,
  2, 1, 1, 1, 3, 1, 1, 1, 3]

lyrics_verse1 = [ "We're ", "no ", "strangers ", "", "to ", "love ", "", "\r\n",
  "You ", "know ", "the ", "rules ", "and ", "so ", "do ", "I\r\n",
  "A ", "full ", "commitment's ", "", "", "what ", "I'm ", "thinking ", "", "of", "\r\n",
  "You ", "wouldn't ", "", "get ", "this ", "from ", "any ", "", "other ", "", "guy\r\n",
  "I ", "just ", "wanna ", "", "tell ", "you ", "how ", "I'm ", "feeling", "\r\n",
  "Gotta ", "", "make ", "you ", "understand", "", "\r\n", "", "", "", "", "", "", "", ""]

# Chorus
chorus_melody = ["b4f", "b4f", "a4f", "a4f",
                "f5", "f5", "e5f", "b4f", "b4f", "a4f", "a4f", "e5f", "e5f", "c5s", "c5", "b4f",
                "c5s", "c5s", "c5s", "c5s",
                "c5s", "e5f", "c5", "b4f", "a4f", "a4f", "a4f", "e5f", "c5s",
                "b4f", "b4f", "a4f", "a4f",
                "f5", "f5", "e5f", "b4f", "b4f", "a4f", "a4f", "a5f", "c5", "c5s", "c5", "b4f",
                "c5s", "c5s", "c5s", "c5s",
                "c5s", "e5f", "c5", "b4f", "a4f", "rest", "a4f", "e5f", "c5s", "rest"]

chorus_rhythmn = [ 1, 1, 1, 1,
  3, 3, 6, 1, 1, 1, 1, 3, 3, 3, 1, 2,
  1, 1, 1, 1,
  3, 3, 3, 1, 2, 2, 2, 4, 8,
  1, 1, 1, 1,
  3, 3, 6, 1, 1, 1, 1, 3, 3, 3, 1, 2,
  1, 1, 1, 1,
  3, 3, 3, 1, 2, 2, 2, 4, 8, 4
]

lyrics_chorus =["Never ", "", "gonna ", "", "give ", "you ", "up\r\n",
  "Never ", "", "gonna ", "", "let ", "you ", "down", "", "\r\n",
  "Never ", "", "gonna ", "", "run ", "around ", "", "", "", "and ", "desert ", "", "you\r\n",
  "Never ", "", "gonna ", "", "make ", "you ", "cry\r\n",
  "Never ", "", "gonna ", "", "say ", "goodbye ", "", "", "\r\n",
  "Never ", "", "gonna ", "", "tell ", "a ", "lie ", "", "", "and ", "hurt ", "you\r\n", "", ""]


def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(BUZZER, GPIO.OUT)
    GPIO.output(BUZZER, 0)

def buzz(noteFreq, duration):
    halveWaveTime = 1 / (noteFreq * 2 )
    waves = int(duration * noteFreq)
    for i in range(waves):
       GPIO.output(BUZZER, True)
       time.sleep(halveWaveTime)
       GPIO.output(BUZZER, False)
       time.sleep(halveWaveTime)

def play_rick(display):
    play_part(intro_melody, intro_rhythmn, lyrics_intro, display)
    play_part(verse1_melody, verse1_rhythmn, lyrics_verse1, display)
    play_part(chorus_melody, chorus_rhythmn, lyrics_chorus, display)
    play_part(chorus_melody, chorus_rhythmn, lyrics_chorus, display)


def play_part(notes, rhytm, lyrics, display):
    for idx, song_note in enumerate(notes):
        try:
            display.print_word(lyrics[idx])
        except Exception as e:
            print(e)
        buzz(frequencies[song_note], rhytm[idx] *0.05)
        time.sleep(rhytm[idx] *0.05)


if __name__ == "__main__":
    setup()
    from rick import Display
    display = Display()

    alarm_time = "23:00"
    last_time = None
    while True:
      now = datetime.now()
      current_time = now.strftime("%H:%M")

      if last_time != current_time:
          display.setup_display()
          display.print_clock(current_time)

      if current_time == alarm_time:
          while True:
            play_rick(display)

      last_time = current_time