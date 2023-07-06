def view_team():
    f=open("data.txt","r")
    username = [line.split(",")[0] for line in f]
    for name in username:
        print(f"Team members are: \n{name}")
