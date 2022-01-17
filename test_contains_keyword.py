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

import unittest
import arxiv_functions

# you may not need to use the types, but we have imported them all for you
from constants import (ID, TITLE, CREATED, MODIFIED, AUTHORS, ABSTRACT, END, 
                       NameType, ArticleValueType, ArticleType, ArxivType)


# You can use this sample dictionary in your tests, if you choose
# You can also create your own sample dictionaries 
TEST_ARXIV = {
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


class TestContainsKeyword(unittest.TestCase):
    """Test cases for function arxiv_functions.contains_keyword
    """
    
    def test_one_match(self) -> None:
        """Test contains_keyword with the keyword appearing in both the title
        and abstract of one article.
        """
        actual = arxiv_functions.contains_keyword(TEST_ARXIV, 'Toronto')
        expected = ['827']
        self.assertEqual(actual, expected)

    def test_two_match(self) -> None:
        """Test contains_keyword with the keyword only appearing in the
        abstract of one article.
        """
        actual = arxiv_functions.contains_keyword(TEST_ARXIV, 'Strange')
        expected = ['042']
        self.assertEqual(actual, expected)

    def test_three_match(self) -> None:
        """Test contains_keyword with the keyword only appearing in the
        title of one article.
        """
        actual = arxiv_functions.contains_keyword(TEST_ARXIV, 'Discrete')
        expected = ['067']
        self.assertEqual(actual, expected)

    def test_four_match(self) -> None:
        """Test contains_keyword with the keyword only appearing five articles
        and sort the ids in lexicographic order.
        """
        actual = arxiv_functions.contains_keyword(TEST_ARXIV, 'is')
        expected = ['008', '031', '042', '067', '827']
        self.assertEqual(actual, expected)

    def test_five_match(self) -> None:
        """Test contains_keyword with the keyword not appearing in all articles
        """
        actual = arxiv_functions.contains_keyword(TEST_ARXIV, 'was')
        expected = []
        self.assertEqual(actual, expected)

    def test_six_match(self) -> None:
        """Test contains_keyword with the keyword in the lower case
        """
        actual = arxiv_functions.contains_keyword(TEST_ARXIV, 'we')
        expected = ['008', '031', '067', '827']
        self.assertEqual(actual, expected)
    
if __name__ == '__main__':
    unittest.main(exit=False)
