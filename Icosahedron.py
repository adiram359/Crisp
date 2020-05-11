import Object3D
import numpy as np
import Face


GOLDEN_RATIO = 1.61803398875


class Icosahedron(Object3D.Object3D):
    def __init__(self, x, y, z, edge_length):
        super().__init__(x, y, z)
        self.edge_length = edge_length
        self.name = "Icosahedron"
        self.faces = []
        self.create_faces(edge_length)

    def create_faces(self, edge_length):
        points = []
        options = [GOLDEN_RATIO / 2 * edge_length, 0, edge_length]
        self.create_vertices(options, points)
        print("Done")



    def create_vertices(self, options, points):
        for option1 in options:
            for option2 in options:
                if option1 != option2:
                    for option3 in options:
                        if option1 != option3 and option2 != option3:
                            points.append(np.array([option1, option2, option3]))



