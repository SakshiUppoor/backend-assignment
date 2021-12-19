
# Chess Youtube

A REST API that continuously fetches latest chess-related Youtube videos and saves them.


## Installation

- Clone the repository
    
    git clone https://github.com/SakshiUppoor/chess-youtube.git
    
- Add your Youtube API key(s) to `YOUTUBE_API_KEYS` in [chessYoutube/credentials.json](https://github.com/SakshiUppoor/chess-youtube/blob/master/chessYoutube/credentials.json)
```
    "YOUTUBE_API_KEYS": [
        "PASTE_YOUR_API_KEY1_HERE",
        "PASTE_YOUR_API_KEY2_HERE"
    ]
```

- Create a virtual environment and activate it _(Optional but recommended)_

    virtualenv venv
    cd Scripts
    activate

- Navigate back to the main folder. Installing dependencies

    pip install -r requirements.txt

- Make migrations
    python manage.gy makemigrations
    python manage.py migrate

- Start the server
    python manage.py runserver

The server should be live at http://127.0.0.1:8000/ :rocket:

## Endpoints Reference

#### List of videos

```http
  GET /api/list
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `page` | `int` | Page number (default=1) |
| `limit` | `int` | Number of videos per page (default=5) |

Returns a paginated list of saved Youtube videos in a reverse chronological order.

#### Dashboard

```http
  GET /dashboard
```
Displays a basic dashboard which utilizes the above REST API endpoint.


## Features

- **Background Scheduler**
    
    To fetch and save new videos to the database asynchronously every 25 seconds
- **Support for supplying multiple API keys**
    
    If quota is exhausted on one, it automatically uses the next available key.
- **Dashboard**

