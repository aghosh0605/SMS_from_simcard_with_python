from ipaddress import IPv4Address  # for your IP address

from pyairmore.request import AirmoreSession  # to create an AirmoreSession

from pyairmore.services.messaging import MessagingService  # to send messages




print("Setup your Airmore ap with the code")
ipadd1=str(input("Enter ip address mentioned on the Airomre app: "))
ip = IPv4Address(ipadd1)  # let's create an IP address object# now create a session
port1=int(input("Enter the port-number mentioned on the Airomre app: "))

#session = AirmoreSession(ip)# if your port is not 2333

session = AirmoreSession(ip, port1)  # assuming it is 2333





session.is_server_running  # True if Airmore is running



was_accepted = session.request_authorization()



print(was_accepted)  # True if accepted





#inputs to send sms

mobile_number=str(input("Enter the mobile number to send message: "))

message_content=str(input("Enter the content to send: "))





#starting sms



service = MessagingService(session)

service.send_message(mobile_number, message_content)
