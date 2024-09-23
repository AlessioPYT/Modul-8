import mongoengine as me

# Connect to MongoDB Atlas
me.connect(db="quotes_db", host="your_connection_string")

class Author(me.Document):
    fullname = me.StringField(required=True)
    born_date = me.StringField(required=True)
    born_location = me.StringField(required=True)
    description = me.StringField()

class Quote(me.Document):
    tags = me.ListField(me.StringField())
    author = me.ReferenceField(Author, reverse_delete_rule=me.CASCADE)
    quote = me.StringField(required=True)


class Contact(me.Document):
    fullname = me.StringField(required=True)
    email = me.EmailField(required=True)
    message_sent = me.BooleanField(default=False)
    additional_info = me.StringField()

    def __str__(self):
        return f"{self.fullname} - {self.email}"
