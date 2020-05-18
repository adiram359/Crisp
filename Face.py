class Face:

    def __init__(self, _vertices):
        self.vertices = _vertices
        self.color = "white"

    def set_color(self, color):
        self.color = color


def face_sort(f):
    return f.vertices[2]
