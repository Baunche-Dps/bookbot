def main():
    print("Starting the main function.")
    try:
        with open("books/frankenstein.txt") as f:
            file_contents = f.read()
            words = len(file_contents.split())
            char_counts = {}
            for char in file_contents:
                if char.isalpha():
                    char = char.lower()
                    if char in char_counts:
                        char_counts[char] += 1
                    else:
                        char_counts[char] = 1
            print("File contents length:", len(file_contents))
            print(file_contents)
            print("File read successfully.")
            print(f"This book was {words} words long!")
            print('--- Begin report of books/frankenstein.txt ---')
            for char, count in sorted(char_counts.items()):
                print(f"The '{char}' character was found {count} times")
            print ("--- End of report ---")
    except FileNotFoundError:
        print("The file was not found. Please check the file path.")

if __name__ == "__main__":
    main()