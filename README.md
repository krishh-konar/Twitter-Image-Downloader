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

1. Edit the `API_Tokens.py` file and add these tokens you recieved in the previous step and save.
2. Run the script (`python twitter_image_downloader.py`).
3. Enter the user's twitter handle `(@twitter_handle)` you want to download images from, followed by max. number of tweets you want to search for.
4. The images are downloaded inside a folder named `twitter_images`, in the folder named `<user_handle>`.

