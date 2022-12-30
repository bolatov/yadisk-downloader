# yadisk-downloader
Download all the media files from Yandex.Disk

## Development

1. Create and Activate Virtual Environment

```
python3 -m venv .venv

source .venv/bin/activate
```

2. Install required dependencies

```
pip3 install -r requirements.txt
```

3. Create a Yandex App that will be able to call its REST API

The app can be created on https://oauth.yandex.ru/. After the successful creation of the app, you should see
`ClientID` and `ClientSecret` values. 

4. Set the following environment variables

```
export YA_APP_CLIENT_ID=""
export YA_APP_CLIENT_SECRET=""
```
