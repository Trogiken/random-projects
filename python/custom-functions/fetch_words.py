def fetch_words(file):
    """Read all words in a file and return in list format"""
    words = []
    try:
        with open(f"{file}", 'r') as f:
            raw_words = f.read().splitlines()
            for item in raw_words:
                if item:
                    for char in item:
                        if char.isalpha():
                            continue
                        else:
                            input(f"Letters Only! - [{item}]\nPress Enter to Exit")
                            exit()
                    words.append(item)
            if words:
                return words
            else:
                input("Words list Empty!\nPress Enter to Exit")
                exit()
    except FileNotFoundError:
        input("Words File Not Found\nPress Enter to Exit")
        exit()
