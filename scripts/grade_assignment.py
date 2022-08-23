import sys
import numpy as np
import pandas as pd
from datetime import datetime
import pytz

TAs = ['Andrew Patterson', 'Tian Tian', 'Adam White', 'Subhojeet Pramanik', 'Yongchang Hao']

# what is the name of the assignment?
# needs to *exactly* match the name in the coursera csv
ASSIGNMENT = 'Semi-gradient TD with a Neural Network'
# usually offset this by a few hours to be lenient with due dates
# i.e. if due at midnight on the 26th, might set this to 4am on the 27th
DUE_DATE = datetime(
    year=2021,
    month=11,
    day=26,
    hour=13,
    minute=59,
    tzinfo=pytz.timezone('Canada/Mountain'),
)

if len(sys.argv) < 3:
    print('Call using:')
    print('python3 scripts/grade_assignment.py <eclass_participant.csv> <coursera_gradebook.csv>')
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

late_submissions = 0
for _, student in eclass_table.iterrows():
    name = student['First name'] + ' ' + student['Surname']
    email = student['Email address']
    ccid = student['CCID']

    # we don't need the TA information
    if name in TAs:
        continue

    # first see if we can identify using email
    if email in got_emails:
        coursera_items = coursera_table[coursera_table['Email'] == email]

    # if not, then see if we can identify using name
    elif name in got_names:
        coursera_items = coursera_table[coursera_table['Full Name'] == name]

    else:
        print(f'Warn: could not find {name}')
        # NOTE: We can ignore these people while grading and eclass will just give them a zero
        # grades.append((name, ccid, email, 0))
        continue

    # ---------------------------
    # -- Now check submissions --
    # ---------------------------
    coursera_items = coursera_items[coursera_items['Assignment Name'] == ASSIGNMENT]

    submissions = coursera_items[(coursera_items['Change Type'] == 'Submitted') | (coursera_items['Change Type'] == 'Started')]
    graded_items = coursera_items[coursera_items['Change Type'] == 'Graded']

    submissions = submissions.sort_values('Timestamp')
    graded_items = graded_items.sort_values('Timestamp')

    # only consider submissions that resulted in a grade
    submissions = submissions[:len(graded_items)]

    total_submissions = len(submissions)
    # also only consider submissions that occur before the deadline
    submissions = submissions[submissions['Timestamp'] <= DUE_DATE]

    num_late = total_submissions - len(submissions)

    # if we've filtered out all submissions, that means they were all late.
    # these might require manual grading
    # for now, these are added to the gradebook as a 0
    if len(submissions) == 0 and total_submissions > 0:
        print(f'All submissions for {name} were late')
        late_submissions += 1
        grades.append((name, ccid, email, 0))
        continue

    if len(submissions) == 0:
        print(f'{name} did not submit')
        # NOTE: eclass will automatically give a zero for anyone not in the uploaded csv, but will record it as a NaN
        # this way we can distinguish after-the-fact who submitted and got a 0 vs. who did not submit
        # grades.append((name, ccid, email, 0))
        continue

    # --------------------------
    # -- Finally check grades --
    # --------------------------

    if num_late > 0:
        # remove the last N grades if some of the submissions were late
        graded_items = graded_items[:-num_late]

    # ideally we should never get here
    # but the coursera data is often weird
    if len(graded_items) == 0:
        print(f'ERROR: found submissions but no grades for {name}')
        continue

    # I'm going to be nice and select the highest grade of all submissions before deadline
    # which might be different than the _last_ grade before deadline
    grade = max(graded_items['Assignment Grade'])

    # TODO: change for any grade transformations we might (or might not) want to do
    # if grade >= 0.8 and grade < 0.95:
    #     grade = 0.95

    # eclass expects grades to be out of 100
    # but coursera gives grades between [0, 1]
    grades.append((name, ccid, email, grade * 100))

grades = pd.DataFrame(grades, columns=['name', 'ccid', 'email', 'grade'])
grades.to_csv('to_upload.csv', index=False)

# ----------------------
# -- Grade statistics --
# ----------------------
avg = np.mean(grades['grade'])
std = np.std(grades['grade'])
lo = np.min(grades['grade'])

print('-------------------------------------------')
print('Assignment statistics:')
print(f'min: {lo}  mean: {avg}  std: {std}')
print(f'Num late: {late_submissions}')
