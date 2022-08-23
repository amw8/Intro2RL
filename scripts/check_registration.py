import sys
import pandas as pd

TAs = ['Andy Patterson', 'Tian Tian', 'Adam White', 'Subhojeet Pramanik', 'Yongchang Hao']

if len(sys.argv) < 3:
    print('Call using:')
    print('python3 scripts/check_registration.py <eclass_participant.csv> <coursera_gradebook.csv>')
    exit(1)

eclass_table = pd.read_csv(sys.argv[1])
coursera_table = pd.read_csv(sys.argv[2])

got_emails = list(coursera_table['Email'])
got_names = list(coursera_table['Full Name'])

students = []

for _, student in eclass_table.iterrows():
    name = student['First name'] + ' ' + student['Surname']
    email = student['Email address']

    # we don't need the TA information
    if name in TAs:
        continue

    found_email = email in got_emails
    found_name = name in got_names

    students.append((name, email, found_name, found_email))

students = pd.DataFrame(students, columns=['Name', 'Email', 'Correct Name', 'Correct Email'])

no_registration = students[~students['Correct Name'] & ~students['Correct Email']]
print('I was unable to find these students:')
print(no_registration)

print('Email addresses:')
out = '; '.join(no_registration['Email'])
print(out)
