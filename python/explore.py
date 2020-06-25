from twilio.rest import Client

client = Client('xxxxxxxxxx', 'xxxxxxxxxxx')

# list messages
for msg in client.messages.list():
    print(msg.body)

# delete messages
# for msg in client.messages.list():
# 	print(f"Deleting {msg.body}")
# 	msg.delete()


# create messages
# msg = client.messages.create(
# 		to='xxxxxxxx',
# 		from_='xxxxxxxx',
# 		body='Hello from python!'
# 	)

# print(f'created a message: {msg.sid}')
