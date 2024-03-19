#!/usr/bin/env python
# coding: utf-8

# # Name Module
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

from pyphonetics import Soundex

import unittest

from common import Printable, testExit, projdir
from constants import *


# ## Load Nicknames into Memory
# 
# Load nicknames into memory when the module is imported

# In[2]:


nicknames = {}

csvPath = os.path.join(projdir, CONFIG_DIR, 'nicknames.csv')

with open(csvPath, 'r', encoding='utf-8') as f:
    csvReader = csv.reader(f)
    for values in csvReader:
        if values[0] != "NICKNAME":
            nicknames[values[0].lower()] = values[1]


# ## Name Class
# 
# Generic class to represent a name

# In[3]:


class Name(Printable):
    def __init__(self, name, verbosity=1):

        # Retain parameters
        self.name = name
        self.verbosity = verbosity
        
        self.determineNames()
        self.determineDerivedNames()
        self.determineInitials()
        self.determineSoundexes()
        

    def determineNames(self):
        '''Split up names based on spaces, hyphens and periods'''

        # Change multiple spaces to single spaces
        self.name = ' '.join(self.name.split())

        self.names = []
        for name in self.name.replace('-', ' ').replace('.', ' ').split(' '):
            if name:
                self.names.append(name)

        if len(self.names) >= 1:
            self.firstName = self.names[0]
        else:
            self.firstName = None

        if len(self.names) >= 2:
            self.lastName = self.names[-1]
        else:
            self.lastName = None


    def determineDerivedNames(self):
        '''Convert nicknames into full names'''

        self.derivedNames = []
        for name in self.names:
            if name.lower() in nicknames:
                self.derivedNames.append(nicknames[name.lower()])
            else:
                self.derivedNames.append(name)
        self.derivedName = ' '.join(self.derivedNames)

        if len(self.derivedNames) >= 1:
            self.derivedFirstName = self.derivedNames[0]
        else:
            self.derivedFirstName = None

        if len(self.derivedNames) >= 2:
            self.derivedLastName = self.derivedNames[-1]
        else:
            self.derivedLastName = None


    def determineInitials(self):
        '''Determine initials from each name part'''

        # Determine initials
        self.initials = [name[:1].upper() for name in self.names]
        self.derivedInitials = [name[:1].upper() for name in self.derivedNames]


    def determineSoundexes(self):
        '''Determine soundexes for each name part'''

        # Re-use the same soundex object for each name part
        soundex = Soundex()

        # Calculate soundexes for each name part
        try:
            self.soundexes = [soundex.phonetics(name) for name in self.names if name[:1].isalpha()]
            
            if len(self.soundexes) >= 1:
                self.firstNameSoundex = self.soundexes[0]
            else:
                self.firstNameSoundex = None

            if len(self.soundexes) >= 2:
                self.lastNameSoundex = self.soundexes[-1]
            else:
                self.lastNameSoundex = None
        except:
            print('Crashed calculating soundexes for {}'.format(self.names))
            raise
            
            
        # Calculate soundexes for each derived name part
        try:
            self.derivedSoundexes = [soundex.phonetics(name) for name in self.derivedNames if name[:1].isalpha()]
            
            if len(self.derivedSoundexes) >= 1:
                self.derivedFirstNameSoundex = self.derivedSoundexes[0]
            else:
                self.derivedFirstNameSoundex = None

            if len(self.derivedSoundexes) >= 2:
                self.derivedLastNameSoundex = self.derivedSoundexes[-1]
            else:
                self.derivedLastNameSoundex = None
        except:
            print('Crashed calculating soundexes for {}'.format(self.derivedNames))
            raise


# ## Unit Tests
# 
# A handful of very basic tests

# In[4]:


class TestName(unittest.TestCase):
    '''Class to test Name class'''

    def testNickname(self):

        name = Name('Bob Spagnoletti')

        self.assertEqual(name.name, 'Bob Spagnoletti')
        self.assertEqual(name.firstName, 'Bob')
        self.assertEqual(name.lastName, 'Spagnoletti')
        self.assertEqual(name.names, ['Bob', 'Spagnoletti'])
        self.assertEqual(name.initials, ['B', 'S'])
        self.assertEqual(name.soundexes, ['B100', 'S125'])
        self.assertEqual(name.firstNameSoundex, 'B100')
        self.assertEqual(name.lastNameSoundex, 'S125')

        self.assertEqual(name.derivedName, 'Robert Spagnoletti')
        self.assertEqual(name.derivedFirstName, 'Robert')
        self.assertEqual(name.derivedLastName, 'Spagnoletti')
        self.assertEqual(name.derivedNames, ['Robert', 'Spagnoletti'])
        self.assertEqual(name.derivedInitials, ['R', 'S'])
        self.assertEqual(name.derivedSoundexes, ['R163', 'S125'])
        self.assertEqual(name.derivedFirstNameSoundex, 'R163')
        self.assertEqual(name.derivedLastNameSoundex, 'S125')


    def testHyphen(self):

        name = Name('Claude Van-Martyn')

        self.assertEqual(name.name, 'Claude Van-Martyn')
        self.assertEqual(name.firstName, 'Claude')
        self.assertEqual(name.lastName, 'Martyn')
        self.assertEqual(name.names, ['Claude', 'Van', 'Martyn'])
        self.assertEqual(name.initials, ['C', 'V', 'M'])
        self.assertEqual(name.soundexes, ['C430', 'V500', 'M635'])
        self.assertEqual(name.firstNameSoundex, 'C430')
        self.assertEqual(name.lastNameSoundex, 'M635')

        self.assertEqual(name.derivedName, 'Claude Van Martyn')
        self.assertEqual(name.derivedFirstName, 'Claude')
        self.assertEqual(name.derivedLastName, 'Martyn')
        self.assertEqual(name.derivedNames, ['Claude', 'Van', 'Martyn'])
        self.assertEqual(name.derivedInitials, ['C', 'V', 'M'])
        self.assertEqual(name.derivedSoundexes, ['C430', 'V500', 'M635'])
        self.assertEqual(name.derivedFirstNameSoundex, 'C430')
        self.assertEqual(name.derivedLastNameSoundex, 'M635')


    def testInitials(self):

        name = Name('E.H.S.')

        self.assertEqual(name.name, 'E.H.S.')
        self.assertEqual(name.firstName, 'E')
        self.assertEqual(name.lastName, 'S')
        self.assertEqual(name.names, ['E', 'H', 'S'])
        self.assertEqual(name.initials, ['E', 'H', 'S'])
        self.assertEqual(name.soundexes, ['E000', 'H000', 'S000'])
        self.assertEqual(name.firstNameSoundex, 'E000')
        self.assertEqual(name.lastNameSoundex, 'S000')

        self.assertEqual(name.derivedName, 'E H S')
        self.assertEqual(name.derivedFirstName, 'E')
        self.assertEqual(name.derivedLastName, 'S')
        self.assertEqual(name.derivedNames, ['E', 'H', 'S'])
        self.assertEqual(name.derivedInitials, ['E', 'H', 'S'])
        self.assertEqual(name.derivedSoundexes, ['E000', 'H000', 'S000'])
        self.assertEqual(name.derivedFirstNameSoundex, 'E000')
        self.assertEqual(name.derivedLastNameSoundex, 'S000')


    def testWhitespaceRemoval(self):

        name = Name('Michael    George')
        self.assertEqual(name.name, 'Michael George')


    def testCrash(self):

        name = Name('Richard Jones (GBR-32)')


# ## Run Unit Tests
# 
# Note: Only run unit tests when running this script directly, not during an import

# In[5]:


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=testExit)


# ## All Done!
