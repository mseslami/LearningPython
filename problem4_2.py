'''
Question: difference between readlines() in w+ mode and r mode?
Answer:
as we know:
``r''   Open text file for reading.  The stream is positioned at the
         beginning of the file.
``w+''  Open for reading and writing.  The file is created if it does not
         exist, otherwise it is truncated.  The stream is positioned at
         the beginning of the file.
so by opening file in r mode, we can read lines normally but
in w+ mode, file will be truncated, and there is nothing to show.
you can test above answer by below code:
'''

import os

# select a path where .txt file will be located
current_directory = os.getcwd()
final_directory = os.path.join(current_directory)

# create and open file and write some lines into it
#  then read what you have written:
with open(final_directory + "/test.txt", mode="+w") as myfile:
    myfile.writelines("a a\nb b\nc c\nd d\n")
    myfile.seek(0)
    for line in myfile.readlines():
        print(line)

# open in r mode and see lines:
with open(final_directory + "/test.txt", mode="r") as mylifle3:
    print("mode r:")
    mylifle3.seek(0)
    for line in mylifle3.readlines():
        print(line)

# open in +w mode and see nothing!
with open(final_directory + "/test.txt", mode="+w") as mylifle2:
    print("mode +w:")
    mylifle2.seek(0)
    for line in mylifle2.readlines():
        print(line)
