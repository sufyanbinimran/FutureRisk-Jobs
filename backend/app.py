from flask import Flask
from flask_cors import CORS
from models import db
from routes import api
from config import Config
import os
from dotenv import load_dotenv
load_dotenv()


app = Flask(__name__)
app.config.from_object(Config)

# Initialize extensions
CORS(app)
db.init_app(app)

# Register blueprints
app.register_blueprint(api, url_prefix='/api')

# Create database tables safely
with app.app_context():
    try:
        print("📦 SQLAlchemy Engine:", db.engine.url)  # 👈 move this up
        db.create_all()
        print("✅ Tables created.")
    except Exception as e:
        print("❌ Error creating tables:", e)



print("🚨 DATABASE URI:", os.getenv("DATABASE_URL"))

if __name__ == '__main__':
    app.run(debug=True)
