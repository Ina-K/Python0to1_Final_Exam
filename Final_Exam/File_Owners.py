"""
File Owners
"""

"""
File Owners
"""

def group_by_owners(files):

    kkeys = list(set(files.values())) #unique list of names

    odic = dict()
    for ind in kkeys:
        odic.setdefault(ind, [k for k, v in files.items() if v == ind]) # .items gives all the keys and values

    return odic

files = {
    'Input.txt': 'Randy',
    'Code.py': 'Stan',
    'Output.txt': 'Randy'
}
print(files.items())
print(group_by_owners(files))
