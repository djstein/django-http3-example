# django-http3-example

```bash
poetry install
hypercorn --quic-bind localhost:8000 server.asgi:application --keyfile certs/ssl_key.pem --ca-cert certs/pycacerts.pem --certfile certs/ssl_cert.pem

python client.py --ca-certs certs/pycacerts.pem https://127.0.0.1:8000/
```
