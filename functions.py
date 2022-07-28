from essential_generators import DocumentGenerator
import time
import random
from variables import riddlelist
from replit import db

# Changelog:
# Optimised some of the code
# Standardised indentation
# Please set your intentation settings to 4 spaces

# Overall Comments:
# In general, I'm not so sure of the usage of global variables here
# If I were to do a full rewrite, I would make functions return their intended output instead
# of setting it in a global variable
# Also, this might be nitpicking, but try to seperate words in function names with undescores

sentence = ''
starttime = 0
senlist = []
randnum = 0
typingauthor = ''
riddleauthor = ''

if 'team' not in db.keys():
    for x in range(1, 5): # Use a for-loop instead
        exec(f'db["team{x}"] = 0') # I DO NOT encourage this, but since people can't input stuff in there I guess it's fine

def sen_gen():
    gen = DocumentGenerator()
    global sentence
    global senlist
    sentence = gen.sentence()
    senlist = sentence.split()
    if len(senlist) > 10:
        sentence = " ".join(senlist) + "." # Use join instead, much better


def start_time():
    global starttime
    starttime = time.time()


def team_find(roles):
    for roletemp in roles: # Use a for loop instead, much easier
        if 'Team' in str(roletemp):
            role = str(roletemp).split(' ')
            return role[1]


def add_pts(teamno, nopts):
    exec('db["team{}"] += {}'.format(teamno, nopts)) # exec really shouldn't be used in code, but okay
    exec("global var; var = db['team" + teamno + "']")
    return var
  
def riddle_gen():
    global randnum
    randnum = random.randint(0, 3)
    return riddlelist[randnum][0]


def riddle(author):
    global riddleauthor
    riddleauthor = author

def typing(author):
    global typingauthor
    typingauthor = author 
