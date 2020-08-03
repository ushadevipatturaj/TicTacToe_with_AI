def tracklist(**tracks):
    for key, value in tracks.items():
        print(key)
        for key1, value1 in value.items():
            print("ALBUM:", key1, "TRACK:", value1)

tracklist(Woodkid={"The Golden Age": "Run Boy Run",
                   "On the Other Side": "Samara"},
          Cure={"Disintegration": "Lovesong",
                "Wish": "Friday I'm in love",
                "Seventeen Seconds": "A Forest"})