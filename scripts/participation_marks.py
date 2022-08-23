import sys
import numpy as np
import pandas as pd
from datetime import datetime
import pytz

TAs = ['Andrew Patterson', 'Tian Tian', 'Adam White', 'Subhojeet Pramanik', 'Yongchang Hao']

# what are the names of the assessments?
# needs to *exactly* match the name in the coursera csv
class Assessment:
    def __init__(self, course: int, name: str, month: int, day: int, hour: int, minute: int):
        # the course should specify if C1, C2, C3, C4
        assert course > 0 and course < 5

        self.course = course
        self.name = name
        self.due_date = datetime(
            year=2021,
            month=month,
            day=day,
            hour=hour,
            minute=minute,
            tzinfo=pytz.timezone('Canada/Mountain'),
        )

ASSIGNMENTS = [
    Assessment(1, 'Sequential Decision-Making',                       month=9,  day=7,  hour=23, minute=59),
    Assessment(1, 'MDPs',                                             month=9,  day=13, hour=13, minute=1),
    Assessment(1, '[Practice] Value Functions and Bellman Equations', month=9,  day=20, hour=13, minute=1),
    Assessment(1, 'Dynamic Programming',                              month=9,  day=27, hour=13, minute=1),
    Assessment(2, 'Blackjack',                                        month=10, day=11, hour=13, minute=1),
    Assessment(2, 'TD Methods Practice Quiz',                         month=10, day=11, hour=13, minute=1),
    Assessment(2, 'Practice Quiz',                                    month=10, day=18, hour=13, minute=1),
    Assessment(2, 'Practice Assessment',                              month=10, day=25, hour=13, minute=1),
    Assessment(3, 'On-policy Prediction with Approximation',          month=11, day=1,  hour=13, minute=1),
    Assessment(3, 'Constructing Features for Prediction',             month=11, day=22, hour=13, minute=1),
]

if len(sys.argv) < 3:
    print('Call using:')
    print('python3 scripts/participant_marks.py <eclass_participant.csv> <coursera_gradebook.csv ...>')
    exit(1)

eclass_table = pd.read_csv(sys.argv[1])

ass_names = tuple(a.name for a in ASSIGNMENTS)
mark_cols = tuple(0 for _ in ass_names)

people = []
for _, student in eclass_table.iterrows():
    name = student['First name'] + ' ' + student['Surname']
    email = student['Email address']
    ccid = student['CCID']

    # we don't need the TA information
    if name in TAs:
        continue

    people.append((name, ccid, email) + mark_cols)

people_table = pd.DataFrame(people, columns=('name', 'ccid', 'email') + ass_names)

# --------------------------------------------------------------
# -- First filter coursera csv to only participants of course --
# --------------------------------------------------------------
for assignment in ASSIGNMENTS:
    print('-----------------------------------------------------')
    print(f'----- {assignment.name} -----')
    arg = assignment.course + 1

    coursera_table = pd.read_csv(sys.argv[arg])
    coursera_table['Timestamp'] = pd.to_datetime(coursera_table['Timestamp'])

    got_emails = list(coursera_table['Email'])
    got_names = list(coursera_table['Full Name'])

    missing = 0
    for idx, student in people_table.iterrows():
        name = student['name']
        email = student['email']
        ccid = student['ccid']

        # first see if we can identify using email
        if email in got_emails:
            coursera_items = coursera_table[coursera_table['Email'] == email]

        # if not, then see if we can identify using name
        elif name in got_names:
            coursera_items = coursera_table[coursera_table['Full Name'] == name]

        else:
            # print(f'Warn: could not find {name}')
            missing += 1
            continue

        # ---------------------------
        # -- Now check submissions --
        # ---------------------------
        coursera_items = coursera_items[coursera_items['Assignment Name'] == assignment.name]

        submissions = coursera_items[(coursera_items['Change Type'] == 'Submitted') | (coursera_items['Change Type'] == 'Started')]
        graded_items = coursera_items[coursera_items['Change Type'] == 'Graded']

        submissions = submissions.sort_values('Timestamp')
        graded_items = graded_items.sort_values('Timestamp')

        # only consider submissions that resulted in a grade
        submissions = submissions[:len(graded_items)]

        total_submissions = len(submissions)
        submissions = submissions[submissions['Timestamp'] <= assignment.due_date]

        num_late = total_submissions - len(submissions)

        if len(submissions) == 0 and total_submissions > 0:
            # print(f'All submissions for {name} were late')
            missing += 1
            continue

        if len(submissions) == 0:
            # print(f'{name} did not submit')
            missing += 1
            continue

        # --------------------------
        # -- Finally check grades --
        # --------------------------

        if num_late > 0:
            # remove the last N grades if some of the submissions were late
            graded_items = graded_items[:-num_late]

        if len(graded_items) == 0:
            # print(f'ERROR: found submissions but no grades for {name}')
            missing += 1
            continue

        # I'm going to be nice and select the highest grade of all submissions before deadline
        # which might be different than the _last_ grade before deadline
        grade = max(graded_items['Assignment Grade'])

        if grade >= 0.8:
            grade = 1
        else:
            grade = 0

        people_table.loc[idx, assignment.name] = grade

    print(f'Missing: {missing} / {len(people_table)}')

people_table.to_csv('all_marks.csv', index=False)

def agg(row):
    marks = row.iloc[3:]
    arr = np.asarray(marks)

    # drop the 2 lowest marks
    arr = np.sort(arr)[2:]

    # worth .6% each
    return arr.sum() * (6 / 9)

grade_table = people_table[['name', 'ccid']].assign(grade = people_table.agg(agg, axis=1))
grade_table.to_csv('to_upload.csv', index=False)

# # ----------------------
# # -- Grade statistics --
# # ----------------------
# avg = np.mean(grades['grade'])
# std = np.std(grades['grade'])
# lo = np.min(grades['grade'])

# print('-------------------------------------------')
# print('Assignment statistics:')
# print(f'min: {lo}  mean: {avg}  std: {std}')
