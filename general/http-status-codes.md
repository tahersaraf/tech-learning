## HTTP Status Codes
HTTP status codes are three-digit standard responses issued by a web server to inform a client (such as a browser or API) of the outcome of their request. They are divided into five primary classes:
* 1xx – Informational: The server has received the request and is continuing the process.
* 2xx – Success: The request was successfully received, understood, and processed.
* 3xx – Redirection: Further action is needed (like visiting a different URL) to complete the request.
* 4xx – Client Error: The request contains bad syntax or cannot be fulfilled due to a client-side issue.
* 5xx – Server Error: The server failed to fulfill a valid request due to an internal error.


### 1xx: Informational Responses

* 100 Continue: The initial part of the request was received; the client should continue with the rest of the request.
* 101 Switching Protocols: The server is complying with a client request to switch protocols (e.g., upgrading to WebSockets).
* 103 Early Hints: Used to return some response headers before final HTTP message.


### 2xx: Success Responses

* 200 OK: The request succeeded, and the requested data is returned in the body.
* 201 Created: The request succeeded, and a new resource was created.
* 202 Accepted: The request has been accepted for processing, but processing is not yet complete.
* 204 No Content: The request succeeded, but there is no payload/response body to return (common for DELETE or PUT).
* 206 Partial Content: The server is delivering only a portion of the resource due to a range header sent by the client.

### 3xx: Redirection Responses

* 301 Moved Permanently: The target resource has been assigned a new permanent URI.
* 302 Found: The resource resides temporarily under a different URI (temporary redirect).
* 304 Not Modified: The cached version of the resource is still fresh and can be used.
* 307 Temporary Redirect: The target resides temporarily under a different URI, and the client must not change the HTTP method used.
* 308 Permanent Redirect: The resource is permanently at a new URI, and the client must keep the same HTTP method.

### 4xx: Client Error Responses

* 400 Bad Request: The server cannot process the request due to malformed syntax or invalid data.
* 401 Unauthorized: Authentication is required and has failed or has not been provided.
* 403 Forbidden: The server understood the request, but refuses to authorize it.
* 404 Not Found: The requested resource could not be found on the server.
* 405 Method Not Allowed: The HTTP method used is not supported for this resource.
* 408 Request Timeout: The server timed out waiting for the request from the client.
* 409 Conflict: The request could not be completed due to a conflict with the current state of the resource (e.g., duplicate entry).
* 410 Gone: The requested resource is permanently deleted and will not be available again.
* 413 Payload Too Large: The request is larger than the server is willing or able to process.
* 415 Unsupported Media Type: The media format of the requested data is not supported by the server.
* 422 Unprocessable Entity: The request was well-formed (valid syntax) but contained semantic errors.
* 429 Too Many Requests: The client has sent too many requests in a given amount of time (rate limiting).

### 5xx: Server Error Responses

* 500 Internal Server Error: A generic error message when the server encounters an unexpected condition.
* 501 Not Implemented: The server does not support the functionality required to fulfill the request.
* 502 Bad Gateway: The server, while acting as a gateway or proxy, received an invalid response from an upstream server.
* 503 Service Unavailable: The server is temporarily unable to handle the request (due to overload or maintenance).
* 504 Gateway Timeout: The gateway server did not receive a timely response from an upstream server.
* 505 HTTP Version Not Supported: The server does not support the HTTP protocol version used in the request.
* 511 Network Authentication Required: The client needs to authenticate to gain network access.