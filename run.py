from app import app
from app.database import create_tables

create_tables()
app.run(debug=True)