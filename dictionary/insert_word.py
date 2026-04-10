from dictionary.print_stats import print_stats

def insert_word(dictionary, word):
    """Insert a single word into dictionary and update file."""
    # Check if word already exists
    if dictionary.tree.search(word):
        print(f"ERROR: Word '{word}' already in the dictionary!")
        return False
    
    # Insert into tree
    dictionary.tree.insert(word)
    
    # Append to dictionary file
    try:
        with open('dictionary.txt', 'a') as file:
            file.write(word + '\n')
        print(f"Word '{word}' inserted successfully!")
    except Exception as e:
        print(f"Warning: Could not update file - {e}")
    
    # Print statistics after insertion
    print_stats(dictionary)
    return True
