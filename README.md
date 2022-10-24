# Twitter Image Downloader
Downloads images/photos uploaded on twitter from a given twitter handle.

### Dependencies

This tool uses the Python [tweepy](www.tweepy.org) library and [wget](https://www.gnu.org/software/wget/) package.

You can install requirements using `requirements.txt`.

`pip install -r requirements.txt`

### Authorization Tokens

You will also need to create an app account on https://dev.twitter.com/apps to get authorization tokens

1. Sign in with your Twitter account
2. Create a new app.
3. Fill necessary details
4. Generate OAuth tokens for the app.

Following these steps and a successful app creation, you will recieve 3 tokens for your app, namely `API_KEY`, `API_KEY_SECRET` and `BEARER_TOKEN`. 
### Usage

* Edit the `API_Tokens.py` file and add these tokens you recieved in the previous step and save.

#### Using CLI
* Run using `twitter_image_downloader.py [-h] [-H HANDLE] [-n [MAX_TWEETS]] [-t [{images,videos,gifs,all} ...]]`

Examples:
```
python twitter_image_downloader.py --handle arsenal 
python twitter_image_downloader.py --handle arsenal --max-tweets 10 --type images,gifs
```
#### Using Interactive UI
1. Run the script (`python twitter_image_downloader.py`).
2. Enter the user's twitter handle `(@<twitter_handle>)` you want to download images from, followed by max. number of tweets you want to search for.
3. The images are downloaded inside a folder named `twitter_images`, in the folder named `<user_handle>`.

Example:
```
$ python twitter_image_downloader.py 

Twitter Image Downloader:
========================

Enter the twitter handle of the Account to download media from:  arsenal
Enter Max. number of tweets to search (default: 1000): 10
Enter type of media (images/gifs/videos/all) (default: images) gifs images

Fetching tweets.....
...
```
