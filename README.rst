**rpgsupportbot**

Chatbot Project in Python

for now my personal goals are:

1. run on Discord
2. roll dice to the chat
3. learn about test driven dev
4. learn about and try a more complex project structure
5. at least get something ready in january ;)
------------
I aim for the following project structure: (C&C welcome)

rpgbot
├── sample
│   ├── functions         # all the dicerolling, random encounters etc. happening here
│   |   ├── __init__.py
│   |   ├── diceroller.py
│   |   └── client.py
│   ├── libraries         # for information the program accesses
│   |   ├── resources
│   |   ├── mobs
│   |   ├── npcs
│   |   ├── gear
│   |   ├── loot
│   |   ├── quests
│   |   ├── __init__.py
│   |   └── librarian.py
│   ├── __init__.py
│   └── client.py
└── test
    ├── test_functions      # subdir for detailed tests
    │   ├── test_diceroller.py
    │   └── __init__.py
    ├── __init__.py         # test as separate package
    └── test_client.py
|
.
.
.   # stuff i missed

------------
Modules i managed to do so sloppy i am restructuring it completely:
- helpmsg
- diceroll
------------
**I really have to clean up a lot of mess**
- redo code structure
- create sensible packages
- write the tests
