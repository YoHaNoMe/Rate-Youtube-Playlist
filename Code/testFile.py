import re
import requests
import json
# x = 'https://www.youtube.com/watch?v=H94TyyavGIE,Dislike'
#
# searched = re.search(r'(?<=,)like|dislike|none', x, re.I)
#
# print(searched.group(0))

# API_URL = 'https://www.googleapis.com/youtube/v3/playlists?part=contentDetails&id=PL7B2B7D9520020C16&key=AIzaSyBgVuGaJuQOdFdiclQD8Zy0H06yjjBQSfo'
# response = requests.get(API_URL).text
# print(response)
# print('*************')
# json_e = json.loads(response)
# print(json_e['items'][0]['kind'])


from pathlib import Path

# file = Path('/home/youssef/PycharmProjects/YoutubeAPIPlaylists/Credentials/test.txt')
# if file.is_file():
#     if str(file).endswith('.json'):
#         print('yes')
#     else:
#         print('no')
# else:
#     print('no')
# f = open('utility.txt', 'a')
# f.write('asdlsadksadksafsajf')


# path = Path(input('The path to credentials: '))
#
# if path.is_file():
#     local_path = str(path)
#     f = open('utility.txt', 'x')
#     f.write(local_path)
#     f.close()
#     print('hello')

f = open('utility.txt', 'r')
print(f.readline())
print(f.readline())




# import re
# import os
#
# from googleapiclient.errors import HttpError
#
# import getRating as rate
# import videos as vid
#
#
# def choose_choice(argument):
#     choices = {
#         '1': 'hello world',
#         '2': 'hey man how are you',
#     }
#
#     return choices.get(argument, 'Invalid')
#
#
# CLIENT_SECRETS_FILE = "../Credentials/client_secret.json"
# SCOPES = ['https://www.googleapis.com/auth/youtube.force-ssl']
# API_SERVICE_NAME = 'youtube'
# API_VERSION = 'v3'
#
# if __name__ == '__main__':
#     os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'
#     credential_dict = {
#         'client_secret_file': CLIENT_SECRETS_FILE,
#         'scopes': SCOPES,
#         'api_name': API_SERVICE_NAME,
#         'api_version': API_VERSION
#     }
#     video = vid.Video(**credential_dict)
#     try:
#         response = video.video_rate(id='H94TyyavGIEasfdasfafas', rating='like')
#         if response is None:
#             print('None')
#         elif response == '':
#             print('Empty')
#         else:
#             print("Error")
#         print(response)
#     except HttpError:
#         print('Error Really')
#
#
# # # x = input("Enter a number")
# # # print(choose_choice(x))
# # url_playlist = 'https://www.youtube.com/watch?v=yDntCIs-IJM&list=PL6gx4Cwl9DGAKWClAD_iKpNC0bGHxGhcx&index=3;like'
# # url_video = 'https://www.youtube.com/watch?v=z0xNlfrXkVU;dislike'
# # play_url = 'https://www.youtube.com/playlist?list=PL6gx4Cwl9DGAKWClAD_iKpNC0bGHxGhcx;like'
# # #modified = re.search(r'(?<=\?v=)\S+=?', url_video)
# # #modified = re.search(r'(?<=\?v=)\S+(?=&)(?!\blist\b)', url_playlist)
# # #modified = re.search(r'(?<=\?v=)\S{11}', url_playlist)
# #
# #
# #
# #
# #
# # #modified = re.search(r'(?<=;)\w+',play_url)
# # #modified = re.search(r'(?<=list=)\w+' , play_url)
# # modified = re.search(r'(?<=\?v=)\w+[-]?(\w+)?', url_video)
# # #modified = re.search(r'(?<=\?v=)\w+', url_video)
# # print(modified.group().split())
# # # print(modified.group(0))
# # # print(modified.group().split())
