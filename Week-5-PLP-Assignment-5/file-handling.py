# File Creation
try:
    with open("my_file.txt", "w") as file:
        file.write("This is line 1\n")
        file.write("2nd line with numbers: 123\n")
        file.write("Line 3: End of content\n")
        print("File 'my_file.txt' created successfully.")
except PermissionError:
    print("Permission denied. Cannot create the file.")
except Exception as e:
    print("An error occurred:", e)
finally:
    print("File creation process completed.\n")

# File Reading and Display
try:
    with open("my_file.txt", "r") as file:
        print("Contents of 'my_file.txt':")
        print(file.read())
except FileNotFoundError:
    print("File 'my_file.txt' not found.")
except PermissionError:
    print("Permission denied. Cannot read the file.")
except Exception as e:
    print("An error occurred:", e)
finally:
    print("File reading process completed.\n")

# File Appending
try:
    with open("my_file.txt", "a") as file:
        file.write("Appending line 4\n")
        file.write("Appending line 5\n")
        file.write("Appending line 6\n")
    print("Data appended to 'my_file.txt' successfully.")
except FileNotFoundError:
    print("File 'my_file.txt' not found.")
except PermissionError:
    print("Permission denied. Cannot append to the file.")
except Exception as e:
    print("An error occurred:", e)
finally:
    print("File appending process completed.")
