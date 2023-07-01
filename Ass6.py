def ds(roll_no, name):
    data_list = [roll_no, name]
    data_tuple = (roll_no, name)
    data_set = {roll_no, name}
    data_dict = {'roll_no': roll_no, 'name': name}

    # Printing the initial data structures
    print("Initial Data Structures:")
    print("List:", data_list)
    print("Tuple:", data_tuple)
    print("Set:", data_set)
    print("Dictionary:", data_dict)
    print()

    # Changing values during runtime
    new_roll_no = input("Enter new roll number: ")
    new_name = input("Enter new name: ")

    data_list[0] = new_roll_no
    data_list[1] = new_name

    # Tuple is immutable, so we need to create a new tuple
    data_tuple = (new_roll_no, new_name)

    data_set.remove(roll_no)
    data_set.add(new_roll_no)
    data_set.remove(name)
    data_set.add(new_name)

    data_dict['roll_no'] = new_roll_no
    data_dict['name'] = new_name

    # Printing the updated data structures
    print("Updated Data Structures:")
    print("List:", data_list)
    print("Tuple:", data_tuple)
    print("Set:", data_set)
    print("Dictionary:", data_dict)
    print()

    # Deleting the data structures
    del data_list
    del data_tuple
    del data_set
    del data_dict

    print("Data structures deleted.")


# Testing the function
ds(123, "John")
