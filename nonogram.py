import csv
class Nonogram:
    def __init__(self,nono_file):
        self.clues = dict()
        print(nono_file)
        self.clues = self.generate_clues(nono_file)

    def generate_clues(self, filename):
        row_clues = []
        col_clues = []
        with open(filename, newline = '') as f:
            reader = csv.reader(f)
            for row in reader:
                row_clues.append(row[0].split(' '))
                col_clues.append(row[1].split(' '))
        return {'row':row_clues, 'col': col_clues}       
nonogram = Nonogram('5x5.csv')
print(nonogram.clues)