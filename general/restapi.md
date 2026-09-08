## What is a REST API?
REST API stands for Representational State Transfer Application Programming Interface. 

It is an architectural style that allows different software applications to communicate with each other over the internet. 

It acts as a standardized translator, enabling a client (like a mobile app or web browser) to request data or actions from a server.

REST APIs typically use the HTTP protocol—the same technology used to load websites. They map standard HTTP methods to CRUD database operations:

| HTTP Method | Action | Example Endpoint | Real-World Result |
| --- | --- | --- | --- | 
| `GET` | Read / Retrieve data | /v1/products | Fetches a list of all products.
| `POST` | Create new data | /v1/products | Adds a brand new product to the database. |
| `PUT / PATCH` | Update existing data | /v1/products/123 | Modifies the details of product ID 123. |
| `DELETE` | Delete data | /v1/products/123 | Removes product ID 123 from the system.

## The Core Principles of REST
For an API to be considered truly "RESTful," it must adhere to specific rules outlined by computer scientist Roy Fielding in 2000: 
* Statelessness: The server does not store any information about past requests. Every single request from the client must contain all the data and authentication keys needed to complete it. 
* Client-Server Separation: The front-end (client) and back-end (server) are completely independent. You can completely rebuild your website's UI without having to change how the database stores data.
* Uniform Interface: Resources must be organized logically using uniform resource identifiers (URIs) named with nouns rather than verbs (e.g., /products instead of /get-all-products). 
* Cacheability: Server responses must explicitly state whether the data can be cached by the client. This prevents the client from repeatedly requesting data that rarely changes (like a company logo), speeding up performance. 

## The Request and Response Cycle
* The Request: The client sends an HTTP request to a specific URL (called an endpoint). This request contains the HTTP method, headers (metadata/auth tokens), and an optional payload (data, usually formatted in JSON). 
* The Response: The server processes the request and sends back a response payload (typically JSON) alongside an HTTP Status Code.
    * 200 OK: The request succeeded.
    * 201 Created: A new resource was successfully added.
    * 404 Not Found: The requested resource doesn't exist.
    * 500 Internal Server Error: Something broke on the server side.