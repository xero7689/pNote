#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
PNote - Python Command-Line Note App

Modify some API
Save as Pickle

author: xero
mail: volleyp7689@gmail.com
last edit: July 17 2014
"""
import pickle
import datetime
#import tempfile
import getpass
import os
import copy
import sys

_VERSION = "2.0"
_AUTHOR = "xero"

_LINE_BREAK = "\n"
_DEFAULT_ENCODE = "utf-8"
_DEFAULT_DECODE = "utf-8"
_FILENAME_EXT = ".pkl"

_USER = getpass.getuser()
_USER_HOME_DIR = os.path.expanduser("~")
_DEFAULT_PNOTE_DIR = os.path.join(_USER_HOME_DIR, "pNote")

_NOW = datetime.datetime.now().ctime().split()

NOTE_LIST = []

'''Data structure'''
class Note:
    def __init__(self, title = None, time = None, tag = None):
        self.title = title
        self.time = time
        self.tags = tag
        self.content = ""
        self.filename = None
    
    def addTag(self, *tags):
        for tag in tags:
            self.tags.append(tag)
        print("Add tag: ", end = "")
        for tag in self.tags:
            print(tag, end=",")
    
    def check_filename(self):
        if self.filename is None:
            return False
        else:
            return self.filename
            
    def takeNote(self):
        #set title
        print("Note title:")
        while True:
            self.title = input("->")
            if len(self.title) == 0:
                print("Need a title !")
            else:
                break
        
        #take note
        print("Note Content:")
        while True:
            text = input()
            if len(text) == 0:
                break
            else:
                self.content = self.content + text + _LINE_BREAK
                
        #set file name
        self.filename = os.path.join(_DEFAULT_PNOTE_DIR, self.title + _FILENAME_EXT)
    
    def save(self):
        if not self.check_filename():
            print("This note doesn't have a filename.")
            return
        
        self.time = _NOW
        data = (self.title, self.time, self.tags, self.content)
            
        with open(self.filename, "ba+") as f:
            pickle.dump(data, f)
    
    def load(self, filename):
    
'''Command'''
def init_dir():
    if not os.path.exists(_DEFAULT_PNOTE_DIR):
        os.makedir(_DEFAULT_PNOTE_DIR)

def add():
    new = Note()
    new.takeNote()
    new.save()

def load():
    pass

def listNote():
    for note in os.listdir(_DEFAULT_PNOTE_DIR):
        if note.endswith(_FILENAME_EXT):
            NOTE_LIST.append(note)
    print(NOTE_LIST)

def _quit():
    sys.exit("Bye!\n")
    
command = dict(a = add,
                l = load,
                ll = listNote,
                q = _quit)

def commandLine():
    ''' prompting message '''
    print("\nWelcome to pNote-" + _VERSION)
    
    while True:
        print("\nCommand:")
        print("(a)Add (l)Load (ll)List (q)Quit")
        action = input("->")
        try:
            command[action]()
        except KeyError:
            print("command error, choose again!")
            
def main():
    commandLine()
    
if __name__ == "__main__":
    main()
