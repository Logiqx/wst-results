#!/usr/bin/env python
# coding: utf-8

# # Common Module
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
import sys


# In[2]:


# Determine whether session is interactive or batch to facilitate unittest.main(..., exit=testExit)
import __main__ as main
testExit = hasattr(main, '__file__')


# In[3]:


projdir = os.path.realpath(os.path.join(sys.path[0], '..'))


# ## Generic Class
# 
# Generic class to ensure that all custom classes are printable

# In[4]:


class Printable:
    def __init__(self, verbosity=1):
        self.verbosity = verbosity

    def __repr__(self):
        return str(self.__class__) + ": " + str(self.__dict__)

    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)
    
    def logInfo(self, msg):
        if self.verbosity >= 2:
            print('INFO:', msg)

    def logWarning(self, msg):
        if self.verbosity >= 1:
            print('WARNING:', msg)

    def logError(self, msg):
        print('ERROR:', msg)


# ## All Done!
