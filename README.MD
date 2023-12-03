# TFL Train Times Notifier
## Introduction
Are you a Londoner that takes TFL trains such as 'Circle' or 'District' that come at irregular times? Say no more! This TfL Train Times Notifier shows you an example of how to scrape the train time-table for yourstration and uses Pushover to send notifications straight to your phone. 

## Project Structure
Here's how we've organized the code:
- `src/`
  - `main.py`       - The heart of our project.
  - `scraper.py`    - The brain behind scraping TfL's site.
- `examples.py`     - Where we test our examples.
- `requirements.txt` - All the ingredients you need.
- `run_example1.bat` - A simple click to run our first example.
- `run_example2.bat` - Similarly, for our second example.


## Setup
Before you dive in, let's set things up:

1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/tfl-train-times-notifier.git
   cd tfl-train-times-notifier
   ```
2. **Create a Virtual Environment (Recommended)**
   ```bash
    python -m venv venv
3. **Activate the Virtual Environment**
   - On Windows: ```venv\Scripts\activate```
    - On Unix/MacOS: ```source venv/bin/activate```
4. **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```
5. **Configuration**
    - Rename ```config-sample.ini``` to ```config.ini```.
    - Fill in the necessary details like your [Pushover API keys](https://support.pushover.net/i175-how-to-get-a-pushover-api-or-pushover-application-token).
    - Install the [Pushover App](https://pushover.net/) on your phone and log in with your details.

6. **How to Use**
    - **Running Examples** (These scripts will activate your environment, run the example, and then deactivate it).
        - Example 1: To run the first example, just double-click ```run_example1.bat```.
        - Example 2: Similarly, double-click ```run_example2.bat```.
    - **Scheduling with Windows Task Scheduler**:
        - Open Task Scheduler and create a new task.
        - Set the trigger to the time you want (like 6 PM for homebound trains).
        - For the action, select "Start a program" and choose run_example1.bat or run_example2.bat.
        - Save and enable the task. Voilà!

## Contributing
Love this project? Great! We're open to contributions:
- Fork the repo.
- Make your changes.
- Submit a pull request.

## License
This project is licensed under MIT License. Feel free to use it as you like!