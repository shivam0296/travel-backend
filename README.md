# TravelBuddy application
This repository contains the code for the backend of our travel-app.

What is a Travel Buddy? How does it work and what are its benefits?

Travel Buddy is a one-stop solution for travelers who want to explore new destinations with
like-minded people. With the rise of solo travel, the app provides a platform for travelers to
connect with others and create meaningful connections while exploring new places. The app
allows users to create a profile, post their travel plans, and search for other users with similar
interests.

The app's travel agent feature provides an opportunity for travel agents to connect with
travelers and offer personalized travel packages based on their preferences. This feature not
only benefits travelers by providing them with tailored travel options but also benefits travel
agents by giving them access to a wider customer base.

Travel Buddy is a convenient and efficient way for travelers to connect with each other, plan
their trips, and create meaningful connections. With its unique features and user-friendly
interface, the app has the potential to revolutionize the way people travel and explore new
destinations.

To start using the app, users need to create a profile and fill in their travel details, such as the
starting location, destination, and preferred travel dates. Once users have created their profile
and posted their travel plans, other users who are interested in the same destination can
connect with them through the app. This connection provides an opportunity for users to get
to know each other and decide if they want to plan the trip together. The app provides users
with the flexibility to plan the trip according to their preferences, making it easier to
personalize the trip and ensure that everyone's interests are accommodated.

One of the key benefits of the app is the opportunity to connect with like-minded people who
share similar travel interests. This creates a community of travelers who can share tips,
recommendations, and experiences, and foster meaningful connections.

Another benefit of Travel Buddy is the opportunity to save money by sharing travel expenses
with a travel companion. This is especially useful for solo travelers, who can split costs such
as accommodation, transportation, and food with a partner. By sharing expenses, travelers
can stretch their budgets further and potentially afford to do more activities or stay in nicer
accommodations.

Traveling alone can be daunting and risky, especially for first-time travelers or in unfamiliar
3
destinations. Travel Buddy reduces the risk of traveling alone by allowing users to find travel
partners to explore new destinations with. This not only makes traveling safer but also more
enjoyable and fun, as users can share the experience with someone else.

Lastly, Travel Buddy offers a chance to create new friendships and build meaningful
connections with other travelers. By sharing travel experiences and exploring new
destinations together, users can form lasting friendships that extend beyond the trip itself.
This can lead to future travel opportunities and a sense of community with other travelers.

What is edge computing and how is it used in Travel Buddy?

Edge computing is a distributed computing model that aims to reduce latency and improve
the performance of applications by bringing computation and data storage closer to the edge
of the network, where the data is being generated. This means that the data is processed and
analyzed locally on devices, such as smartphones or IoT devices, rather than being
transmitted to a centralized cloud for processing.

In Travel Buddy, edge computing plays a vital role in providing efficient and personalized
travel recommendations to users. The app uses edge computing to process and analyze data
locally on the user's device, rather than transmitting it to a remote server for processing. This
results in faster response times, reduced bandwidth usage, and improved overall user
experience.

Edge computing in Travel Buddy also enhances data privacy and security. Since the data is
processed locally on the user's device, sensitive data is not transmitted to a remote server,
reducing the risk of data breaches.

The use of edge computing in Travel Buddy is especially beneficial for users who are on the
go, as it reduces the reliance on stable and consistent network connections. This makes the
app more reliable and ensures that users can access personalized travel recommendations
even in areas with poor network connectivity.
4
What are the advantages of using edge computing for Travel Buddy?

The advantages of using edge computing for Travel Buddy include:
• Improved performance: Edge computing reduces latency and improves the app's
responsiveness, providing a smoother and more enjoyable user experience.

• Increased reliability: Edge computing ensures that the app can continue to function
even in areas with limited or no internet connectivity, improving its reliability and
availability.

• Enhanced security: Edge computing keeps the user's data private and secure on their
device, reducing the risk of data breaches or unauthorized access.

• Lower costs: Edge computing reduces the need for expensive server infrastructure,
lowering the app's operational costs.

Overall, edge computing is a powerful technology that can enhance the performance,
reliability, and security of Travel Buddy, providing a better experience for travelers and
making trip planning more efficient      

<img width="449" alt="image" src="https://github.com/shivam0296/travel-backend/assets/88713292/21dc9a0b-d6af-4ee9-b19d-36ece096bcc7">      

Explain how edge computing is integrated into the architecture?

Edge computing is integrated into the architecture of Travel Buddy through the use of MQTT
(Message Queuing Telemetry Transport) on the client side. MQTT is a lightweight protocol
that is designed for IoT (Internet of Things) devices with limited processing power and
memory. It allows the client to communicate with the server through a publish/subscribe
messaging model.

In the case of Travel Buddy, the client is the user's device, such as a smartphone or tablet.
When the user interacts with the Travel Buddy application, their device sends data to the
server through MQTT messages. This data can include the user's preferences for their trip,
such as the destination, activities, and budget.

The server processes this data and sends back relevant information to the user's device, such
as recommended travel itineraries and nearby attractions. This communication between the
client and server is made possible by the edge computing capabilities provided by MQTT.
By using edge computing, Travel Buddy is able to provide faster response times and reduce
latency. This is because the processing of data happens closer to the source, on the user's
device, rather than on a centralized server. This allows for a more efficient and effective use
of resources and improves the overall user experience.

In summary, MQTT enables the integration of edge computing into Travel Buddy's
architecture by allowing for efficient communication between the client and server, resulting
in faster response times and improved user experience 



<img width="437" alt="image" src="https://github.com/shivam0296/travel-backend/assets/88713292/5a973aa0-d42b-40ec-99e6-d035bf279bf7">



MQTT (Message Queuing Telemetry Transport) is a publish-subscribe messaging protocol
designed for low-bandwidth, high-latency, and unreliable networks. Its architecture consists of
three main components: publishers, brokers, and subscribers.

Publishers are devices or applications that generate messages and publish them to an MQTT
broker. These messages are typically small and contain data such as sensor readings, device
status updates, or control commands.

The MQTT broker is the central hub of the architecture. It receives messages from publishers
and routes them to subscribers based on predefined topics. The broker is responsible for
maintaining a list of subscribed clients and delivering messages to them. It also provides
various services such as message persistence, security, and quality of service (QoS) control.
Subscribers are devices or applications that receive messages from the MQTT broker.
Subscribers subscribe to specific topics and receive messages that are published to those topics.
The messages can be used to trigger actions or update the state of the subscriber.

In summary, the architecture of MQTT involves publishers sending messages to the MQTT
broker, which then routes those messages to subscribers based on predefined topics. This
design allows for a scalable and efficient communication system that is well-suited for lowpower, low-bandwidth, and intermittent network connections.

Technology Stack:

• React : For front-end development of the project.

• Python + Flask : For back-end development.

• MySQL : Database to store users' information.

• MQTT Search : To connect nearby users.

• Testing in postman : To make the application more reliable.
How does the Website Work:


 <img width="502" alt="image" src="https://github.com/shivam0296/travel-backend/assets/88713292/ab5acd64-fefc-4294-8fbc-a20c8fac0fe6">
 <img width="566" alt="image" src="https://github.com/shivam0296/travel-backend/assets/88713292/4705c16d-9023-4b27-b518-de37dc8e154b">
<img width="495" alt="image" src="https://github.com/shivam0296/travel-backend/assets/88713292/f44f8aec-3c0f-45e4-8d48-56600fe17bcd">
<img width="496" alt="image" src="https://github.com/shivam0296/travel-backend/assets/88713292/3d525db7-f7cd-45dd-b655-6b9db6ecb306">

GitHub Link to access the code:
• Backend app: https://github.com/shivam0296/travel-backend
• Frontend app: https://github.com/shivam0296/travel-app  

References:
• http://www.steves-internet-guide.com/mqtt/
• https://pypi.org/project/paho-mqtt/
• https://react.dev
• https://www.php.net
