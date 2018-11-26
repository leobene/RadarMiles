# RadarMiles
A simple **REST** API using Flask

## API 

From the API we can:

1. Look up flights


## Setting up the application
To download and start the application issue the following commands.
First clone the application code into any directory on your disk:

$ cd /path/to/my/workspace/

$ git clone https://github.com/leobene/RadarMiles

$ cd RadarMiles

Create a virtual Python environment in a directory named venv, activate the virtualenv and install required dependencies using pip:

$ virtualenv -p python3 venv

$ source venv/bin/activate

(venv) $ pip install -r requirements.txt

Now let’s start the app:

(venv) $ python app.py

OK, everything should be ready. In your browser, open the URL http://127.0.0.1:5000/

## Testing the application

To run the unit, integration or system tests just folow the example above:

$python -m unittest tests/system/user_test.py

