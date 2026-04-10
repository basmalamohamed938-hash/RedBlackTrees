from .print_stats import print_stats

def load_from_file(dictionary, filename):
    """Load dictionary from text file (one word per line)."""
    try:
        with open(filename, 'r') as file:
            for line in file:
                word = line.strip()
                if word:  # Skip empty lines
                    # Check if word already exists (avoid duplicates)
                    if dictionary.tree.search(word) == "NO":
                        dictionary.tree.insert(word)
        print(f"Dictionary loaded successfully from {filename}")
        print_stats(dictionary)
    except FileNotFoundError:
        print(f"ERROR: File '{filename}' not found!")
    except Exception as e:
        print(f"ERROR loading file: {e}")
