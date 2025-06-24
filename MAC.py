from nonogram import Nonogram
import copy

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
        test_board = copy.deepcopy(self.nonogram.rows)
        test_board[tail_index] = tail
        test_board[head_index] = head

        # check if each column of the test board is valid
        valid_column = True
        # for each column_index in columns:
        for column_index in range(len(tail)):
            column_possibilities = self.col_constraints[column_index]
            #   for each column_possibulity in column_index
            for column_possibility in column_possibilities:
        #       if each cell in column_pos == each row on test board at column index
                for row_index in range(len(column_possibility)):
                    # if test board has data in this row check if it matches the coloumn, if not go to next row
                    if test_board[row_index]:
                        # if the row position in the column matches the test board go to the next row
                        # if not try a different column
                        # if we exhaust all the cloumn possibilities and there's no match there's a conflict
                        # if all the rows in a column possibilitiy match move to the next column
                        if column_possibility[row_index] != test_board[row_index][column_index]:
                                if column_possibilities.index(column_possibility) + 1 == len(column_possibilities):
                                    return True
                                else:
                                    break
                        elif row_index + 1 == len(column_possibility):
                            break
        #           if each index has a vald possibility return false
        #       if all column possibilities in cofumn index are conflicts break and return true
                    # return True
        return conflict





        # for i in range(len(tail)):
        #     valid_columns = 0
        #     for column in self.col_constraints[i]:
        #         for j in range(len(test_board)):
        #             if test_board[j] and column[j] != test_board[j][i]:
        #                 break

        # if valid_columns == 5:
        #     return False
        # else:
        #     return True
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
nono = Nonogram("5x5.csv")
mac = MAC(nono)
#print(mac.all_variables)
if mac.init_AC3() and mac.search():
    print("Solution found")
    nono.print_nonogram()
else:
    print("Can't find solution")
                