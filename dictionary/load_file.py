def load_from_file(dictionary, filename):
    """Load dictionary from text file (one word per line)."""
    try:
        with open(filename, 'r') as file:
            for line in file:
                word = line.strip()
                if word:  # Skip empty lines
                    # Check if word already exists (avoid duplicates)
                    if not dictionary.tree.search(word):
                        dictionary.tree.insert(word)
        print(f"Dictionary loaded successfully from {filename}")
        _print_stats(dictionary)
    except FileNotFoundError:
        print(f"ERROR: File '{filename}' not found!")
    except Exception as e:
        print(f"ERROR loading file: {e}")

def _print_stats(dictionary):
    """Internal method to print statistics."""
    print("-" * 40)
    print(f"Dictionary Size: {dictionary.tree.get_size()} words")
    print(f"Tree Height: {dictionary.tree.get_height()}")
    print(f"Black Height: {dictionary.tree.get_black_height()}")
    print("-" * 40)