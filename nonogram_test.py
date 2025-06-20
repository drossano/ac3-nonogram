from nonogram import Nonogram
test_nono = Nonogram("5x5.csv")

def test_neighbors():
    test_nono = Nonogram("5x5.csv")
    num = 1
    for row in test_nono.rows:
        row.append(num)
        num += 1
    assert test_nono.get_neighbors(0) == [[2],[3],[4],[5]]

def test_get_columns():
    test_nono = Nonogram("5x5.csv")
    num = 1
    for row in test_nono.rows:
        row.append(num)
        num += 1
        row.append(num)
        num += 1
    print(test_nono.rows)
    assert test_nono.get_columns(test_nono.rows) ==  [[1,3,5,7,9],[2,4,6,8,10]]