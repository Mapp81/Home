from app import create_app
from models import db

app = create_app()

with app.app_context():
    db.create_all()  # 🧙 Esto crea la tabla "post" automáticamente
    print("✅ Tabla 'post' creada en blog.db")