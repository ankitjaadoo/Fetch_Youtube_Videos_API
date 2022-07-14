### Project Goal ✨

To make an API to fetch latest videos sorted in reverse chronological order of their publishing date-time from YouTube for a given tag/search query in a paginated response.

## About it :scroll:	

* choose any search query, for example: official, cricket, football and GET API will returns the stored video data in a paginated response sorted in descending order of published datetime.
* Added support for supplying multiple API keys so that if quota is exhausted on one, it automatically uses the next available key.

## Tech Stack :memo:
 * Django
 * Django Rest Framework
 * YouTube data v3 API

## Setting Up 🔨

 <details>
  <summary><strong>Setup Steps</strong></summary>

- Clone the Repository
 ```
$ git clone https://github.com/ankitjaadoo/Fetch_Youtube_Videos_API
 ```
- Go the the folder
 ```
$ cd fetch_youtube_video_API
 ```
- Setup Virtual environment
 ```
$ python3 -m venv env
```
- Activate the virtual environment
```
$ source env/Scripts/activate - for Windows
$ source env/bin/activate - for Mac
```
- Install dependencies using
```
$ pip install -r requirements.txt
```
- Modify settings.py File - Remove the existing keys and add your own YouTube Data API keys in the form [key1, key2, ...]:
```
$ API_KEYS = ['Google_API_Key_1', 'Google_API_Key_2','Google_API_Key_3',] 
```
- Make migrations using
```
$ python manage.py makemigrations
```
- Migrate Database
```
$ python manage.py migrate
```
- Create a superuser
```
$ python manage.py createsuperuser
```
- Run server using
```
$ python manage.py runserver
``` 
  
</details>


## Usage :label:

Run the manage.py file:

```python
python manage.py runserver
```
## Reference:

    YouTube data v3 API: https://developers.google.com/youtube/v3/getting-started
    Search API reference: https://developers.google.com/youtube/v3/docs/search/list
    To fetch the latest videos you need to specify these: type=video, order=date, publishedAfter=<SOME_DATE_TIME>
    Without publishedAfter, it will give you cached results which will be too old


## Directory Structure
    
    API_Youtube            
    .
    ├── Contains       
    |   ├── Images            # Contain screenshots of the project and other images
    │   ├── API               # The main Django app/api containing the models, views, serializers etc
    │   ├── API_Youtube       # All the settings and url routes settings of the REST API
    |   ├── db.sqlite3        # SQLite database housing the data of the videos fetched
    │   └── manage.py         # Python code used for starting the app by establishing DRF server
    |   └── requirements.txt  # Requirements file
    |______________________   
[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://github.com/ankitjaadoo/Fetch_Youtube_Videos_API)