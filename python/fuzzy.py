#!/usr/bin/env python
# coding: utf-8

# # Fuzzy Module
# 
# Copyright 2022 Michael George (AKA Logiqx).
# 
# This file is part of [sse-results](https://github.com/Logiqx/sse-results) and is distributed under the terms of the GNU General Public License.
# 
# sse-results is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
# 
# sse-results is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License along with sse-results. If not, see <https://www.gnu.org/licenses/>.

# ## Initialisation
# 
# Basic approach to determine the project directory

# In[1]:


import os
import csv
import Levenshtein

import unittest

from common import Printable, testExit, projdir
from name import Name
from constants import *


# ## Load Relations into Memory
# 
# Load relations into memory when the module is imported

# In[2]:


relations = {}

csvPath = os.path.join(projdir, CONFIG_DIR, 'relations.csv')

with open(csvPath, 'r', encoding='utf-8') as f:
    csvReader = csv.reader(f)
    for values in csvReader:
        if values[0] != 'ENTRANT NAME':
            relations[values[0].lower()] = values[1].lower()
            relations[values[1].lower()] = values[0].lower()


# ## Fuzzy Match Class
# 
# Generic class to fuzzy match two names

# In[3]:


class FuzzyMatch(Printable):
    def __init__(self, verbosity=1):

        self.verbosity = verbosity


    def matchNames(self, name1, name2):
        '''Simple method to determine of two names are a likely match'''

        nameOne = Name(name1)
        nameTwo = Name(name2)
        
        return self.matchNameObjects(nameOne, nameTwo)


    def matchNameObjects(self, nameOne, nameTwo):
        '''Simple method to determine of two names are a likely match'''

        # Quick hack to return quickly when first initial does not match
        if nameOne.derivedInitials[:1] != nameTwo.derivedInitials[:1]:
            return False

        # Test the fixed list of exclusions
        if nameOne.derivedName.lower() in relations and nameTwo.derivedName.lower() == relations[nameOne.derivedName.lower()]:
            return False
        
        # Now attempt the fuzzy name matching using Levenshtein and soundex - crude but relatively effective
        try:
            distance = Levenshtein.distance(nameOne.derivedName.lower(), nameTwo.derivedName.lower())
            
            if distance == 0:
                return True

            if len(nameOne.soundexes) >= 2 and len(nameTwo.soundexes) >= 2 and             (
                (
                    # Levenshtein distance up to 4 is allowed if the first and last name are identical
                    nameOne.firstName == nameTwo.firstName and nameOne.lastName == nameTwo.lastName and \
                    distance <= 4
                ) or \
                (
                    # Levenshtein distance up to 3 is allowed if the first and last name have matching soundex
                    nameOne.derivedFirstNameSoundex[3] != '0' and nameTwo.derivedFirstNameSoundex[3] != '0' and \
                    nameOne.derivedFirstNameSoundex == nameTwo.derivedFirstNameSoundex and \
                    nameOne.derivedLastNameSoundex[3] != '0' and nameTwo.derivedLastNameSoundex[3] != '0' and \
                    nameOne.derivedLastNameSoundex == nameTwo.derivedLastNameSoundex and \
                    distance <= 3
                ) or \
                (
                    # Levenshtein distance of 2 is allowed if the first name is identical and last name has matching soundex
                    nameOne.firstName == nameTwo.firstName and \
                    nameOne.derivedLastNameSoundex[3] != '0' and nameTwo.derivedLastNameSoundex[3] != '0' and \
                    nameOne.derivedLastNameSoundex == nameTwo.derivedLastNameSoundex and \
                    distance <= 2
                ) or \
                (
                    # Levenshtein distance of 2 is allowed if the last name is identical and first name has matching soundex
                    nameOne.derivedFirstNameSoundex[3] != '0' and nameTwo.derivedFirstNameSoundex[3] != '0' and \
                    nameOne.derivedFirstNameSoundex == nameTwo.derivedFirstNameSoundex and \
                    nameOne.lastName == nameTwo.lastName and \
                    distance <= 2
                ) or \
                (
                    # Levenshtein distance of 2 is allowed if the first and last name have near-matching soundex (3 chars)
                    nameOne.derivedFirstNameSoundex[2] != '0' and nameTwo.derivedFirstNameSoundex[2] != '0' and \
                    nameOne.derivedFirstNameSoundex[:3] == nameTwo.derivedFirstNameSoundex[:3] and \
                    nameOne.derivedLastNameSoundex[2] != '0' and nameTwo.derivedLastNameSoundex[2] != '0' and \
                    nameOne.derivedLastNameSoundex[:3] == nameTwo.derivedLastNameSoundex[:3] and \
                    distance <= 2
                ) or \
                (
                    # Levenshtein distance of 1 is allowed if the first + last names have partially matching soundex (2 chars)
                    nameOne.derivedFirstNameSoundex[1] != '0' and nameTwo.derivedFirstNameSoundex[1] != '0' and \
                    nameOne.derivedFirstNameSoundex[:2] == nameTwo.derivedFirstNameSoundex[:2] and \
                    nameOne.derivedLastNameSoundex[1] != '0' and nameTwo.derivedLastNameSoundex[1] != '0' and \
                    nameOne.derivedLastNameSoundex[:2] == nameTwo.derivedLastNameSoundex[:2] and \
                    distance <= 1
                )
            ):
                return True

        except:
            print('Crashed comparing {} and {}'.format(nameOne, nameTwo))
            raise
            
        return False


# ## Unit Tests
# 
# A handful of very basic tests

# In[4]:


appliedChanges = [
    ('Alan Cross', 'Allan Cross'),
    ('Alex Bennett- Baggs', 'Alex Bennett-Baggs'),
    ('Alistair Williams', 'Alastair Williams'),
    ('Andy Harris', 'Andrew Harris'),
    ('Antony Baker', 'Anthony Baker'),
    ('Bill Robinson', 'William Robinson'),
    ('Bjoern Haacke', 'Bjorn Haacke'),
    ('Charlie Wilson', 'Charles Wilson'),
    ('Claude Van Martin', 'Claude Van-Martyn'),
    ('Claude Van Martin', 'Claud Van Martin'),
    ('Claud Van Martin', 'Claude Van-Martyn'),
    ('Dan Robinson', 'Daniel Robinson'),
    ('Dave MacInnes', 'David MacInnes'),
    ('Dave Strudwick', 'David Strudwick'),
    ('David Ellerbeck', 'Dave Ellerbeck'),
    ('David Finch', 'Dave Finch'),
    ('Edward Murrell', 'Eddie Murrell'),
    ('Graham Holbert', 'Graham Hulbert'),
    ('Jim Paine', 'James Paine'),
    ('Joe Adams', 'Joseph Adams'),
    ('John Langdown', 'John Langdon'),
    ('John Pepperel', 'John Peperell'),
    ('Malcom Barnsley', 'Malcolm Barnsley'),
    ('Mathew Spooner', 'Matthew Spooner'),
    ('Matthew Burridge', 'Mathew Burridge'),
    ('Matthew Philpott', 'Matt Philpott'),
    ('Michael Walklin', 'Mike Walklin'),
    ('Nick Brumfitt', 'Nick Brumfit'),
    ('Nills Haarbosch', 'Neils Haarbosch'),
    ('Pete Cunningham', 'Peter Cunningham'),
    ('Pete Martin', 'Peter Martin'),
    ('Peter Davis', 'Pete Davis'),
    ('Peter Young', 'Pete Young'),
    ('Phil Lewin', 'Philip Lewin'),
    ('Piere Saville', 'Pierre Saville'),
    ('Robert Date', 'Bob Date'),
    ('Robert Spagnoletti', 'Bob Spagnoletti'),
    ('Roger Crab', 'Roger Crabb'),
    ('Rüdiger Lotz', 'Rudiger Lotz'),
    ('Stephen Davison', 'Steve Davidson'),
    ('Stephen Davison', 'Steve Davison'),
    ('Steve Davidson', 'Steve Davison'),
    ('Steven Summerfield', 'Steve Summerfield'),
    ('Will Giles', 'William Giles'),
    ('William Rowles', 'Will Rowles'),
    ('Will Oscroft', 'William Oscroft'),
    ('Will Trossell', 'William Trossell'),
    ('Xavier Forlet', 'Xavier Ferlet')
]


# In[5]:


class TestFuzzyMatch(unittest.TestCase):
    '''Class to test FuzzyMatch class'''
    
    def testTypo01(self):

        fuzzyMatch = FuzzyMatch(verbosity=0)
        self.assertEqual(True, fuzzyMatch.matchNames('Graham Holbert', 'Graham Hulbert'))


    def testTypo02(self):

        fuzzyMatch = FuzzyMatch(verbosity=0)
        self.assertEqual(True, fuzzyMatch.matchNames('Trevor Watford', 'Trevor Whatford'))


    def testTypo03(self):

        fuzzyMatch = FuzzyMatch(verbosity=0)
        self.assertEqual(True, fuzzyMatch.matchNames('Mathew Spooner', 'Matthew Spooner'))


    def testTypo04(self):

        fuzzyMatch = FuzzyMatch(verbosity=0)
        self.assertEqual(True, fuzzyMatch.matchNames('Kin Newman', 'Kim Newman'))


    def testTypo05(self):

        fuzzyMatch = FuzzyMatch(verbosity=0)
        self.assertEqual(True, fuzzyMatch.matchNames('Piere Saville', 'Pierre Saville'))


    def testTypo06(self):

        fuzzyMatch = FuzzyMatch(verbosity=0)
        self.assertEqual(True, fuzzyMatch.matchNames('John Montgomery', 'John Montgomer'))


    def testTypo07(self):

        fuzzyMatch = FuzzyMatch(verbosity=0)
        self.assertEqual(True, fuzzyMatch.matchNames('Alistair Williams', 'Alastair Williams'))


    def testNickname01(self):

        fuzzyMatch = FuzzyMatch(verbosity=0)
        self.assertEqual(True, fuzzyMatch.matchNames('Pete Martin', 'Peter Martin'))


    def testNickname01(self):

        fuzzyMatch = FuzzyMatch(verbosity=0)
        self.assertEqual(True, fuzzyMatch.matchNames('Dave MacInnes', 'David MacInnes'))


    def testNickname02(self):

        fuzzyMatch = FuzzyMatch(verbosity=0)
        self.assertEqual(True, fuzzyMatch.matchNames('Dan Robinson', 'Daniel Robinson'))


    def testNickname03(self):

        fuzzyMatch = FuzzyMatch(verbosity=0)
        self.assertEqual(True, fuzzyMatch.matchNames('Jim Paine', 'James Paine'))


    def testNickname04(self):

        fuzzyMatch = FuzzyMatch(verbosity=0)
        self.assertEqual(True, fuzzyMatch.matchNames('Matt Spooner', 'Matthew Spooner'))


    def testNickname05(self):

        fuzzyMatch = FuzzyMatch(verbosity=0)
        self.assertEqual(True, fuzzyMatch.matchNames('Eddie Murrell', 'Edward Murrell'))


    def testNickname06(self):

        fuzzyMatch = FuzzyMatch(verbosity=0)
        self.assertEqual(True, fuzzyMatch.matchNames('Ed Murrell', 'Edward Murrell'))


    def testNickname07(self):

        fuzzyMatch = FuzzyMatch(verbosity=0)
        self.assertEqual(True, fuzzyMatch.matchNames('Robert Date', 'Bob Date'))


    def testNickname08(self):

        fuzzyMatch = FuzzyMatch(verbosity=0)
        self.assertEqual(True, fuzzyMatch.matchNames('Stephen Davison', 'Steve Davidson'))


    def testNickname09(self):

        fuzzyMatch = FuzzyMatch(verbosity=0)
        self.assertEqual(True, fuzzyMatch.matchNames('Michael Walklin', 'Mike Walklin'))


    def testVariation01(self):

        fuzzyMatch = FuzzyMatch(verbosity=0)
        self.assertEqual(True, fuzzyMatch.matchNames('Hans-Juergen', 'Hans-Jürgen'))


    def testVariation02(self):

        fuzzyMatch = FuzzyMatch(verbosity=0)
        self.assertEqual(True, fuzzyMatch.matchNames('Claude van Martyn', 'Claude Van-Martyn'))


    def testVariation03(self):

        fuzzyMatch = FuzzyMatch(verbosity=0)
        self.assertEqual(True, fuzzyMatch.matchNames('Claude Van-Martyn', 'Claude Van-Man-Martyn'))


    def testVariation04(self):

        fuzzyMatch = FuzzyMatch(verbosity=0)
        self.assertEqual(True, fuzzyMatch.matchNames('Trevor Lyn Whatford', 'Trevor Whatford'))


    def testNonMatch01(self):

        fuzzyMatch = FuzzyMatch(verbosity=0)
        self.assertEqual(False, fuzzyMatch.matchNames('Alex Montgomery', 'John Montgomery'))


    def testNonMatch02(self):

        fuzzyMatch = FuzzyMatch(verbosity=0)
        self.assertEqual(False, fuzzyMatch.matchNames('Robin Ball', 'Kevin Hall'))


    def testNonMatch03(self):

        fuzzyMatch = FuzzyMatch(verbosity=0)
        self.assertEqual(False, fuzzyMatch.matchNames('Nick Beaney', 'Nick Povey'))


    def testNonMatch04(self):

        fuzzyMatch = FuzzyMatch(verbosity=0)
        self.assertEqual(False, fuzzyMatch.matchNames('Andy', 'Amy'))


    def testNonMatch05(self):

        fuzzyMatch = FuzzyMatch(verbosity=0)
        self.assertEqual(False, fuzzyMatch.matchNames('Richard Jenkins', 'Richard Jones'))


    def testNonMatch06(self):

        fuzzyMatch = FuzzyMatch(verbosity=0)
        self.assertEqual(False, fuzzyMatch.matchNames('Jeremy Waitt', 'Jeremy Walwin'))


    def testNonMatch07(self):

        fuzzyMatch = FuzzyMatch(verbosity=0)
        self.assertEqual(False, fuzzyMatch.matchNames('Dave Ellerman', 'Dave Ellerbeck'))


    def testNonMatch08(self):

        fuzzyMatch = FuzzyMatch(verbosity=0)
        self.assertEqual(False, fuzzyMatch.matchNames('Simon Moore', 'Simon Maguire'))    
        

    def testExclusion01(self):
        '''Brothers'''

        fuzzyMatch = FuzzyMatch(verbosity=0)
        self.assertEqual(False, fuzzyMatch.matchNames('Ruben Hofman', 'Robin Hofman'))


    def testExclusion02(self):
        '''Father and son'''

        fuzzyMatch = FuzzyMatch(verbosity=0)
        self.assertEqual(False, fuzzyMatch.matchNames('Emile Burnaby Lautier', 'Emile Jan Burnaby Lautier'))


    def testExclusion03(self):
        '''Legacy exclusion - now avoided by soundex test'''

        fuzzyMatch = FuzzyMatch(verbosity=0)
        self.assertEqual(False, fuzzyMatch.matchNames('Mike Pacey', 'Mike Pearce'))


    def testExclusion04(self):
        '''Legacy exclusion - now avoided by soundex test'''

        fuzzyMatch = FuzzyMatch(verbosity=0)
        self.assertEqual(False, fuzzyMatch.matchNames('Mike Price', 'Mike Pacey'))


    def testExclusion05(self):
        '''Legacy exclusion - now avoided by soundex test'''

        fuzzyMatch = FuzzyMatch(verbosity=0)
        self.assertEqual(False, fuzzyMatch.matchNames('Alex Bradley', 'Alex Bailey'))


    def testExclusion06(self):
        '''Legacy exclusion - now avoided by soundex test'''

        fuzzyMatch = FuzzyMatch(verbosity=0)
        self.assertEqual(False, fuzzyMatch.matchNames('Robert Dunn', 'Robert Date'))


    def testExclusion07(self):
        '''Legacy exclusion - now avoided by soundex test'''

        fuzzyMatch = FuzzyMatch(verbosity=0)
        self.assertEqual(False, fuzzyMatch.matchNames('Roger Clark', 'Roger Crabb'))


    def testExclusion09(self):
        '''Legacy exclusion - now avoided by soundex test'''

        fuzzyMatch = FuzzyMatch(verbosity=0)
        self.assertEqual(False, fuzzyMatch.matchNames('Stephen Corps', 'Stephen Cole'))


    def testSurnameCollision01(self):

        fuzzyMatch = FuzzyMatch(verbosity=0)
        self.assertEqual(False, fuzzyMatch.matchNames('Simon Hemsley', 'Simon Hinkley'))


    def testSurnameCollision02(self):

        fuzzyMatch = FuzzyMatch(verbosity=0)
        self.assertEqual(False, fuzzyMatch.matchNames('Richard Powell', 'Richard Peel'))
        

    def testSurnameCollision03(self):

        fuzzyMatch = FuzzyMatch(verbosity=0)
        self.assertEqual(False, fuzzyMatch.matchNames('Michael Price', 'Michael Pearce'))
        

    def testSurnameCollision04(self):

        fuzzyMatch = FuzzyMatch(verbosity=0)
        self.assertEqual(False, fuzzyMatch.matchNames('John Langley', 'John Lindley'))
        

    def testSurnameCollision05(self):

        fuzzyMatch = FuzzyMatch(verbosity=0)
        self.assertEqual(False, fuzzyMatch.matchNames('Peter Crosby', 'Peter Crook'))
        

    def testCrash01(self):
        '''Legacy crash'''

        fuzzyMatch = FuzzyMatch(verbosity=0)
        self.assertEqual(True, fuzzyMatch.matchNames('Dave - Vinnie - Standing', 'Dave Vinne Standing'))


    def testCrash02(self):
        '''Legacy crash'''

        fuzzyMatch = FuzzyMatch(verbosity=0)
        self.assertEqual(False, fuzzyMatch.matchNames('Richard Jones (GBR-32)', 'Richard Trubger'))


    def testCaseDifference01(self):

        fuzzyMatch = FuzzyMatch(verbosity=0)
        self.assertEqual(True, fuzzyMatch.matchNames('MIKE GEORGE', 'mike George'))


    def testCaseDifference02(self):

        fuzzyMatch = FuzzyMatch(verbosity=0)
        self.assertEqual(True, fuzzyMatch.matchNames('MIKE GEORGE', 'michael George'))


    def testCaseDifference03(self):

        fuzzyMatch = FuzzyMatch(verbosity=0)
        self.assertEqual(True, fuzzyMatch.matchNames('gifford', 'Gifford'))


    def testCaseDifference04(self):

        fuzzyMatch = FuzzyMatch(verbosity=0)
        self.assertEqual(True, fuzzyMatch.matchNames('guy cribb', 'Guy Cribb'))


    def testSpaceDifference01(self):

        fuzzyMatch = FuzzyMatch(verbosity=0)
        self.assertEqual(True, fuzzyMatch.matchNames('Keith  Atkinson', 'Keith Atkinson'))


    def testAppliedChanges(self):
        '''Test changes that have been applied to historical data'''

        fuzzyMatch = FuzzyMatch(verbosity=0)
        for appliedChange in appliedChanges:
            result = fuzzyMatch.matchNames(appliedChange[0], appliedChange[1])
            if result == False:
                print('Issue with {} vs {}'.format(appliedChange[0], appliedChange[1]))
            self.assertEqual(True, result)


# ## Run Unit Tests
# 
# Note: Only run unit tests when running this script directly, not during an import

# In[6]:


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=testExit)


# ## All Done!
