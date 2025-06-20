from nonogram import Nonogram
from MAC import MAC
test_nono = Nonogram("5x5.csv")

def test_neighbors():
    test_nono = Nonogram("5x5.csv")
    num = 0
    assert test_nono.get_neighbors(0) == { 1: [[1, 1, 0, 0, 0], [0, 1, 1, 0, 0], [0, 0, 1, 1, 0], [0, 0, 0, 1, 1]], 2: [[1, 1, 1, 0, 0], [0, 1, 1, 1, 0], [0, 0, 1, 1, 1]], 3: [[1, 0, 1, 0, 0], [1, 0, 0, 1, 0], [1, 0, 0, 0, 1], [0, 1, 0, 1, 0], [0, 1, 0, 0, 1], [0, 0, 1, 0, 1]], 4: [[1, 0, 1, 0, 0], [1, 0, 0, 1, 0], [1, 0, 0, 0, 1], [0, 1, 0, 1, 0], [0, 1, 0, 0, 1], [0, 0, 1, 0, 1]]}

def test_get_columns():
    test_nono = Nonogram("5x5.csv")
    num = 1
    for row in test_nono.rows:
        row.append(num)
        num += 1
        row.append(num)
        num += 1
    print(test_nono.rows)
    assert test_nono.get_columns() ==  [[1,3,5,7,9],[2,4,6,8,10]]

def test_print_nonogram():
    test_nono = Nonogram("5x5.csv")
    test_nono.rows = [[1,0],[0,1]]
    assert test_nono.print_nonogram() == " # .\n . #\n"

def test_get_domain_size():
    test_nono = Nonogram("5x5.csv")
    assert test_nono.get_domain_size() == 5

def test_init_MAC():
    test_nono = Nonogram("5x5.csv")
    test_MAC = MAC(test_nono)
    assert test_MAC.nonogram == test_nono
    assert test_MAC.all_variables == test_nono.row_possibilities