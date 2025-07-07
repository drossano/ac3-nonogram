from nonogram import Nonogram
import time
import copy
import sklearn.metrics

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
        for i in range(len(tail)):
            column_possibilities = self.col_constraints[i]
            for column in column_possibilities:
                if column[tail_index] != tail[i] or column[head_index] != head[i]:
                    # if last column possibility return true
                    if column_possibilities.index(column) + 1 == len(column_possibilities):
                        return True
                    # try another column if there's a conflict
                    else:
                        continue
                    
                else:
                    break
        return conflict
        #check if there's a column possibilty that matches those rows
        # ie first pair = first column indexed at those rows
    def revise(self, tail, head):
        '''
        checks if two rows can be part of a vaild column
        '''
        revised = False
        tail_values = self.getAllVariables()[tail]
        valid = copy.copy(tail_values)
        if len(valid) != 1:
            for tail_possibility in tail_values:
                supported = False
                for head_possibility in self.getAllVariables()[head]:
                    if self.find_conflict(tail, tail_possibility, head, head_possibility) == False:
                        supported = True
                        break
                if supported == False:

                    valid.remove(tail_possibility)
                    revised = True
        else:
            # locks in row for tail with 1 possibility
            self.nonogram.rows[tail] = valid[0]
        self.getAllVariables()[tail] = valid   
        return revised

    def init_AC3(self):
        arcs = []
        row_index = 0
        for pos in self.all_variables.keys():
            for neigh in self.nonogram.get_neighbors(row_index).keys():
                arcs.append((neigh, pos))
            row_index += 1
        return self.AC3(arcs)
    
    def AC3(self, arcs):
        
        while True:
            current_arc = arcs.pop(0)
            if self.revise(current_arc[0], current_arc[1]) == True:

                if len(self.getAllVariables()[current_arc[0]]) == 0:
                    return False
                else:
                    neighbors = self.nonogram.get_neighbors(current_arc[0])
                    # neighbors.remove(current_arc[1])
                    del neighbors[current_arc[1]]
                    for neighbor in neighbors:
                        new_arc = (neighbor, current_arc[0])
                        arcs.append(new_arc)
            if len(arcs) < 1:
                break
        return True
        

    def search(self):
        n = self.select_unassigned()
        if n == None:
            return True
        self.assigned.append(n)
        print(f"{n}, {len(self.assigned)}")
        while self.all_variables[n]:
            value = self.all_variables[n].pop(0)
            all_var_copy = copy.deepcopy(self.all_variables)
            self.all_variables[n].clear()
            self.all_variables[n].append(value)
            arcs = []

            for neighbors in self.nonogram.get_neighbors(n):
                arcs.append((neighbors, n))
            if self.AC3(arcs) and self.search():
                return True
            else:
                print(f"{n}  reverting")
                self.all_variables = all_var_copy
        self.assigned.remove(n)
        return False

    def getAllVariables(self):
        return self.all_variables
    
    def is_assigned(self, var):
        return var in self.assigned

    def select_unassigned(self):
        smallest_var = None
        for var in self.all_variables.keys():
            if self.is_assigned(var) == False:
                if smallest_var == None:
                    smallest_var = var
                elif len(self.all_variables[var]) < len(self.all_variables[smallest_var]):
                    smallest_var = var
        return smallest_var
    
    
