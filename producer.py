import pika
import json
from faker import Faker
from authors_and_quotes import Contact  


connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='email_queue')

fake = Faker()

def create_contacts(n):
    for _ in range(n):
        contact = Contact(
            fullname=fake.name(),
            email=fake.email(),
            additional_info=fake.text()
        )
        contact.save()
    
        message = {'contact_id': str(contact.id)}
        channel.basic_publish(exchange='', routing_key='email_queue', body=json.dumps(message))
        print(f"[x] Sent contact: {contact.fullname} - {contact.email}")

if __name__ == "__main__":
    number_of_contacts = int(input("Enter number of contacts to create: "))
    create_contacts(number_of_contacts)

    connection.close()
