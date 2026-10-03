import random
import os
import time
import datetime as dt

class BadLetterError(Exception):

    def __init__(self, message = 'Some of those letters are not nice'):
        self.message = message
        super().__init__(message)


    pass


class BadTimeError(Exception):
    pass


def readfile():
    try:
        with open('booster.txt', mode = 'r') as file:
            print(file.readline())
    except FileNotFoundError:
        print('You are out of luck today')







def short_form(idx, *names):
    #print(names)
    final =''
    try:
        for name in names:
            final = final+name[idx]


    except IndexError as e:
        print('Indexing is incorrect', e)
    except TypeError as e:
        print('Wrong data type', e)
    except Exception as e:
        print('Something is wrong', e)

    else:
        print('Looks good')
        return final.upper()
    finally:
        print('Hope you passed this stage')
        print('Try readfile() to see your luck')
        if random.randint(1,100) < 10:
            with open('booster.txt', mode = 'w') as file:
                file.write('You are lucky')


    #final = name1[0]+ name2[0]
    #return final.upper()

strength = {'name':10, 'surname':20, 'nickname':30, 'alias':40, 'aka': 50}


def name_strength(**fullname):
    results = 0
    try:
        for key, value in fullname.items():
            result += strength[key]*len(value)
    except KeyError as e:
        print('perhaps you are giving too many fields', e)
    else:
        return result

def validate(**prelimdata):
    try:
        assert prelimdata['sc'] != None
        assert prelimdata['ns'] != None
    except KeyError as e:
        print('You are bad at typing')
        print('Validation failed due to', e)
    except AssertionError as e:
        print('One of the earlier stages did not work')
        print('Validation failed due to', e)
    else:
        print('Looking food so far ...')
        print('Sending for deeper validation')
        print('Opening connection o a remote server ...')

        try:
            deep_validate(prelimdata)
        except ValueError:
            print('There is something deeply wrong ...')
            print('Validation has failed')
        except BadLetterError as e:
            print('I did not like some of the letters ...', e)
            print('Validation Failed')
        except BadTimeError as e:
            print('The timing is not looking good, please try again later')
            print('Validation Failed')
        else:
            print("Congrats ... Validation Succesful")
            print('Congrats ... Welcome to my world')
        finally:
            print('Closing connection to the remote server ...')

def deep_validate(prelimdata):
    print(prelimdata)
    threshold_sc = random.randint(80,100)
    threshold_ns = random.randint(2000,3000)

    print(threshold_ns, threshold_sc)

    badLetters = ['a', 'r', 'e']

    ct = dt.datetime.now()

    if ct.second % 2 == 0:
        raise BadTimeError


    if any(x in prelimdata['sc'] for x in badLetters):
        raise BadLetterError('Please avoid a, r, and e')

    if len(prelimdata['sc'])< threshold_sc or prelimdata['ns'] < threshold_ns:
        raise ValueError


print('Welcome to the Programmers\' Den')
print("I hear you have been learning Python")
print("Guess you can use the command line to create your own welcome kit")

print()

print('You may want to read the README file for instructions')
print('Since I guess you may be lazy, I guess I will put the instructions here')

print()


print ('The process is simple, create a short code, a few words about ourself, prefix = , suffix = ')
print('For name strenght code, use ns = name_strength(name =, surname, = , aka = , salutaion =)')
print('For validate, use validate (sc = sc, ns = ns)')

print('Alright champ, get going ...')

try:
    os.remove('bosster.txt')
except FileNotFoundError:
    pass




print(' ')