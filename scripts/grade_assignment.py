import sys
import numpy as np
import pandas as pd
from datetime import datetime
import pytz

TAs = ['Andrew Patterson', 'Tian Tian', 'Adam White', 'Subhojeet Pramanik', 'Yongchang Hao']

# what is the name of the assignment?
# needs to *exactly* match the name in the coursera csv
ASSIGNMENT = 'Bandits and Exploration/Exploitation'
DUE_DATE = datetime(2021, 10, 10, 1, 0, tzinfo=pytz.timezone('Canada/Mountain'))

if len(sys.argv) < 3:
    print('Call using:')
    print('python3 scripts/check_registration.py <eclass_participant.csv> <coursera_gradebook.csv>')
    exit(1)

# --------------------------------------------------------------
# -- First filter coursera csv to only participants of course --
# --------------------------------------------------------------
eclass_table = pd.read_csv(sys.argv[1])
coursera_table = pd.read_csv(sys.argv[2])

coursera_table['Timestamp'] = pd.to_datetime(coursera_table['Timestamp'])

got_emails = list(coursera_table['Email'])
got_names = list(coursera_table['Full Name'])

grades = []

for _, student in eclass_table.iterrows():
    name = student['First name'] + ' ' + student['Surname']
    email = student['Email address']
    ccid = student['CCID']

    # we don't need the TA information
    if name in TAs:
        continue

    # first see if we can identify using email
    if email in got_emails:
        submissions = coursera_table[coursera_table['Email'] == email]

    # if not, then see if we can identify using name
    elif name in got_names:
        submissions = coursera_table[coursera_table['Full Name'] == name]

    else:
        print(f'Warn: could not find {name}')
        grades.append((name, ccid, email, 0))
        continue

    # ----------------------
    # -- Now check grades --
    # ----------------------

    submissions = submissions[submissions['Change Type'] == 'Graded']
    submissions = submissions[submissions['Assignment Name'] == ASSIGNMENT]
    total_submissions = len(submissions)
    submissions = submissions[submissions['Timestamp'] <= DUE_DATE]

    if len(submissions) == 0 and total_submissions > 0:
        print(f'All submissions for {name} were late')

    if len(submissions) == 0:
        print(f'{name} did not submit')
        # TODO: need to actually append a 0 here
        grades.append((name, ccid, email, 0))
        continue

    # I'm going to be nice and select the highest grade of all submissions before deadline
    # which might be different than the _last_ grade before deadline
    grade = max(submissions['Assignment Grade'])

    # TODO: change for any grade transformations we might (or might not) want to do
    if grade >= 0.8 and grade < 0.95:
        grade = 0.95

    grades.append((name, ccid, email, grade * 100))

grades = pd.DataFrame(grades, columns=['name', 'ccid', 'email', 'grade'])
grades.to_csv('to_upload.csv', index=False)
