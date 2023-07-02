def file_operation(roll_no, name,stud_class, file="data.txt"):
    try:
        f=open(file, "w")
        pass
        f=open(file,"a")
        line=[f"{roll_no}, {name}, {stud_class}"]
        f.writelines(line)
        f=open(file,"r")
        data=f.readlines()
        print("Data is: ")

        print(data)

    except FileNotFoundError:
        print(f"{file} was not found....enter correct file name")

    except Exception:
        print("Something went wrong")
file_operation(42, "Amaad", "3rd Year")