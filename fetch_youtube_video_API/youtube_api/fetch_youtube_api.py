# -*- coding: utf-8 -*-

# Sample Python code for youtube.channels.list
# See instructions for running these code samples locally:
# https://developers.google.com/explorer-help/code-samples#python

import os

import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors
from requests import HTTPError

from .models import Video
from youtube_api import settings
from datetime import datetime, timedelta


scopes = ["https://www.googleapis.com/auth/youtube.readonly"]

# This function would be fetching videos from YouTube API
def getnewposts():

    # Fetching the API keys from settings file
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"
    client_secrets_file = "client_auth.json"

    current_time = datetime.now()                 
    
    # Since we need to get the posts which were posted 5 minutes from current_time
    req_time = current_time - timedelta(minutes=5)

    # Get credentials and create an API client
    flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
        client_secrets_file, scopes)
    credentials = flow.run_console()
    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, credentials=credentials)

    request = youtube.channels().list(
        part="snippet,contentDetails,statistics",
        id="UC_x5XG1OV2P6uZZ5FSM9Ttw"
    )
    response = request.execute()

    # print(response)
    
    # flag variable to ensures the videos are successfully fetched.
    flag = False
    for apikey in credentials:
        try:
            # Called the youtube API as given in the documentation here : https://developers.google.com/youtube/v3/quickstart/python
            youtube = build("youtube", "v3", developerKey=apikey)
           
            # The searchable query is 'pokemon' here
            req = youtube.search().list(q="pokemon",part="snippet", order="date",
                                        maxResults=50, publishedAfter=(req_time.replace(microsecond=0).isoformat()+'Z') )
            response = req.execute()
          
            flag=True
            for obj in response['items']:
                title = obj['snippet']['title']
                description = obj['snippet']['description']
                publishingDateTime = obj['snippet']['publishedAt']
                thumbnailsUrls = obj['snippet']['thumbnails']['default']['url']
                channelTitle = obj['snippet']['channelTitle']

                # Saving the details in the DB
                Video.objects.create(title=title, description=description,
                        publishingDateTime=publishingDateTime, thumbnailsUrls=thumbnailsUrls,
                        channelTitle=channelTitle)

        # keep on using the same key if the quota for an api key is not exceeded 
        except HTTPError as er:
            err_code = er.resp.status
            if not(err_code == 400 or err_code == 403):
                break

        if flag:
            break