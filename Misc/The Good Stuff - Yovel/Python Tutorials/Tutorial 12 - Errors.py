# You should have learned this a while back, but late is better than never!
import sys

# When you do something terribly wrong
prin sme tex ot blh bah bla '''''''' 12y371263498716234' 'e kl hkjlashd))))'))')')'''
# Then python will try to tell you with an error message
# Sometimes, this is annoying and all you want to do is ignore the error and move on

# There are two terms you need to know
# Catch: intercept an error and handle it
# Throw: raise an exception that can be handled

# So, you tell python to TRY to do something and if there is an exception, do something else
try:
    prin some blah
except:
    print('This did not work')
# Now, when you try to 'prin some blah' python will continue with the program and complain with 'This did not work'

# There is something more useful you can do though, in case you don't know what went wrong
try:
    prin some blah
except Exception as e:
    print(e)
# This gets the exception that occurred, and stores it as the local variable e. It then prints out e.
# Sometimes you want to do different things for different errors. There are a multitude of errors
try:
    prin some blah
except TypeError:
    print('There was a type error')
except SyntaxError:
    print('Your syntax is invalid')
except Exception:
    print('Something else happened')

# Seeing any similarities to something you learned already?
# This looks a bit like an elif, an elif, and an else
# That's basically how it works

# Now, there are some errors you should try not to catch
# For example, pressing control-c during a program will stop it
# This is known as Keyboard Interrupt
# You can catch it
try:
    while True:
        input('Type stuff')
except KeyboardInterrupt:
    print('You interrupted the program')
    sys.exit(0)
# Sometimes you want to catch this, so that you don't get a big fat error or you want to make a custom exit message
# But usually, you don't want to catch this error because then you might have problems actually interrupting the program

# There are some more useful ones

EOFError
ArithmeticError
AttributeError
KeyError

# And there are some not so useful ones

KeyboardInterrupt  # You should want this error to exist
SystemExit         # It wouldn't be good if the program can't quit itself
ZeroDivisionError  # Just don't divide by zero


# So, that's error handling!

# You can also CAUSE an error directly using raise

if 'y' not in input('If you want an error, say no\n'):
    raise SystemExit  # Error throwing
else:
    print('Yay!')

# If the user says no, then the system exits with a SystemExit error
# This is not a great example, but you can make your own errors too!
raise 'End of the program'
# This will exit the program with an error message akin to that

# And that's all for errors!