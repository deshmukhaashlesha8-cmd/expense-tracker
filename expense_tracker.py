expenses = []

def add_expense():
    amount = float(input("enter amount:"))
    category = input("enter category:")
    description = input("enter description")

    expense = {
        "amount": amount,
        "category": category,
        "description": description
    }

    expenses.append(expense)
    print("expense added successfully")

def view_expenses():
    if len(expenses) == 0:
        print("no expense found")
        return

    for expense in expenses:
         print("")
         print("amount", expense["amount"])
         print("category", expense["category"])  
         print("description", expense["description"])     

def total_spending():
    total = 0

    for expense in expenses:
        total += expense["amount"]

    print("total spending",total)

def search_category():
    category = input("enter category to search")

    found = False

    for expense in expenses:
        if expense["category"].lower() == category.lower():
            print(expense)
            found = True

    if not found:
        print("no matching expenses found")


    while True:
      print("\n====== expense tracker ======")  
      print("1. add expense")
      print("2. view expense")
      print("3. total expense")       
      print("4. search category")
      print("5. exit")     

      choice = input("enter your choice")
     
      if choice == "1":
             add_expense()

      elif choice == "2":
             view_expenses()

      elif choice == "3":
             total_spending()

      elif choice == "4":
             search_category()

      elif choice == "5":
             print("goodbye")
             break

      else:            
              print("invalid choice")