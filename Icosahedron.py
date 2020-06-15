import Object3D
import numpy as np
from Face import Face



class Icosahedron(Object3D.Object3D):
    def __init__(self, x, y, z, edge_length):
        super().__init__(x, y, z, "block", "white")
        self.edge_length = edge_length
        self.name = "Icosahedron"
        self.faces = []
        self.create_faces(edge_length)

    def create_faces(self, edge):
        golden = 1.61803398875

        a = edge * np.array([0, 1, golden])
        b = edge * np.array([0, -1, golden])
        c = edge * np.array([0, 1, -golden])
        d = edge * np.array([0, -1, -golden])
        e = edge * np.array([1, golden, 0])
        f = edge * np.array([-1, -golden, 0])
        g = edge * np.array([1, -golden, -0])
        h = edge * np.array([-1, golden, 0])
        i = edge * np.array([golden, 0, 1])
        j = edge * np.array([-golden, 0, -1])
        k = edge * np.array([-golden, 0, 1])
        l = edge * np.array([golden, 0, -1])


        self.faces.append(Face([a, k, b]))
        self.faces.append(Face([b, a, i]))
        self.faces.append(Face([a, h, k]))
        self.faces.append(Face([a, e, i]))
        self.faces.append(Face([a, e, h]))
        self.faces.append(Face([h, c, e]))
        self.faces.append(Face([e, c, l]))
        self.faces.append(Face([e, l, i]))
        self.faces.append(Face([f, g, d]))
        self.faces.append(Face([j, d, f]))
        self.faces.append(Face([k, f ,j]))
        self.faces.append(Face([k, b, f]))
        self.faces.append(Face([i, l, e]))
        self.faces.append(Face([k, h, j]))

        self.faces.append(Face([b, g, i]))
        self.faces.append(Face([b, f, g]))
        self.faces.append(Face([i, l, g]))
        self.faces.append(Face([f, g, d]))
        self.faces.append(Face([g, d, l]))
        self.faces.append(Face([d, j, c]))
        self.faces.append(Face([d, c, l]))
        self.faces.append(Face([h, c, j]))
