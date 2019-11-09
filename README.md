# Scanair Telegram BOT

Scanair Bot watches the trading rate of 2 currencies and send you a notification if it is below a specific amount.

## Setup

 - `pip3 install -r requirements.txt` to install the dependencies
 - Connect to postgresql and create a database
 - `python3 manage.py migrate` to set up the database
 - `./scripts/import.py` to insert the list of currencies
 - `cp .env.example .env` and update the required variables
 - `source .env` to load the environment
 - `python3 manage.py runserver` to start the project!

## Env

| NAME                  | DESC                                          |  VALUES   |
| :-------------------- | :-------------------------------------------- | :-------: |
| HOSTNAME              | Hostname to listen on                         | localhost |
| PORT                  | Port to listen on                             |   8080    |
| TELEGRAM_BOT_KEY      | Telegram private BOT key provided by Telegram |  SECRET   |
| CURRENCYLAYER_API_KEY | Currency Layer private API Key                |  SECRET   |
| PG_DB_HOST            | Postgresql Hostname                           | localhost |
| PG_DB_PORT            | Postgresql Hostname                           |   5432    |
| PG_DB_NAME            | Postgresql Hostname                           |  scanair  |
| PG_DB_USER            | Postgresql Hostname                           |  scanair  |
| PG_DB_PASS            | Postgresql Hostname                           |  scanair  |

## Project Organization

### Scanair

Core Config

### Currency Layer Api

Currency Layer Api wrapper (https://currencylayer.com/documentation)

### Telegram Bot

Telegram Bot interactions (https://core.telegram.org/bots)
