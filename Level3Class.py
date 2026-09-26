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