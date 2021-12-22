class Node:
    def _init_(self, list):
        self.id = list["id"]
        self.pos = list["pos"]

    def _iter_(self):
        return self.inEdge

    def __repr__(self) -> str:
        return f"id={self.id} pos={self.pos}"
