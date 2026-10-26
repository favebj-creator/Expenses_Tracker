print("======== EXPENSE TRACKER ==========")
name = "constance"
budget_salary = 20000
food = 20000
internet = 10000
transportation = 30000
total_expense = (food+internet+transportation)
amount_remaining = (budget_salary - total_expense)
print("name =", name, 
      "\nbudget salary =", budget_salary,
        "\nfood =", food,
        "\ninternet =" , internet,
        "\ntransportation =", transportation,
        "\ntotal expense =", total_expense,
        "\namount remaining =", amount_remaining)
if budget_salary > total_expense:
    print("constance is in her budget")
elif budget_salary < total_expense:
    print("constance expense pass income")