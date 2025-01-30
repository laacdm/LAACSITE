from mongoengine import Document, StringField, FileField

class Image(Document):
    image_id = StringField(primary_key=True, required=True)  # Now the primary key
    name = StringField(required=True)
    image = FileField()  # Stores PDFs using GridFS