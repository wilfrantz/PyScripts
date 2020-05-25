#!/usr/bin/env python3

 #* Typo generator Python command-line application.
 #* Wilfrantz DEDE - May 2020

import sys 


# Create Typo in the stream and send to stdout
def __makeTypo__(stream):
    for word in stream[1:]:
        size = len(word)
        if (size >= 6): # target 6(or more) char long words.
            for c in range(size):
                print(word)
    print(f"\nTypo: \n")

# main:
def __main__():
    argc = int(len(sys.argv) - 1)
    if (argc < 2 and argc >=10):
        print("String too long!!! must be <= 10\n")
        sys.exit(-1)

    # Converts the list to a string.
    stream = " ".join(sys.argv[1:])
    print(f"\nInitial input:\n{stream}")

    __makeTypo__(sys.argv)

if __name__ == "__main__":
    __main__()


