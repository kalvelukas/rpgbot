**rpgsupportbot**

Chatbot Project in Python

for now my personal goals are:

1. run on Discord
2. roll dice to the chat
3. learn about test driven development
4. learn about and try a more complex project structure (pseudocomplexity on purpose)
5. at least get the diceroller ready in january ;)
------------
I aim for the following project structure: (C&C welcome)

rpgbot_project
├── code
│   ├── functions         # all the dicerolling, random encounters etc. happening here
│   |   ├── __init__.py
│   |   ├── dice.py
│   |   └── formatter.py
│   ├── libraries         # for information the program accesses
│   |   ├── resources     # stuff inside these folders, based on rule framework
│   |   ├── mobs
│   |   ├── npcs
│   |   ├── gear
│   |   ├── loot
│   |   ├── quests
│   |   ├── __init__.py
│   |   └── librarian.py
│   ├── __init__.py
│   └── client.py
├── test
|   ├── test_functions      # subdir for subpkg tests
|   │   ├── test_diceroller.py
|   │   └── __init__.py
|   ├── __init__.py         # test as separate package
|   └── test_client.py
|
.
.
.   # stuff i missed/will learn about

------------
Modules i managed to do so sloppy i am restructuring it completely on a test basis:
- helpmsg
- diceroll
------------
**I really have to clean up a lot of mess**
- redo code structure
- create sensible packages
- write the tests
