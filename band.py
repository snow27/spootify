
class Band:
    def __init__(self, name):
        self.name = name
        self.albums = []

    def add_album(self, album_name):
        if album_name in self.albums:
            return f"Band {self.name} already has {album_name.name} in their library."
        self.albums.append(album_name)
        return f"Band {self.name} has added their newest album {album_name.name}."

    def remove_album(self, album_name):
        for album in self.albums:
            if album_name == album.name:
                if album.published:
                    return "Album has been published. It cannot be removed."
                else:
                    self.albums.remove(album)
                    return f"Album {album_name} has been removed."

        return f"Album {album_name} is not found."


    def details(self):
        result = f"Band {self.name}\n"
        for album in self.albums:
            result += album.details()+"\n"
        return result

