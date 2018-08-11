import ast
import os

current_directory = os.getcwd()
final_directory = os.path.join(current_directory)


def Add_Data():
    bookid = input("Enter book id")
    writername = input("Enter writer's name")
    with open(final_directory + "/datafile.txt", mode="a+") as datafile:
        datafile.write(str({"id": bookid, "writer'sname": writername}) + "\n")


def Delete():
    itemtodelete = input("Enter book id to delete it")
    with open(final_directory + "/datafile.txt", mode="r+") as datafile:
        datafile.seek(0)
        mylist = datafile.readlines()
    # reopen it (with "w" mood) to erase file:
    with open(final_directory + "/datafile.txt", mode="w") as datafile:
        for item in mylist:
            mydict = ast.literal_eval(item)  # converts string ot dict
            if not (itemtodelete == mydict["id"]):
                datafile.write(item)
            else:
                print("Item is deleted")


def Edit():
    itemtoedit = input("Enter book id to edit it")
    newname = input("Enter new writer's name")
    with open(final_directory + "/datafile.txt", mode="r+") as datafile:
        datafile.seek(0)
        mylist = datafile.readlines()
    # reopen it (with "w" mood) to erase file:
    with open(final_directory + "/datafile.txt", mode="w") as datafile:
        for item in mylist:
            mydict = ast.literal_eval(item)  # converts string ot dict
            if not (itemtoedit == mydict["id"]):
                datafile.write(item)
            else:
                (mydict["writer'sname"]) = newname
                datafile.write(str(mydict) + "\n")
                print("Item is updated")


def Read():
    with open(final_directory + "/datafile.txt", mode="a+") as datafile:
        datafile.seek(0)
        for item in datafile.readlines():
            mydict = ast.literal_eval(item)  # converts string ot dict
            print("book id is: ", (mydict["id"]), " and writer's name is ", (mydict["writer'sname"]))


def Try_again():
    print("try again")


if __name__ == '__main__':

    while True:
        selection = input("--------------------------\nEnter{:< 3d} to add or\nenter{:< 3d} to delete or\nenter{:< 3d} "
                          "to edit or\nenter{:< 3d} to read\n ".format(1, 2, 3, 4))

        selectiondic = {"1": Add_Data,
                        "2": Delete,
                        "3": Edit,
                        "4": Read}

        dict.get(selectiondic, selection, Try_again)()
        mycontinue = input("enter [Y/n] to continue or stop")
        if mycontinue == "Y":
            continue
        elif mycontinue == "n":
            break
        else:
            print("enter Y or n")

# package import json domp o loads
