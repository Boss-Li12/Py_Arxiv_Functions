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

from typing import Dict, List, Tuple, Union

ID = 'identifier'
TITLE = 'title'
CREATED = 'created'
MODIFIED = 'modified'
AUTHORS = 'authors'
ABSTRACT = 'abstract'
END = 'END'

# We store names as tuples of two strs: (last-name, first-name(s)).
NameType = Tuple[str, str]

# ArticleValueType is the type for valid values in the ArticleType
# dict.  All values are str, except for the value associated with
# key AUTHORS, which is a List of NameType.
# Note that we have not introduced Union - you can read it as "or"
ArticleValueType = Union[str, List[NameType]]

# ArticleType is a dict that maps keys ID, TITLE, CREATED, MODIFIED,
# AUTHORS, and ABSTRACT to their values (of type ArticleValueType).
ArticleType = Dict[str, ArticleValueType]

# ArxivType is a dict that maps article identifiers to articles,
# i.e. to values of type ArticleType.
# 也就是构建了这样一个基于dict的数据结构
ArxivType = Dict[str, ArticleType]
