# TravelBuddy application
Travel Buddy is a travel app designed to connect like-minded travelers, allowing users to create profiles, share travel plans, and find companions with similar interests. It includes a feature for travel agents to offer personalized packages, benefiting both travelers and agents. The app aims to foster a community of travelers who can share experiences, tips, and expenses, making travel safer, more affordable, and enjoyable. Additionally, Travel Buddy employs edge computing to enhance performance, reliability, and security by processing data locally on users' devices. This technology ensures faster response times, reduced bandwidth usage, and better data privacy, making the app effective even in areas with poor connectivity. Overall, Travel Buddy seeks to revolutionize travel planning by offering a convenient, efficient, and secure platform for travelers.    

<img width="449" alt="image" src="https://github.com/shivam0296/travel-backend/assets/88713292/21dc9a0b-d6af-4ee9-b19d-36ece096bcc7">      

Edge computing is integrated into the architecture of Travel Buddy using MQTT (Message Queuing Telemetry Transport) on the client side. MQTT, a lightweight protocol ideal for devices with limited processing power and memory, facilitates communication between the user's device (such as a smartphone or tablet) and the server via a publish/subscribe messaging model. When a user interacts with the Travel Buddy app, their device sends data, including travel preferences, to the server through MQTT messages. The server processes this data and sends back relevant information, such as recommended itineraries and nearby attractions, to the user's device. This integration allows Travel Buddy to leverage edge computing, enabling data processing to occur closer to the source on the user's device, which results in faster response times, reduced latency, and an overall improved user experience.



<img width="437" alt="image" src="https://github.com/shivam0296/travel-backend/assets/88713292/5a973aa0-d42b-40ec-99e6-d035bf279bf7">



The Travel Buddy website operates on a technology stack consisting of React for front-end development, Python with Flask for back-end development, MySQL for database management, and MQTT for connecting nearby users. The MQTT protocol, designed for low-bandwidth and unreliable networks, facilitates communication between publishers (devices or applications generating messages), brokers (central hub for routing messages), and subscribers (devices or applications receiving messages). Publishers, such as users' devices, generate small messages containing data like travel preferences or updates. These messages are sent to the MQTT broker, which routes them to subscribers based on predefined topics. This architecture ensures efficient communication, particularly in low-power or intermittent network environments. Additionally, the website undergoes testing in Postman to enhance reliability. Overall, users interact with the website by inputting travel preferences, which are transmitted via MQTT to the broker and processed by the Python-Flask backend. The backend retrieves relevant information from the MySQL database and delivers personalized recommendations or updates to users via the MQTT broker, creating a seamless and efficient travel planning experience.


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
