import pika
import json
from authors_and_quotes import Contact

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()


channel.queue_declare(queue='email_queue')

def send_email_stub(contact):
    """
    відправка email (заглушка).
    """
    print(f"Sending email to {contact.fullname} ({contact.email})...")
    print(f"Email sent to {contact.fullname}")

def callback(ch, method, properties, body):
    message = json.loads(body)
    contact_id = message['contact_id']
    
    
    contact = Contact.objects(id=contact_id).first()

    if contact and not contact.message_sent:
        send_email_stub(contact)
        
        contact.update(message_sent=True)
        print(f"[x] Contact {contact.fullname} updated as message sent.")
    
    
    ch.basic_ack(delivery_tag=method.delivery_tag)


channel.basic_consume(queue='email_queue', on_message_callback=callback, auto_ack=False)

print('[*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
