def view_pos():
    f=open("data.txt","r+")
    for line in f:
        parts = line.split(",")
        username = parts[0]
        position = parts[2].strip()
        print(f"Username: {username},\n Position: {position}")
