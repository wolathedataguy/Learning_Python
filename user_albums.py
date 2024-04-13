def make_album(artist_name, album_title):
    """Build a dictionary describing a music album."""
    album = {
        'artist': artist_name,
        'title': album_title
    }
    return album

while True:
    print("Enter 'q' at any time to quit.")

    artist = input("Enter the artist's name: ")
    if artist == 'q':
        break
    
    title = input("Enter the album's title: ")
    if title == 'q':
        break

    album_info = make_album(artist, title)
    print(album_info)
