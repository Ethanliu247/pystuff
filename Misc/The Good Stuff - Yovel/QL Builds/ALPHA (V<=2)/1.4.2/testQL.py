import QL
from time import sleep

ql = QL.ql
QL.embedding = True

# Works as expected
ql('heapin <22> <What is your name?>')
answer = ql('heapget <22>')
print('Hello, '+answer.title()+'!')

# Works as expected
result = ql('execute <testing.ql>')
print(result)

# Works as expected
ql('file <testing.blah>')
sleep(5)
ql('scrap <testing.blah>')

# Looks like it all works fine!
# This is well on its way to being great!
