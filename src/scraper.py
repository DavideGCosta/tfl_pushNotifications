import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta

def scrape_tfl(stationURL, dataPlatformID, linesList):
    """
    Scrapes train departure times from a given TfL station URL.

    Args:
    stationURL (str): The URL of the TfL station to scrape.
    dataPlatformID (str): The data-platform ID used to locate the correct departure information in the HTML.
    linesList (list of str): List of line names to filter the results.

    Returns:
    list of str: List of train departure times and expected times.
    """

    # Send a GET request to the station URL
    current_time = datetime.now()
    response = requests.get(stationURL)

    # Parse the HTML content of the page
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find the departure list using the data-platform ID
    departures_list = soup.find('div', {'data-platform-id': dataPlatformID})

    # Initialize a list to hold train information
    trains = []

    # Process each departure item if departures are found
    if departures_list:
        for item in departures_list.find_all('li', class_='live-board-feed-item'):
            line_name = item['data-line-name']
            eta = item.find('span', class_='live-board-eta').get_text(strip=True)

            # Convert 'Due' to 0 minutes or extract the number of minutes
            minutes_to_add = 0 if eta == 'Due' else int(eta.split()[0])
            
            # Calculate the expected time of the train
            expected_time = current_time + timedelta(minutes=minutes_to_add)

            # If the line is in the list of interest, add it to the trains list
            if line_name in linesList:
                trains.append(f'{line_name} - {eta} (Expected: {expected_time.strftime("%H:%M")})')
    else:
        trains = ["Couldn't find any trains"]

    return trains