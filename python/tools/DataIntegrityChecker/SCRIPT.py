"""Create hash for each file in a directory and subdirectories to check for data integrity."""

# import modules
import os
import hashlib

# define function to create hash for each file in a directory and subdirectories.
# print and save the hash for each file in a directory and subdirectories in a dictionary.
# example of the creation print statements: file_name -> hash
# example of the check print statements: hash -> file_name : Bad (Hash doesn't match current) or Ok (Hash matches current) or ? (Missing data/file/hash)


# create two options for the user to choose from to either check the data integrity of a directory or to create the dictionary of hashes.
# use tkinter to ask for the directory path.