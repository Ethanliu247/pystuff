from random import choice as randchoice

print('Hello and welcome to my insult generator. Just hit return and then have fun!!!')

a1 = ['pig-headed', 'ox-brained', 'cow-mugging', 'chain-tuffling', 'fascist', 'antogonistic', 'fart-smelling', 'red-bearing', 'fat', 'communist', 'Trump-like', 'ass-headed', 'jaded', 'imprisoned', 'drug-addicted', 'uranium-smoking', 'dumb', 'spliced', 'cannabilistic', 'Yovel-like']
a2 = ['cob-wobbling', 'chainmail-chuffling', 'faucist', 'cattle-rustling', 'Nazi-loving', 'terrorist-backing', 'bloodthirsty', 'disease-ridden', 'America-hating', 'Kavkaesque', 'idiotical', 'shallow', 'simple-minded', 'pea-brained', 'racist', 'soucilist', 'beautiful', 'green']
n1 = ['scoudrel', 'scallywag', 'ass', 'terrorist', 'Nazi', 'Commie', 'camel', 'feather', 'cow', 'hoodlum', 'barbarian', 'waste of space', 'bully', 'Raisin Bran', 'Cookie no one will eat', 'Last piece of lettuce  on the shelf', 'imperfect diamond', 'racist', 'Jew', 'dinosaur', 'bear-on-a-unicycle']

def insult():
    global a1
    global a2
    global n1
    print('You', randchoice(a1).lower(), randchoice(a2).lower(),
          randchoice(n1).lower()+'!')

while input() not in ('quit', 'exit', 'leave'):
    insult()
