# -*- coding: utf-8 -*-
import re
import os
from videos import Video
from googleapiclient.errors import HttpError
import json
from pathlib import Path

CLIENT_SECRETS_FILE = ""
SCOPES = ['https://www.googleapis.com/auth/youtube.force-ssl']
API_SERVICE_NAME = 'youtube'
API_VERSION = 'v3'
API_KEY = ''
UTILITY_FILE_NAME = 'utility.txt'


def print_choice():
    print('*********************************\n1- Rate Video\n2- Rate Playlist\n3- '
          'Exit\n*********************************\n')


def choice_switcher(argument):
    info = 'Invalid choice'
    if argument == 1:
        info = str(input(
            "Enter the url of the video you want to rate then Comma(,) then the rate you want (Like, Dislike, None): ")).replace(
            ' ', '')
    elif argument == 2:
        info = str(input(
            "Enter the url of the playlist you want to rate then Comma(,) then the rate you want (Like, Dislike, "
            "None): ")).replace(' ', '')
    elif argument == 3:
        info = 'exit'
    return info


# rate video
def rate_video(video, video_id, rating):
    try:
        video.video_rate(
            id=video_id,
            rating=rating
        )
        result_dict = {'success': True, 'message': 'Done Successfully'}
    except HttpError as e:
        result_dict = {'success': False, 'message': e}
    return result_dict


# To extract the id of the video/playlist from the given url and the rate
def extract_id_rate(argument):
    if argument is None:
        return None
    try:
        # if argument.find('playlist') != -1:
        #     url_id = re.search(r'(?<=list=)\w+', argument).group(0)
        # else:
        #     url_id = re.search(r'(?<=\?v=)\w+[-]?(\w+)?', argument).group(0)
        url_id = re.search(r'((?<=list=)|(?<=\?v=)).+(?=,)', argument).group(0)
        try:
            rate = re.search(r'(?<=,)(like|dislike|none)$', argument, re.I).group(0).lower()
        except TypeError as e:
            url_id = -1
            rate = e
    except AttributeError as e:
        url_id = -1
        rate = e
    return {'id': url_id, 'rate': rate}


def print_error_message(e):
    content_error = json.loads(e.content.decode('utf-8'))
    message = content_error['error']['message']
    return message


def credentials_path_exists(secret_file):
    if Path(secret_file).exists():
        return True
    else:
        return False


if __name__ == '__main__':

    try:
        utility_path = Path(UTILITY_FILE_NAME)
        # If there is a file named utility
        if utility_path.is_file():
            # If the file doesnt contain any data
            if os.stat(utility_path).st_size == 0:
                # Prompt the user to enter credential path
                credentials_path = Path(input('Enter credentials path: '))
                # Prompt the user to enter the API key
                api_key = input('Enter API key: ')
                # Write to the file
                path = open(utility_path, 'w')
                path.write(str(credentials_path)+'\n')
                path.write(api_key)
            # Open the file, which is now containing data
            path = open(utility_path, 'r')
            CLIENT_SECRETS_FILE = path.readline().replace('\n', '')
            API_KEY = path.readline()
            path.close()
        # there is no utility file, it is deleted
        else:
            print('There is no utility file!, create a file and name it utility.txt then put it into the Code folder')
            exit()
    except Exception as e:
        print(e.args)

    # check if credential path, api key and secret_file endswith '.json' not empty
    if CLIENT_SECRETS_FILE == '' or not CLIENT_SECRETS_FILE.endswith('.json') or API_KEY == '':
        print('There are something wrong with credential path or api key, please read the documentaion page on Github carefully')
        exit()

    if not credentials_path_exists(CLIENT_SECRETS_FILE):
        path = open(utility_path, 'w')
        print('You have changed the path of Credentials or the file is not exist, please specify it again (open the program again!)')
        path.close()
        exit()

    os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'
    credential_dict = {
        'client_secret_file': CLIENT_SECRETS_FILE,
        'scopes': SCOPES,
        'api_name': API_SERVICE_NAME,
        'api_version': API_VERSION,
        'api_key': API_KEY
    }
    video = Video(**credential_dict)
    while True:
        # print choice menu
        print_choice()
        # check if the choice correct
        try:
            choice = int(input("enter choice: "))
        except ValueError:
            choice = -1
        # Getting the video/playlist url and rate if choice is 1 or 2, exit if the choice 3
        data_info = choice_switcher(choice)
        print('\n********************************* The Result *********************************')
        # Extract id and rate
        id_rate_dict = extract_id_rate(data_info)

        # Rate video
        if choice == 1:
            # # Extract id and rate
            # id_rate_dict = extract_id_rate(data_info)
            video_id = id_rate_dict['id']
            # Check if the user entered a valid url and rate splitted by Comma
            if video_id != -1:
                video_rate = id_rate_dict['rate']
                rate_video_dict = rate_video(video, video_id, video_rate)
                if rate_video_dict['success']:
                    print(rate_video_dict['message'])
                else:
                    print('Failed')
                    print(print_error_message(rate_video_dict['message']))
            else:
                print('Error: ' + str(
                    id_rate_dict['rate']) + ', Please check you entered a valid url and rate, Splitted by a comma')

        # Rate Playlist
        elif choice == 2:
            # # Extract id and rate
            # id_rate_dict = extract_id_rate(data_info)
            playlist_id = id_rate_dict.get('id')
            # Check if the user entered a valid url and rate splitted by Comma
            if playlist_id != -1:
                playlist_rate = id_rate_dict['rate']
                rate_playlist_dict = video.rate_playlist(playlist_id, playlist_rate)
                if rate_playlist_dict['success']:
                    print(rate_playlist_dict['message'])
                else:
                    print('Failed')
                    print(print_error_message(rate_playlist_dict['message']))
            else:
                print('Error: ' + str(
                    id_rate_dict['rate']) + ', Please check you entered a valid url and rate, Splitted by a comma')

        # Exit
        elif choice == 3:
            print(data_info + '\nBye Bye ...\n')
            exit()

        # Invalid choice
        elif choice == -1:
            print(data_info)
        print('******************************************************************\n')
