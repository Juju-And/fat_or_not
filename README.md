# Are you FAT OR NOT?

This is a simple Python application intended to calculate Body mass index (BMI) is a measure of body fat based on height and weight that applies to adult men and women.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

Install all required modules running pip with the provided file:

```
pip install -r requirements.txt
```

### Installing

As a first step upgrade SQLite database, by:
```
$ flask db upgrade
```

In order to run the application the command should be typed:

```
$ python3 main.py
```

in console will be shown the link to localhost address.

All interaction happens in the browser. User can add weight and height, application will count BMI, and add to the database.
List of records would include only 10 last results and count it's average.