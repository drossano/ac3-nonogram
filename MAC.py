from nonogram import Nonogram

class MAC:
    def __init__(self, nonogram):
        self.nonogram = nonogram
        self.all_variables = nonogram.row_possibilities
        self.col_constraints = nonogram.col_possibilities
        self.assigned = []
    
    def find_conflict(self, tail_index, tail, head_index, head):
        conflict = False
        # get row num of tail and head
        #for each value of tail and head
        for i in range(len(tail[0])):
            for column in self.col_constraints[i]:
                if column[tail_index] != tail[i] and column[head_index] != head[i]:
                    conflict = True
                    break
        return conflict
        #check if there's a column possibilty that matches those rows
        # ie first pair = first column indexed at those rows
    
    def revise(self, tail, head):
        '''
        checks if two rows can be part of a vaild column
        '''
        revised = False
        tail_values = getAllVariables()[tail]
        if len(tail_values) != 1:
            for tail_possibility in tail_values:
                supported = False
                for head_possibility in getAllVariables()[head]:
                    if self.find_conflict(tail, tail_possibility, head, head_possibility) == False:
                        supported = True
                        break
                    if supported == False:
                        tail_values.remove(0)
                        revised = True
        return revised

    def init_AC3(self):
        arcs = []
        row_index = 0
        for pos in self.all_variables.keys():
            for neigh in self.nonogram.get_neighbors(row_index).keys():
                arcs.append((neigh, pos))
            row_index += 1
        return arcs

def getAllVariables(self):
    return self.all_variables

    
nono = Nonogram("5x5.csv")
mac = MAC(nono)
#print(mac.all_variables)
print(mac.init_AC3())
                