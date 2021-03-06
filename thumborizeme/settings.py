import os

# REDIS
REDIS_HOST = os.environ.get('REDIS_HOST', '127.0.0.1')
REDIS_PORT = os.environ.get('REDIS_PORT', 6379)
REDIS_PASSWORD = os.environ.get('REDIS_PASSWORD', '')

HOST = os.environ.get('HOST', 'http://localhost:9000')
THUMBOR_HOST = os.environ.get('THUMBOR_HOST', 'http://localhost:8001')

# PROXY
PROXY_HOST = os.environ.get('PROXY_HOST', '')
PROXY_HOST_HTTPS = os.environ.get('PROXY_HOST_HTTPS', '')
PROXY_PORT = os.environ.get('PROXY_PORT', 0)
