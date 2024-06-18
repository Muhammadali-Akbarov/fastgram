# Fastgram template

Support Group - <a href="https://t.me/+bYouuOlqt1c3NmYy">Telegram</a><br>

# Installation
* 1 - clone repo 
  - ```git clone git@github.com:Muhammadali-Akbarov/fastgram.git```
* 2 - Setting up environment variables
  - ```cp .env.dist .env```
* 3 - RUN Project the following commands
  - ```make run.image``` - run with docker
* 4 - Run the following commands without docker
  - ```python3 -m venv venv```
  - ```source venv/bin/activate``` or ```./venv/Scripts/activate```
  - ```pip3 install -r requirements.txt```
  - ```uvicorn main:app --port ${SERVICE_PORT}``` run bot
  - ```celery -A app.bot.services.external.celery.tasks worker -l INFO``` run celery worker
  - ```celery -A app.bot.services.external.celery.tasks beat -l INFO``` run celery beat


## Technologies Used
Fastgram is built using the following technologies:
- **FastAPI**: A modern, fast (high-performance) web framework for building APIs with Python 3.6+ based on standard Python type hints.
- **aiogram 3**: An asynchronous framework for Telegram Bot API based on asyncio and aiohttp.
- **SQLAlchemy**: The Python SQL toolkit and Object-Relational Mapping (ORM) library.
- **PostgreSQL**: A powerful, open-source object-relational database system.
- **Redis**: An in-memory data structure store, used as a database, cache, and message broker.
- **Celery**: An asynchronous task queue/job queue based on distributed message passing.

This combination of technologies ensures that Fastgram is robust, scalable, and ready for production environments.


```
(fastgram) 🚀 fastgram % tree app/bot/services/external/aiogram
app/bot/services/external/aiogram
├── __init__.py
├── enum
│   ├── __init__.py
│   └── state.py
├── filter
│   ├── __init__.py
│   ├── chat.py
│   ├── payment.py
│   └── text.py
├── handler
│   ├── __init__.py
│   ├── echo.py
│   ├── example.py
│   └── start.py
├── keyboard
│   ├── __init__.py
│   ├── inline
│   │   ├── __init__.py
│   │   ├── create.py
│   │   └── default.py
│   └── markup
│       ├── __init__.py
│       ├── create.py
│       └── default.py
├── middleware
│   ├── __init__.py
│   └── lang.py
├── router
│   ├── __init__.py
│   └── prepare.py
├── shortcut
│   ├── __init__.py
│   ├── action.py
│   └── schema.py
├── state
│   ├── __init__.py
│   └── intro.py
└── storage
    ├── __init__.py
    └── fsm.py
```

