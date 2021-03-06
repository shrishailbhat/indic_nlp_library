# Copyright Anoop Kunchukuttan 2014 - present
#
# This file is part of Indic NLP Library.
# 
# Indic NLP Library is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# Indic NLP Library is distributed in the hope that it will be useful,
#        but WITHOUT ANY WARRANTY; without even the implied warranty of
#        MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#        GNU General Public License for more details.
# 
#        You should have received a copy of the GNU General Public License
#        along with Indic NLP Library.  If not, see <http://www.gnu.org/licenses/>.
#

import os

"""
Path to the Indic NLP Resources directory
"""
INDIC_RESOURCES_PATH=''

def init():
    """
    Initialize the module. The following actions are performed:

    - Checks of INDIC_RESOURCES_PATH variable is set. If not, checks if it can beb initialized from 
        INDIC_RESOURCES_PATH environment variable. If that fails, an exception is raised
    """
    global INDIC_RESOURCES_PATH 
    try: 
        if INDIC_RESOURCES_PATH=='':
            INDIC_RESOURCES_PATH=os.environ['INDIC_RESOURCES_PATH']
    except Exception as e: 
        raise IndicNlpException('Indic Resources Path not set')

    if INDIC_RESOURCES_PATH=='': 
        raise IndicNlpException('Indic Resources Path not set')



def get_resources_path(): 
    """
        Get the path to the Indic NLP Resources directory
    """
    return INDIC_RESOURCES_PATH

def set_resources_path(resources_path): 
    """
        Set the path to the Indic NLP Resources directory
    """
    global INDIC_RESOURCES_PATH 
    INDIC_RESOURCES_PATH=resources_path

class IndicNlpException(Exception):
    """
        Exceptions thrown by Indic NLP Library components are instances of this class.  
        'msg' attribute contains exception details.
    """
    def __init__(self, msg):
        self.msg = msg 

    def __str__(self):
        return repr(self.msg)

