import http.client
import urllib
from datetime import datetime
from src.scraper import scrape_tfl 

def main(stationURL, dataPlatformID, linesList, pushoverKeys):
    """
    Main function to scrape train times and send notifications.

    Args:
    stationURL (str): URL of the TfL station to scrape.
    dataPlatformID (str): Data-platform ID for locating departure information.
    linesList (list of str): List of line names to filter the results.
    pushoverKeys (dict): Dictionary containing Pushover API keys.

    Sends a notification with train times on weekdays.
    """


    # Check if today is a weekday (Monday=0, Sunday=6)
    if datetime.now().weekday() < 7:
        # Initialize message in case no trains are found
        message = "Couldn't find any trains"
        for _ in range(3):  # Try function 3 times if it couldn't find any trains
            trains = scrape_tfl(stationURL, dataPlatformID, linesList)
            if trains != ["Couldn't find any trains"]:
                message = '\n'.join(trains)
                break

        # Send notification via Pushover
        conn = http.client.HTTPSConnection("api.pushover.net:443")
        conn.request("POST", "/1/messages.json",
                     urllib.parse.urlencode({
                         "token": pushoverKeys['TOKEN'],
                         "user": pushoverKeys['USER_ID'],
                         "message": message,
                     }), {"Content-type": "application/x-www-form-urlencoded"})
        conn.getresponse()