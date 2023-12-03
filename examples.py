"""
This script demonstrates how to use the main module to run specific TfL station queries.

It accepts a command-line argument to select which pre-defined example to run. 
The examples showcase different station URLs and parameters for scraping train times.

Usage:
    python examples.py <example_number>

Arguments:
    example_number: An integer (1 or 2) specifying which example to run.
"""

import sys
import configparser
from src.main import main

def run_example():
    """
    Main function to execute the script based on command line arguments.
    """
    config = configparser.ConfigParser()
    config.read('config.ini')

    try:
        example_number = int(sys.argv[1])  # Takes the example number as a command-line argument
    except IndexError:
        print("Error: No example number provided. Please run the script with an example number (1 or 2).")
        sys.exit(1)
    except ValueError:
        print("Error: Invalid example number. Please provide a numeric value (1 or 2).")
        sys.exit(1)

    if example_number == 1:
        # Example 1: Cannon Street Underground Station, Westbound - Platform 1
        main('https://tfl.gov.uk/tube/stop/940GZZLUCST/cannon-street-underground-station/',
                    'Westbound - Platform 1', ['Circle'], config['Credentials'])
    elif example_number == 2:
        #Example 2: High Street Kensington Underground Station, Westbound - Platform 1
        main('https://tfl.gov.uk/tube/stop/940GZZLUHSK/high-street-kensington-underground-station/?Input=High+Street+Kensington+Underground+Station',
                    'Westbound - Platform 1', ['Circle'], config['Credentials'])
    else:
        print("Error: Invalid example number. Please provide a valid example number (1 or 2).")
        sys.exit(1)

if __name__ == "__main__":
    run_example()
