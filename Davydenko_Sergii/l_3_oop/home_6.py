from context_manager_account import Account

with Account('Itea', 100500) as transactions:
    transactions.add_transaction(50)
    transactions.add_transaction(20)
    transactions.add_transaction(30)
    transactions.print_method()
    del transactions._copy_transactions
