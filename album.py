def make_album(artist_name, album_title, track_no=''):
    if track_no:
        album_info = {'Artist name': artist_name, 'Title of the album':album_title, 'Number of tracks':track_no}
        print(album_info)
        return album_info
    else:
        album_info = {'Artist name': artist_name, 'Title of the album':album_title}
        print(album_info)
        return album_info

make_album('Travis Scott', 'Astroworld')
make_album('Drake', 'For all the dogs in')
make_album('J. Cole', 'Might Delete Later')
make_album('Dave',  'PSYCHODRAMA', 11)