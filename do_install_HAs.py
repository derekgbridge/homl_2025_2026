import sys
import os
from IPython.display import display, Markdown

def initialize():
    nb_filename = sys.argv[1]
    (root, ext) = os.path.splitext(nb_filename)
    ha_filename = root + "_HA.txt"
    ha_pathname = os.path.join(os.getcwd(), "has", ha_filename)
    if not os.path.exists(ha_pathname):
        display(Markdown(f"Error! I'm looking for a file called '{ha_filename}' in the 'has' folder. Make sure this file exists and re-run this cell. Hints and answers will not be available until this has been done."))
        return [], []
    with open(ha_pathname, 'r+', encoding='utf-8') as f:
        lines = f.readlines()
    hints = []
    answers = []
    is_hint = None
    val = ""
    for line in lines:
        if line.startswith("<<<"):
            if val and is_hint:
                hints.append(val)
            elif val:
                answers.append(val)
            val = ""
            is_hint = True if line.startswith("<<<H") else False
        else:
            val += line
    if val:
        answers.append(val)
    return hints, answers

def hint(n):
    if len(hints) == 0:
        display(Markdown("There are no hints. There was a code cell at the start of the Notebook to create the hints. Did you run it? Did it run without error?"))
    elif type(n) is int and 1 <= n <= len(hints):
        display(Markdown(hints[n - 1]))
    else:
        display(Markdown(f"To get a hint, supply an integer between 1 and {len(hints)} inclusive."))

def answer(n):
    if len(answers) == 0:
        display(Markdown("There are no answers. There was a code cell at the start of the Notebook to create the answers. Did you run it? Did it run without error?"))
    elif type(n) is int and 1 <= n <= len(answers):
        display(Markdown("```\n" + answers[n - 1] + "\n```"))
    else:
        display(Markdown(f"To get an answer, supply an integer between 1 and {len(answers)} inclusive."))

hints, answers = initialize()



