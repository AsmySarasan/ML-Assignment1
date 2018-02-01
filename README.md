## Machine Learning Assignment - 1

### Scraping using Python

> Author - Asmy Sarasan, 100462413

This is a scraping tool built using Python 3.6.3 that would give you the details of FIFA 2018 rounds and game dates.

To get the details, clone this repo to your local drive, activate the virtual environment by unzipping the
_venv.zip_ folder and then running the following command from the location where it has been unzipped:

> source venv/bin/activate

and then running:

> pip install -r requirements.txt

to install the requirements to run this program in your local drive. 

You can then run the program by running the command:

> python Scrape.py

On your terminal, you will be able to see the details of the **First stage** of FIFA 2018 with the dates, teams playing and the times of the games.  As the FIFA tournament progresses to second stage, the terminal will display details of next stage along with irst stage. A CSV file named `FIFA.csv` will also be created that stores the dates of all the games for each stage.
