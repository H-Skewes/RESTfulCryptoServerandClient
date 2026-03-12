--Task 1 complete--


---Task 2 inprogress---
--currently completed or working on--

Mac client server connection Done 3/11/2026
Fake sever HMAC verification testing Done 3/11 2026



File writeups

Client

Requests weather data from the basic server.

Server

Basic weather app api/server that returns weather data when requested.

Mac Server

This file makes a accepts requests to the mac server and creates a tag to be verified.

Mac Client

This file makes a request to the mac server and verifies the tag against the pre shared key hmac hash.

Fake Server

The fake server is to basically mimic if an attacker was on wireshark while hosting a non TLS secured
server, and having the attacker steal the key to try and verify eachother through the connection. In this 
instance the key is from the tag file, but it could be easily moved.



Generate Hex Key

Generates a 256 bit hex key for the .env file to be used in cryptographic operations.

