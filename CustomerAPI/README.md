

# An example Django CRUD operation application

Install and run:

# Move to previous folder
cd ..
# Create environment and run below commands
python -m venv env
pip install -r requirements.txt
cd env
cd scripts
activate
# Move to Customer API folder
cd ..
cd ..
cd CustomerAPI
manage.py runserver



Open `http://127.0.0.1:8000/` in your browser:

Navigate to path that is not routed, eg `http://127.0.0.1:8000/nope`:


Raise a server error by navigating to `http://127.0.0.1:8000/error`:


