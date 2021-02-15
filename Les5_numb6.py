# я не выдержала сплитить по символам и буду через регулярные
import re

with open('subjects.txt', 'r') as file:
    subj_dict = {}
    for line in file:
        if line.strip():
            hours = [int(i) for i in re.findall(r'(?<![A-Za-z0-9.])\d+\.*\d+(?!\w)', line)]
            subj_dict.update({line.split()[0]: sum(hours)})
print(subj_dict)
