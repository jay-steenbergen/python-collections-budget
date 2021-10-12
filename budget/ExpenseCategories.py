from . import Expense
import matplotlib.pyplot as plt

def main():
    expenses = Expense.Expenses()
    expenses.read_expenses('data/spending_data.csv')
    divided_for_loop = expenses.categorize_for_loop()
    divided_set_comp = expenses.catergorize_set_comprehesion()
    if divided_for_loop != divided_set_comp:
        print('Sets are NOT equal by == test')
    for a,b in zip(divided_for_loop,divided_set_comp):
        if no (a.issubset(b) and b.issubset(a)):
            print('Set are NOT equal by subset test')

if __name__ == "__main__":
    main()