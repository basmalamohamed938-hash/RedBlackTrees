def lookup_word(dictionary, word):
    if not word:
        result = dictionary.tree.search(word)
        if result:
            print(f"YES the '{word}' is found")
            return
    print(f"NO the '{word}' is not found")
