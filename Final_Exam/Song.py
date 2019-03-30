"""
Song
"""

class Song:
    def __init__(self, name):
        self.name = name
        self.next = None
        
    def next_song(self, song):
        self.next = song

    def is_repeating_playlist(self):
        """
            :returns: (bool) True if the playlist is repeating, False if not.
         """

        # Assumes that the first song is unique in the playlist
        if(self.next is None):
            return False
        first_name = self.name
        temp = self.next
        while temp:
            if(temp.name != first_name):
                if(temp.next is not None):
                    temp = temp.next
                else:
                    return False
            else:
                return True
                
        return None

first = Song("Hello")
second = Song("Eye of the tiger")
third = Song("Third Eye")

first.next_song(second)
second.next_song(third)
third.next_song(first)

print(first.is_repeating_playlist())
# This should return True
