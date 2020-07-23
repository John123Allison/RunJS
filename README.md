# RunJS
Prototype run tracking app.

# Setup
Clone the repository, and in the top level, use `export FLASK_APP=runjs.py` and `export FLASK_ENV=development` and `SECRET_KEY=<key>` to set up the required environment variables. Then, use run `flask db migrate` and `flask db upgrade` to create the local dev database (sqlite). Finally, run `flask run` to run the development server.

Make sure you have pip installed and have the virtual environment activated with `source venv/bin/activate` before starting work.
