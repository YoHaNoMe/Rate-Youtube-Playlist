from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
import requests
import json

from googleapiclient.errors import HttpError


class Video:

    def __init__(self, **kwargs):
        self.__client_secrets_file = kwargs['client_secret_file']
        self.__scopes = kwargs['scopes']
        self.__api_name = kwargs['api_name']
        self.__api_version = kwargs['api_version']
        self.__API_KEY = kwargs['api_key']
        self.__client = self.get_authenticated_service()

    # authentication method
    # The first function being called to Get the Client
    def get_authenticated_service(self):
        flow = InstalledAppFlow.from_client_secrets_file(self.__client_secrets_file, self.__scopes)
        credentials = flow.run_console()
        return build(self.__api_name, self.__api_version, credentials=credentials)

    # rate the video
    def video_rate(self, **kwargs):
        kwargs = self.remove_empty_kwargs(**kwargs)

        respone = self.__client.videos().rate(
            **kwargs
        ).execute()
        return respone

    # remove empty values from dictionary
    def remove_empty_kwargs(self, **kwargs):
        good_kwargs = {}
        if kwargs is not None:
            for key, value in kwargs.items():
                if value:
                    good_kwargs[key] = value
        return good_kwargs

    # To get video rating (like, dislike, ..)
    def videos_get_rating(self, **kwargs):
        # See full sample for function
        kwargs = self.remove_empty_kwargs(**kwargs)
        response = self.__client.videos().getRating(
            **kwargs
        ).execute()
        return response

    # Get the ID of each video in a PlayList
    def get_play_list_videos_id(self, **kwargs):
        kwargs = self.remove_empty_kwargs(**kwargs)

        response = self.__client.playlistItems().list(
            **kwargs
        ).execute()

        return response

    # get the playlist length
    def __get_playlist_count(self, playlist_id):
        API_URL = 'https://www.googleapis.com/youtube/v3/playlists?part=contentDetails&id=' + playlist_id + '&key=' + self.__API_KEY
        response = requests.get(API_URL).text
        count = json.loads(response)['items'][0]['contentDetails']['itemCount']
        return 50 if count > 50 else count

    def __rate_playlist(self, play_list_id, rating, play_list_count=50, next_page_token=''):
        try:
            playlist = self.get_play_list_videos_id(
                part='snippet',
                maxResults=play_list_count,
                playlistId=play_list_id,
                pageToken=next_page_token
            )
            items = list(playlist['items'])
            try:
                next_page_token = playlist['nextPageToken']
            except KeyError:
                next_page_token = ''
            for item in items:
                snippet = item['snippet']
                position = snippet['position'] + 1
                print(rating + ' video ' + str(position) + ' ' + snippet['title'])
                video_id_per_item = snippet['resourceId']['videoId']
                from main import rate_video
                rate_video(self, video_id_per_item, rating)
            if next_page_token != '':
                self.__rate_playlist(
                    play_list_id,
                    rating,
                    next_page_token=next_page_token
                )

            result_dict = {'success': True, 'message': rating + 'd Successfully'}
        except HttpError as e:
            result_dict = {'success': False, 'message': e}
        return result_dict

    def rate_playlist(self, play_list_id, rating):
        play_list_count = self.__get_playlist_count(play_list_id)
        return self.__rate_playlist(play_list_id, rating, play_list_count)

    # @property
    # def client(self):
    #     return self.__client


