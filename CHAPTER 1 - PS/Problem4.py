import os

current_directory = os.getcwd()
print(f"Contents of directory: {current_directory}")

for item in os.listdir(current_directory):
    print(item)
