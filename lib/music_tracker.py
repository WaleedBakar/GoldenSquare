# x Method Design Recipe


## 1. Describe the Problem
# as a user we want to keep track of my music that im listening to
# i want to add tracks that ive listened to and see list 



## 2. Design the Method Signature

class MusicTracker:
    def __init__(self):
        # initialze an empty list to store tracks
        self.track_list = []

    def add_track(self, track_name: str) -> None:
        self.track_list.append(track_name)

    def get_track_list(self) -> list:

        return self.track_list


