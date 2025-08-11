from mongoengine import connect

connect(
    db="notes_db",
    host="mongodb://localhost:27017/notes_db"
)

