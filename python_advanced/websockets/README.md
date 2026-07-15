# Real-time Communication with WebSockets

## Description

This project focuses on building a real-time communication system using **WebSockets**.

Traditional HTTP communication follows a **request-response** model: the client sends a request and the server sends back a response. This approach is not ideal for applications requiring continuous updates, such as chat applications, live dashboards, or collaborative tools.

WebSockets solve this limitation by creating a **persistent connection** between the client and the server. Once the connection is established, both sides can exchange messages at any time without creating a new connection for each interaction.

The goal of this project is to implement a real-time communication system using:

* WebSocket protocol
* Asynchronous programming with Python
* Multiple concurrent client connections
* Real-time message exchange

---

## Learning Objectives

By completing this project, you will learn how to:

* Create a WebSocket server using Python.
* Use asynchronous programming with `async` / `await`.
* Handle multiple clients connected at the same time.
* Send and receive messages in real time.
* Implement different communication patterns.
* Validate and respect message formats.
* Build the foundation of real-time applications.

---

## Project Features

The project is progressively implemented through several steps:

### 1. WebSocket Server

Create a server capable of:

* Accepting WebSocket connections.
* Keeping connections open.
* Receiving messages from clients.
* Sending responses in real time.

### 2. WebSocket Clients

Create clients that can:

* Connect to the server.
* Send messages.
* Receive messages from the server.

### 3. Multiple Participants

Support communication between multiple connected clients:

* Track active connections.
* Handle simultaneous users.
* Broadcast or route messages when required.

### 4. Message Routing and Validation

Implement:

* Message handling logic.
* Validation of received data.
* Respect of predefined communication formats.

### 5. Web Client Integration

Connect the WebSocket system with a browser-based client to demonstrate real-time communication.

---

## Technologies Used

* Python 3
* `websockets` library
* `asyncio`
* WebSocket protocol
* HTML / JavaScript (for web client integration)

---

## Requirements

### Python Files

All Python files must:

* Start with:

```python
#!/usr/bin/env python3
```

* End with a new line.
* Follow **PEP 8** style guidelines.

---

### Programming Requirements

The implementation must use:

* The `websockets` Python library.
* Asynchronous programming (`async` / `await`).

The application must:

* Maintain persistent connections.
* Handle continuous communication correctly.
* Support multiple concurrent connections when required.
* Follow the expected behavior exactly.

---

## Important Rules

Do not:

* Add unnecessary frameworks.
* Modify the communication protocol.
* Add features that are not requested.
* Change the expected message format.

Message formats must be respected exactly when specified.

Small differences in behavior may cause automated evaluations to fail.

---

## How WebSockets Work

### HTTP Communication

Traditional HTTP:

```
Client  ---- Request ---->  Server
Client  <--- Response ----  Server
```

The client always starts the communication.

---

### WebSocket Communication

WebSocket:

```
Client  <================>  Server

        Persistent connection

Client  ---- Message ----> Server
Client  <--- Message ----- Server
```

Both sides can communicate at any time.

---

## Asynchronous Programming

This project uses Python's `asyncio` to manage multiple connections efficiently.

Example:

```python
async def handler(websocket):
    async for message in websocket:
        print(message)
```

The server can wait for messages without blocking other connected clients.


---

## Author

Project made by Rawan for Holberton school-Real-time communication with WebSockets project
