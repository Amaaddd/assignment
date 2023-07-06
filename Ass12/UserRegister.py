def register():
    user = input("Enter Username: ")
    password = input("Enter Password: ")
    pos = input("Enter your Position in team: ")

    try:
        f = open("data.txt", "r")
        usernames = [line.split(",")[0] for line in f]
        # f.close()

        if user in usernames:
            print("Username already exists. Please choose a different username.")
            return

        f = open("data.txt", "a+")
        f.write(f"{user},{password},{pos}\n")
        # f.close()

        print("Welcome!")
    except FileNotFoundError:
        print("Error: 'data.txt' file not found.")
        return

# register()