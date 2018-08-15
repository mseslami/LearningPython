'''
In this exercise we are going to hava a database of book based on dictionary
with id as key and a name as writer's name.
it should support CRUD (create, read, update, delete).
'''

import ast
import os
import json

current_directory = os.getcwd()
final_directory = os.path.join(current_directory)

''' add_data() get a bookid as id for book and writername as name of the writer then creates a dictionary
and update a datafiele.txt if it exists, else create datafile.txt then write into it.'''


def add_data():
    bookid = input("Enter book id")
    writername = input("Enter writer's name")
    with open(final_directory + "/datafile.txt", mode="a+") as datafile:
        datafile.write(str({"id": bookid, "writer'sname": writername}) + "\n")


''' delete() get a bookid of user then deletes it. deleting process is:
reading and storing all items from datafile.txt , then erase datafile.txt by oppeing it in mood="w",
then add all stored items except the item which should be deleted.'''


def delete():
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


''' edit() get a bookid and newname of user then update the book with book id by newname. 
editing process is:
reading and storing all items from datafile.txt , then erase datafile.txt by oppeing it in mood="w",
then add all stored items normally except the item which should be edited. It will be updated then
add to datafile.txt'''


def edit():
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


'''read() prints all items in datafile.txt by converting every item to string '''


def read():
    with open(final_directory + "/datafile.txt", mode="a+") as datafile:
        datafile.seek(0)
        for item in datafile.readlines():
            mydict = ast.literal_eval(item)  # converts string ot dict
            print("book id is: ", (mydict["id"]), " and writer's name is ", (mydict["writer'sname"]))

            # for item2 in jsonobject:
            # print(jsonobject)
            # jsonobject = json.encoder(datafile)
            # print(jsonobject)


'''use try_again() when user enter something irrelevent'''


def try_again():
    print("try again")


if __name__ == '__main__':

    while True:
        selection = input("--------------------------\nEnter{:< 3d} to add or\nenter{:< 3d} to delete or\nenter{:< 3d} "
                          "to edit or\nenter{:< 3d} to read\n ".format(1, 2, 3, 4))

        selectiondic = {"1": add_data,
                        "2": delete,
                        "3": edit,
                        "4": read}

        dict.get(selectiondic, selection, try_again)()
        mycontinue = input("enter [Y/n] to continue or stop")
        if mycontinue == "Y":
            continue
        elif mycontinue == "n":
            break
        else:
            print("enter Y or n")

# package import json dump o loads
