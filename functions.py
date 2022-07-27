from essential_generators import DocumentGenerator
import time
import random
from variables import riddlelist
from replit import db

sentence = ''
starttime = 0
senlist = []
randnum = 0
typingauthor = ''
riddleauthor = ''

if 'team' not in db.keys():
  x = 1
  while x <=4:
    exec('db["team{}"] = 0'.format(x))
    x+=1

def sengen():
    gen = DocumentGenerator()
    global sentence
    global senlist
    sentence = gen.sentence()
    senlist = sentence.split()
    if len(senlist) > 10:
        sentence = senlist[0] + ' ' + senlist[1] + ' ' + senlist[
            2] + ' ' + senlist[3] + ' ' + senlist[4] + ' ' + senlist[
                5] + ' ' + senlist[6] + ' ' + senlist[7] + ' ' + senlist[
                    8] + ' ' + senlist[9] + '.'


def start_time():
    global starttime
    starttime = time.time()


def teamfind(roles):
    i = 0
    while i < len(roles):
        roletemp = roles[i]
        if 'Team' in str(roletemp):
            role = str(roletemp).split(' ')
            return role[1]
        i += 1


def addpts(teamno,nopts):
  exec('db["team{}"] += {}'.format(teamno,nopts))
  exec("global var; var = db['team" + teamno + "']")
  return var
  
def riddlegen():
    global randnum
    randnum = random.randint(0, 3)
    return riddlelist[randnum][0]


def riddle(author):
  global riddleauthor
  riddleauthor = author

def typing(author):
  global typingauthor
  typingauthor = author 
