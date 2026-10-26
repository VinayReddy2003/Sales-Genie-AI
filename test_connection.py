from sqlalchemy import create_engine
from sqlalchemy.engine import URL

url_object = URL.create(
    "postgresql+psycopg",
    username="postgres",
    password="admin123",
    host="localhost",
    port=5432,
    database="salesgenie",
)

try:
    engine = create_engine(url_object)
    connection = engine.connect()
    print("✅ Database connected successfully!")
    connection.close()
except Exception as e:
    print(f"❌ Connection failed: {e}")
