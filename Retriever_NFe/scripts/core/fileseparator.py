import os
from os import listdir
from os.path import isfile, join
import shutil
from datetime import date


def createList(_self_):
    retrievedfiles = [f for f in listdir(_self_) if isfile(join(_self_, f))]
    return(retrievedfiles)