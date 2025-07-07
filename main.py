from nonogram import Nonogram
import MAC
import time
import glob
from sklearn.metrics import accuracy_score
def  main():
    directory = ('nonograms/15x15')
    nono = Nonogram(f"{directory}/*.csv")
    mac = MAC.MAC(nono)
    start_time = time.time()
    #print(mac.all_variables)
    if mac.init_AC3() and mac.search():
        elapsed_time = time.time() - start_time
        print("Solution found")
        print(f"Runtime: {elapsed_time}" )
        solution = nono.print_nonogram()
        print(nono.print_nonogram())
        print(f"Accuracy: {get_accuracy(solution, directory) * 100} %")
    else:
        print("Can't find solution")

def  get_real_solution(filepath):
    solution = None
    with open(filepath, newline = '') as f:
        solution = f.read()
    return solution.split()

def get_accuracy(solution, directory):
    test_solution_list = solution.split()
    real_solution = get_real_solution(glob.glob(f'{directory}/*.txt')[0])
    return accuracy_score(test_solution_list, real_solution)
    
main()
                