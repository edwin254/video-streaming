# Run a test server.
from app import app

if __name__ == "__main__":
    print("MAIN")
    app.run(host='0.0.0.0', port=8080, debug=True)