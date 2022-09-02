"""
Riddle list of dictionaries.
List contains six riddles each with a question with the key of riddle
and an answer with the key of correct.
Riddle questions also include escape sequences for bold and italic font
styling which are printed to the terminal with the riddles.
Riddle questions and answers are selected and set to variables for each
riddle function and passed into the riddle me this function as arguments. 
"""

riddle = [
    {
        "riddle": '''    \033[1m\x1B[3m"What can run, but never walks;\n
    has a mouth, but never talks;\n
    has a head, but never weeps;\n
    has a bed, but never sleeps?"\n\x1B[0m\033[0m''',
        "correct": "river"
    },
    {
        "riddle": '''    \033[1m\x1B[3m"Halo of water, tongue of wood,\n
    skin of stone, long I've stood.\n
    My fingers short reach to the sky,\n
    inside my heart men live and die.\n
    What am I?"\n\x1B[0m\033[0m''',
        "correct": "castle"
    },
    {
        "riddle": '''    \033[1m\x1B[3m"First think of the person who lives in\
 disguise,\n
    who deals in secrets and tells naught but lies.\n
    Next, tell me what's always the last thing to mend,\n
    the middle of middle and the end of the end.\n
    Finally, give me the sound often heard during the search\n
    for a hard-to-find word.\n
    Now, string them together, and answer me this:\n
    Which creature would you be unwilling to kiss?"\n\x1B[0m\033[0m''',
        "correct": "spider"
    },
    {
        "riddle": '''    \033[1m\x1B[3m"What is old and sometimes new;\n
    never sad, sometimes blue;\n
    never empty, but sometimes full;\n
    never pushes, always pulls?"\n\x1B[0m\033[0m''',
        "correct": "moon"
    },
    {
        "riddle": '''    \033[1m\x1B[3m"Reaching stiffly for the sky,\n
    I bare my fingers when it's cold.\n
    In warmth I wear an emerald glove\n
    and in between I dress in gold.\n
    What am I?"\n\x1B[0m\033[0m''',
        "correct": "tree"
    },
    {
        "riddle": '''    \033[1m\x1B[3m"What does man love more than life,\n
    hate more than death or mortal strife;\n
    that which contented men desire;\n
    the poor have, the rich require;\n
    the miser spends, the spendthrift saves,\n
    and all men carry to their graves?"\n\x1B[0m\033[0m''',
        "correct": "nothing"
    }
]