from app.app import app
WSGI_APPLICATION = 'nippopo.wsgi.application'

if __name__ == "__main__":
    app.run()
