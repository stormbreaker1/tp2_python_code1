# This program is testing the zip function.
name = ['meliodas','elizabeth','king','diana']
last = ['demon','angel','fairy','giant']

names_zip = zip(name, last)

for a,b in names_zip:
    print(a,b)