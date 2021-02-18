accounts = [("Guido", 2000, 500), ("Raymond", -52, 1000), ("Jack", 900, 1000), ("Brandon", 2000, 0)]

proper_accounts = {
    t[0]:t[1] for t in accounts
    if t[1] >= t[2]
}

print(proper_accounts)