This is a work-in-progress port of https://github.com/brandomr/document_cluster to a
more standard python format.

Uses virtual env.  Mini-tutorial:

# Create your virtual environment and install libs (just once).
virtualenv venv --distribute
pip install -r requirements.txt

# Activate your virtual env (whenever you work on the project).
source venv/bin/activate

# Deactivate your virtual env (whenever you want to stop working on the project).
deactivate

------

The original code is in original.py.  My modified version is in cluster.py.

I'm adding unit tests in the tests directory.  You can run these using py.test like so:

py.test tests/*.py
