user_accounts_file = open('UserAccounts.csv')

for user_data in user_accounts_file:
    print(user_data)
    for data in user_data.split(","):
        print(data)

user_accounts_file.close()