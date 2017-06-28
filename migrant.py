import csv

def ladcodes(list):
    with open('./data/de2016.csv') as f:
        file = csv.DictReader(f, delimiter=',')
        for row in file:
            if row['OutLA'] not in list:
                list.append(row['OutLA'])
            elif row['InLA'] not in list:
                list.append(row['InLA'])
            else:
                pass

def ladnames(dictionary):
    if isinstance(dictionary, dict):
        with open('./data/ladcodes.csv') as f:
            file = csv.DictReader(f, delimiter=',')
            headers = file.fieldnames
            for row in file:
                dictionary[row[headers[0]]] = row[headers[2]]
            dictionary['S92000003'] = 'Scotland'
            dictionary['N92000002'] = 'Northern Ireland'
    else:
        print('ladnames requires an empty dictionary')

def leavingLondon(list):
    with open('./data/de2016-2.csv') as f:
        file = csv.DictReader(f, delimiter=',')
        for person in file:
            if person['InLA'].startswith('E09'):
                pass
            elif person['OutLA'].startswith('E09'):
                list.append(person)
            else:
                pass

def enteringLondon(list):
    with open('./data/de2016.csv') as f:
        file = csv.DictReader(f, delimiter=',')
        for person in file:
            if person['OutLA'].startswith('E09'):
                pass
            elif person['InLA'].startswith('E09'):
                list.append(person)
            else:
                pass
    with open('./data/de2016-2.csv') as g:
        gFile = csv.DictReader(g, delimiter=',')
        for person in gFile:
            if person['OutLA'].startswith('E09'):
                pass
            elif person['InLA'].startswith('E09'):
                list.append(person)
            else:
                pass

def leavingSomewhere(list, string):
    with open('./data/de2016-2.csv') as f:
        file = csv.DictReader(f, delimiter=',')
        for person in file:
            if person['InLA'].startswith(string):
                pass
            elif person['OutLA'].startswith(string):
                list.append(person)
            else:
                pass
    with open('./data/de2016.csv') as f:
        file = csv.DictReader(f, delimiter=',')
        for person in file:
            if person['InLA'].startswith(string):
                pass
            elif person['OutLA'].startswith(string):
                list.append(person)
            else:
                pass

def enteringSomewhere(list, string):
    with open('./data/de2016-2.csv') as f:
        file = csv.DictReader(f, delimiter=',')
        for person in file:
            if person['OutLA'].startswith(string):
                pass
            elif person['InLA'].startswith(string):
                list.append(person)
            else:
                pass
    with open('./data/de2016.csv') as f:
        file = csv.DictReader(f, delimiter=',')
        for person in file:
            if person['OutLA'].startswith(string):
                pass
            elif person['InLA'].startswith(string):
                list.append(person)
            else:
                pass

def genderSplit(list):
    m = 0
    f = 0
    for person in list:
        if person['Sex'] == 'F':
            f += 1
        else:
            m += 1
    print('females', f, 'males', m)

def ageSplit(list):
    d = dict((x['Age'], 0) for x in list)
    for person in list:
        d[person['Age']] +=1
    print(d)
    print(d['19'])
