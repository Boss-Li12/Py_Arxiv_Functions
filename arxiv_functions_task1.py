"""CSC108: Fall 2021 -- Assignment 3: arxiv.org

This code is provided solely for the personal and private use of
students taking the CSC108/CSCA08 course at the University of
Toronto. Copying for purposes other than this use is expressly
prohibited. All forms of distribution of this code, whether as given
or with any changes, are expressly prohibited.

All of the files in this directory and all subdirectories are:
Copyright (c) 2021 Anya Tafliovich, Michelle Craig, Tom Fairgrieve, Sadia
Sharmin, and Jacqueline Smith.
"""

# importing copy for use in the keep_prolific_authors docstring
# you do not need to use it anywhere else
import copy  
from typing import Dict, List, TextIO

from constants import (ID, TITLE, CREATED, MODIFIED, AUTHORS, ABSTRACT, END, 
                       NameType, ArticleValueType, ArticleType, ArxivType)


EXAMPLE_ARXIV = {
    '031': {
        ID: '031',
        TITLE: 'Calculus is the Best Course Ever',
        CREATED: '',
        MODIFIED: '2021-09-02',
        AUTHORS: [('Breuss', 'Nataliya')],
        ABSTRACT: 'We discuss the reasons why Calculus is the best course.'},
    '067': {
        ID: '067',
        TITLE: 'Discrete Mathematics is the Best Course Ever',
        CREATED: '2021-09-02',
        MODIFIED: '2021-10-01',
        AUTHORS: [('Pancer', 'Richard'), ('Bretscher', 'Anna')],
        ABSTRACT: ('We explain why Discrete Mathematics is the best ' +
                   'course of all times.')},
    '827': {
        ID: '827',
        TITLE: 'University of Toronto is the Best University',
        CREATED: '2021-08-20',
        MODIFIED: '2021-10-02',
        AUTHORS: [('Ponce', 'Marcelo'), ('Bretscher', 'Anna'), 
                  ('Tafliovich', 'Anya Y.')],
        ABSTRACT: 'We show a formal proof that the University of\n' +
        'Toronto is the best university.'},
    '008': {
        ID: '008',
        TITLE: 'Intro to CS is the Best Course Ever',
        CREATED: '2021-09-01',
        MODIFIED: '',
        AUTHORS: [('Ponce', 'Marcelo'), ('Tafliovich', 'Anya Y.')],
        ABSTRACT: 'We present clear evidence that Introduction to\n' + \
        'Computer Science is the best course.'},    
    '042': {
        ID: '042',
        TITLE: '',
        CREATED: '2021-05-04',
        MODIFIED: '2021-05-05',
        AUTHORS: [],
        ABSTRACT: 'This is a strange article with no title\n' + \
        'and no authors.\n\nIt also has a blank line in its abstract!'}
}

EXAMPLE_BY_AUTHOR = {
    ('Ponce', 'Marcelo'): ['008', '827'],
    ('Tafliovich', 'Anya Y.'): ['008', '827'],
    ('Bretscher', 'Anna'): ['067', '827'],
    ('Breuss', 'Nataliya'): ['031'],
    ('Pancer', 'Richard'): ['067']
}

################################################
## Task 1 
################################################

# a helper to remove non-alphabetic characters
def clean_word(word: str) -> str:
    """Return word with all non-alphabetic characters removed and converted to 
    lowercase.
    
    Precondition: word contains no whitespace
    
    >>> clean_word('Hello!!!')
    'hello'
    >>> clean_word('12cat.dog?')
    'catdog'
    >>> clean_word("DON'T")
    'dont'
    """
    new_word = ''
    for ch in word:
        if ch.isalpha():
            new_word = new_word + ch.lower()
    return new_word

# Add your other Task 1 functions here
def created_in_year(id_to_article: ArxivType, id: str, year: int) -> bool:
    info = id_to_article.get(id)
    if info is None:
        return False
    else:
        if year == int(info['created'][:4]):
            return True
        return False

def contains_keyword(id_to_article: ArxivType, word: str) -> List[str]:
    res = []
    word = clean_word(word)
    for key in id_to_article:
        info = id_to_article[key]
        if word in clean_word(info['title']) or word in clean_word(info['abstract']):
            res.append(key)
    res.sort()
    return res


################################################
## Task 2
################################################

def read_arxiv_file(f: TextIO) -> ArxivType:
    """Return a ArxivType dictionary containing the arxiv metadata in f.

    Note we do not include example calls for functions that take open files.
    """

    # Complete this Task 2 function
    
    
# Add your helper functions for Task 2 here

################################################
## Task 3
################################################

def make_author_to_articles(id_to_article: ArxivType
                            ) -> Dict[NameType, List[str]]:
    """Return a dict that maps each author name to a list (sorted in
    lexicographic order) of IDs of articles written by that author,
    based on the information in id_to_article.

    >>> make_author_to_articles(EXAMPLE_ARXIV) == EXAMPLE_BY_AUTHOR
    True
    >>> make_author_to_articles({})
    {}
    """
    
    # Complete this Task 3 function
    

# Add your other functions for Task 3 here

################################################
## Task 4
################################################

# Add your Task 4 functions here

def keep_prolific_authors(id_to_article: ArxivType,
                          min_publications: int) -> None:
    """Update id_to_article so that it contains only articles published by
    authors with min_publications or more articles published. As long
    as at least one of the authors has min_publications, the article
    is kept.

    >>> arxiv_copy = copy.deepcopy(EXAMPLE_ARXIV)
    >>> keep_prolific_authors(arxiv_copy, 2)
    >>> len(arxiv_copy)
    3
    >>> '008' in arxiv_copy and '067' in arxiv_copy and '827' in arxiv_copy
    True
    >>> arxiv_copy = copy.deepcopy(EXAMPLE_ARXIV)
    >>> keep_prolific_authors(arxiv_copy, 3)
    >>> arxiv_copy
    {}
    """
    
    # Complete the body of this function. We have provided this docstring to
    # you so that you can use the EXAMPLE_ARXIV for testing mutation.
    # Note that we do not expect you to know about the copy.deepcopy function.
    

if __name__ == '__main__':
    pass
    # uncomment the lines below to run doctest on your code
    # note that doctest requires your docstring examples to be perfectly
    # formatted, and we will not be running doctest on your code
    
    # import doctest
    # doctest.testmod()
    

    # uncomment the lines below to work with the small data set
    
    # example_data = open('example_data.txt')
    # example_arxiv = read_arxiv_file(example_data)
    # example_data.close()
    # if example_arxiv == EXAMPLE_ARXIV:
        # print('The dictionary you produced matches EXAMPLE_ARXIV!')
        # print('This is a good sign, but do more of your own testing!')
    # else:
        # # If you are getting this message, try setting a breakpoint on the 
        # # line that calls read_arxiv_file above and running the debugger
        # print('Expected to get', EXAMPLE_ARXIV)
        # print('But got', example_arxiv)


    # uncomment the lines below to work with a larger data set
    
    # data = open('data.txt')
    # arxiv = read_arxiv_file(data)
    # data.close()

    # author_to_articles = make_author_to_articles(arxiv)
    # most_published = get_most_published_authors(arxiv)
    # print(most_published)
    # print(get_coauthors(arxiv, ('Varanasi', 'Mahesh K.')))  # one
    # print(get_coauthors(arxiv, ('Chablat', 'Damien')))  # many
