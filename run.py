from src.main.configs import app
from src.infra.config import create_database

if __name__ == "__main__":
    create_database()
    app.run(debug=True, host="0.0.0.0", port=5000)
