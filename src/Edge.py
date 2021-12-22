class Edge:
    def _init_(self, list):
        self.src = list["src"]
        self.dest = list["dest"]
        self.w = list["weight"]
        self.Edgein = {}  # list of edge in
        self.Edgeout = {}  # list of edge out

    def _repr_(self):
        return f"src: {self.src} dest: {self.dest} weight: {self.w}"

    def _str_(self):
        return f"src: {self.src} dest: {self.dest} weight: {self.w}"



