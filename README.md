# Rate Youtube Playlist
One day I opened Youtube and watched a playlist and then when I finished it, I really wanted to appreciate the man who made this playlist by liking it.
But I realized that I have to go through every video and like it. Worsen the situation more the playlist was in range of 30 to 50 videos, So it was so painful to do that.
Ummmm, should I have to open each video and like it?!!
Of course I did not do that. I have just made a program which can do that for me, Hurray, So if you have the same problem which i had don't worry, i got you ;). (Sorry for the cringe)

# Before you get started
You have to be familiar with Youtube API if you want to modify the code. Also you may want to have a look at [OAuth 2.0 for Installed Application](https://developers.google.com/api-client-library/python/auth/installed-app)
which it is the method that i used to make this program.

# Get started
1 - Go to [this website](https://console.developers.google.com/flows/enableapi?apiid=youtube) to select or create project:
    - click continue after selecting the appropriate choice for you.
    - On Add credentials for your project, click **Cancel**.
    - Select OAuth consent screen, Specify the application name and email address then click save.
    - Create Credentials then choose OAuth client ID.
    - Select the application type **other**, enter a name, and click **Create** button.
    - click the download button to the right of client id.
    - Rename the file any name you want and save it in your working directory.

2 - Install the Google APIs Client Library for Python:
    - pip install --upgrade google-api-python-client

3 - Install additional libraries:
    - pip install --upgrade google-auth google-auth-oauthlib google-auth-httplib2

Please if you have any problem at any of the above steps, refer to the [this link](https://developers.google.com/youtube/v3/quickstart/python) there are more detailed information.

4 - Make sure that your python version >= 3.5

4 - Run the main.py:
    - python3 main.py

# How the program works
After you run the program you will have to authorize the application, by using a link which should show up as soon as you run the program.
Then a menu will appear and you can choose to: Rate(like, dislike, none) a video, Rate a playlist or exit.Enter the url of video or playlist followed by a comma then the rate and enjoy ;).


# IMPORTANT Note
**Don't delete** a file named 'utility.txt'. it is very important file.
