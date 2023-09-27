from lib.music_tracker import MusicTracker

def test_add_track():
    # test adding tracks and getting the etrack list
    music_tracker = MusicTracker()
    music_tracker.add_track("Track 1")
    music_tracker.add_track("Track 2")
    track_list = music_tracker.get_track_list()
    assert track_list == ["Track 1", "Track 2"]

def test_add_empty_track():
    music_tracker = MusicTracker()
    music_tracker.add_track("Track 1")
    music_tracker.add_track("Track 2")
    music_tracker.add_track("")
    track_list = music_tracker.get_track_list()
    assert track_list == ["Track 1", "Track 2", ""]

    def test_add_tracks_with_special_characters():
        music_tracker = MusicTracker()
        music_tracker.add_track("Track $#!")
        music_tracker.add_track("Track 3")
        Track_list = music_tracker.get_track_list()
        assert track_list == ["Track $#!", "Track 3"]

    def test_get_track_list_from_empty_tracker():
        empty_tracker = MusicTracker()
        empty_tracker = empty_tracker.get_track_list()
        assert empty_track_list == []