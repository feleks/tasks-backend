import os

if __name__ == '__main__':
    host = os.getenv('HTTP_SERVER_HOST')
    port = os.environ.get('HTTP_SERVER_PORT')

    print('Should start server on {}:{}'.format(host, port))
