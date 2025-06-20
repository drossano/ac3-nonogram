from nonogram import Nonogram

class MAC:
    def __init__(self, nonogram):
        self.nonogram = nonogram
        self.all_variables = nonogram.row_possibilities
        self.assigned = []
    
    def revise(self, tail, head):
        '''
        checks if two rows can be part of a vaild column
        '''
        revised = False
        if len(tail) != 0:
            

    def init_AC3(self):
        arcs = []
        row_index = 0
        for possibilities in self.all_variables:
            for neighbors in self.nonogram.get_neighbors(row_index):
                arcs.append((possibilities, neighbors))
            row_index += 1
        return arcs
nono = Nonogram("5x5.csv")
mac = MAC(nono)
#print(mac.all_variables)
print(mac.init_AC3())
                