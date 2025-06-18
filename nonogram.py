import csv
from itertools import combinations
class Nonogram:
    def __init__(self,nono_file):
        self.clues = dict()
        print(nono_file)
        self.clues = self.generate_clues(nono_file)
        self.row_possibilities = self.generate_possibilities(self.clues['row'], len(self.clues['row']))
        self.col_possibilities = self.generate_possibilities(self.clues['col'], len(self.clues['col']))

    def generate_clues(self, filename):
        row_clues = []
        col_clues = []
        with open(filename, newline = '') as f:
            reader = csv.reader(f)
            for row in reader:
                row_clues.append(list(map(int,row[0].split(' '))))
                col_clues.append(list(map(int, row[1].split(' '))))
        return {'row':row_clues, 'col': col_clues}      

    def generate_possibilities(self, clues, no_cells):
        '''
        Using clues create possible lines()
        1 represents filled square, 0 represents blank
        '''
        possibilities = []
        for clue in clues:
            segments = len(clue)
            no_empty_cells = no_cells-sum(clue) - segments + 1
            filled = [[1] * value for value in clue]
            for p in combinations(range(segments+no_empty_cells), segments):
                selected = [-1]*(segments+no_empty_cells)
                filled_idx = 0
                for val in p:
                    selected[val] = filled_idx
                    filled_idx += 1

                res_opt = [filled[val]+[0] if val > -1 else [0] for val in selected]
                res_opt = [item for sublist in res_opt for item in sublist][:-1]
                possibilities.append(res_opt)
        return possibilities
            
nonogram = Nonogram('5x5.csv')
print(nonogram.row_possibilities)
print(nonogram.col_possibilities)