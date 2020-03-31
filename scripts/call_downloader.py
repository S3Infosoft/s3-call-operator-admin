import localsettings
import requests


def fetch_download_link():
    """
    Fetch Download Link
    TODO: Exception Handling and validation for absence of keys.
    """
    payload = "token=%s&file=%s" % (localsettings.OPERATER_TOKEN, localsettings.SAMPLE_CALL_FILENAME)
    response = requests.get(localsettings.URL_DOWNLOAD_LINK, params=payload)
    response_data = response.text
    print(response_data)


if __name__ == "__main__":
    fetch_download_link()
