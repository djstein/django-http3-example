# django-http3-example

Run the server:

```bash
poetry install
poetry shell
hypercorn --quic-bind localhost:8000 server.asgi:application --keyfile certs/ssl_key.pem --ca-cert certs/pycacerts.pem --certfile certs/ssl_cert.pem
```

in another terminal run a client:
The basic one:

```bash
python client.py --ca-certs certs/pycacerts.pem https://127.0.0.1:8000/
```

Or the httpx one:

```bash
python httpx_client.py --ca-certs certs/pycacerts.pem https://127.0.0.1:8000/
```

Clients taken from https://github.com/aiortc/aioquic and added logging of response data
