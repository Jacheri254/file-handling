# File Creation
try:
    # Create a new text file named "my_file.txt" in write mode ('w')
    with open("my_file.txt", "w") as file:
        # Write at least three lines of text to the file
        file.write("This is line 1\n")
        file.write("Line 2: 12345\n")
        file.write("Another line - Line 3\n")
    print("File created successfully and initial content written.")
except Exception as e:
    print("An error occurred during file creation:", str(e))

# File Reading and Display
try:
    # Open and read the contents of "my_file.txt"
    with open("my_file.txt", "r") as file:
        # Display the contents on the console
        print("Contents of my_file.txt:")
        print(file.read())
except FileNotFoundError:
    print("The file 'my_file.txt' does not exist.")
except PermissionError:
    print("Permission denied to read the file.")
except Exception as e:
    print("An error occurred during file reading:", str(e))

# File Appending
try:
    # Open "my_file.txt" in append mode ('a')
    with open("my_file.txt", "a") as file:
        # Append three additional lines of text to the existing content
        file.write("Appended line 1\n")
        file.write("Line 6: New content\n")
        file.write("This is the last line\n")
    print("Additional content appended to the file.")
except Exception as e:
    print("An error occurred during file appending:", str(e))
finally:
    print("Task completed.")

# Error Handling
try:
    # Open a file that does not exist to trigger FileNotFoundError
    with open("nonexistent_file.txt", "r") as file:
        print(file.read())
except FileNotFoundError:
    print("FileNotFoundError: The specified file does not exist.")
except Exception as e:
    print("An error occurred:", str(e))
finally:
    print("Error handling completed.")
