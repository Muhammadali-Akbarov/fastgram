# Fastgram template

# Installation
* 1 - clone repo 
  - ```git clone git@github.com:Muhammadali-Akbarov/fastgram.git```
* 2 - Setting up environment variables
  - ```cp .env.dist .env```
* 3 - RUN Project the following commands
  - ```make setup```


```
(fastgram) 🚀 fastgram % tree app/bot/services/external/aiogram
app/bot/services/external/aiogram
├── __init__.py
├── button
│   ├── inline
│   │   ├── __init__.py
│   │   ├── create.py
│   │   └── default.py
│   └── markup
│       ├── __init__.py
│       ├── create.py
│       └── default.py
├── enums
│   ├── __init__.py
│   └── state.py
├── handler
│   ├── __init__.py
│   ├── echo.py
│   └── start.py
├── middleware
│   ├── __init__.py
│   └── lang.py
├── shortcut
│   ├── __init__.py
│   ├── action.py
│   ├── btns.py
│   ├── location.py
│   ├── message.py
│   └── schema.py
├── state
│   ├── __init__.py
│   └── intro.py
└── storage
    ├── __init__.py
    └── fsm.py

10 directories, 24 files
```