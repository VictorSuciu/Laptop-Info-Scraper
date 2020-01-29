# Laptop Info Scraper

[**Download Here**](https://github.com/VictorSuciu/README-Assets/tree/master/Laptop_Status)

## Description

This program scrapes laptop due dates from Alma and outputs them in a concise list to the terminal. Additionally, it notifies the employee of any due dates that are still at `23:59:00`. Tech desk employees have to manually click on each laptop in Alma to verify green-sheet due dates, so this program saves minutes of tedious clicking. 

## User Instructions

1. [Download](https://github.com/VictorSuciu/README-Assets/tree/master/Laptop_Status) the application folder and unzip it.

2. Run Laptop_Status.exe by double clicking on it.

3. The program will begin running it's own Chrome instance and open the Alma login page.

4. Enter your UW NetID Credentials.

5. The program will begin rapidly navigating Alma and will output laptop info to the terminal.

## Development Dependencies

* Python 2.7 or 3.4+

* Chromedriver Excutable

* Selenium for Python

## Development Installation

1. Install [Selenium](https://pypi.org/project/selenium/) Python package: `pip install selenium`

2. Download the correct [chromedriver](https://chromedriver.chromium.org/downloads) executable for your operating system and version of Chrome.

3. Download `Laptop_Status.py` from this repository.

4. Place `Laptop_Status.py` in a folder.

5. Create another folder next to `Laptop_Status.py` called `driver` an place the chromedriver executable inside.

The project directories should look like this:

```
project/
|
|-- Laptop_Status.py
|-- driver/
    |
    |-- chromedriver.exe
```

## Sample Output

**Note:** The following information is completely fake, and was made up by me. None of the due dates or times reflect real information in the Alma system. This section is meant to showcase the format in which real information would be presented.

```
1:  13/16/2015 |  6:00 PM
2:  13/21/2015 | 11:59 PM <-- Change Due Date
3:  13/05/2015 |  6:00 PM
4:  13/04/2015 | 10:30 PM
5:  IN
6:  IN
7:  13/15/2015 | 10:30 PM
8:  13/14/2015 |  6:00 PM
9:  13/23/2015 | 11:59 PM <-- Change Due Date
10: 13/17/2015 |  6:00 PM
11: 13/22/2015 | 10:30 PM
12: IN
13: 13/12/2015 | 10:30 PM
14: 13/17/2015 |  6:00 PM
15: 13/02/2015 |  6:00 PM
16: 13/10/2015 | 10:30 PM
17: IN
18: 13/24/2015 |  6:00 PM
19: 13/19/2015 | 10:30 PM
20: IN
21: IN
22: 13/18/2015 |  6:00 PM
23: 13/14/2015 | 10:30 PM
24: IN
25: IN
```