# run.py
from api import create_app

app = create_app()

#if __name__ == '__main__':
#    app.run(debug=True)
if __name__ == '__main__':
    app.run(debug=True)  # Set debug to False in production