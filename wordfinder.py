"""Word Finder: finds random words from a dictionary."""
from random import choice, seed 

class WordFinder:
    
    """Methods for finding random words in a set dictionary
    
    >>> wf = WordFinder('/Users/lauren/Library/Mobile Documents/com~apple~CloudDocs/Documents/Springboard/python/python_object_orientation/python_oo_exercise/words.txt')
    235886 words read
    
    >>> isinstance(wf, WordFinder)
    True

    """
    def __init__(self, file):
        """Reads dict file and prints number of words in dict"""
        self.file=open(file)
        self.words=[word for word in self.file]
        print (f"{len(self.words)} words read")
        
    def __repr__(self):
        return f"Find random words in the dictionary at this file path: {self.file}"
        
    def random(self):
        """Picks random word from dictionary and returns it"""
        random_word=choice(self.words)
        without_space_char=random_word.replace("\n", "")
        return without_space_char

class SpecialWordFinder(WordFinder):
    """
    WordFinder that returns a word inside a cateogry

    
    """
    def category_words(self):
        cat_word=[word.strip() for word in words if not word.startswith('#') and word.startswith(' ')]        
        return cat_word
        
   
   
#    wf=WordFinder('/Users/lauren/Library/Mobile Documents/com~apple~CloudDocs/Documents/Springboard/python/python_object_orientation/python_oo_exercise/words.txt')

#swf=WordFinder('/Users/lauren/Library/Mobile Documents/co
#      ...: m~apple~CloudDocs/Documents/Springboard/python/python_obj
#      ...: ect_orientation/python_oo_exercise/complex.txt')