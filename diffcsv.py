#!/usr/bin/python3

import csv, sys, getopt

def logo():
    print('''
##############################################################
##############################################################
#
# PYTHON 3
# CSV DIFF SCRIPT v0.2
# Created by: Andrew Sturm
# Created on: 2020-07-14
#
##############################################################
##############################################################

GitHub: https://www.github.com/deadeye007/diffcsv.git

''')


def main(argv):
    firstInput = ''
    secondInput = ''
    firstOutput = ''

# Check for the correct arguments
    try:
        opts, args = getopt.getopt(argv,"1:2:ho:v",["help","version"])
    except getopt.GetoptError:
        print("Invalid argument.\n\nUsage: diffcsv -1 file1 -2 file2 -o file3")
        exit()

# Get opt cases
    for opt, arg in opts:
        if opt in "-1":
            firstInput = arg
        elif opt in "-2":
            secondInput = arg
        elif opt in ("-h","--help"):
            print("Usage: diffcsv -1 file1 -2 file2 -o file3")
            exit()
        elif opt in "-o":
            firstOutput = arg
        elif opt in ("-v","--version"):
            logo()
            exit()

# Attempt to open the CSV to diff them
    try:
        print("Comparing "+firstInput+" with "+secondInput+"\nOutput: "+firstOutput)
        with open(firstInput, newline='') as t1, open(secondInput, newline='') as t2:
            reader = csv.reader(t2)
            fieldname = next(reader)
            oldFile = t1.readlines()
            newFile = t2.readlines()

        with open(firstOutput, 'w') as outFile:
            writer = csv.DictWriter(outFile, fieldnames=fieldname)
            writer.writeheader()
            for line in newFile:
                if line not in oldFile:
                    outFile.write(line)

    except TypeError:
        tb = sys.exc_info()[2]
        raise NotImplementedError().with_traceback(tb)
        exit(2)

    except KeyboardInterrupt:
        print("Keyboard interrupt sequence initiated. Exiting...")
        exit()


if __name__ == "__main__":
    main(sys.argv[1:])
