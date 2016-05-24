import multiprocessing

bind = "unix:/tmp/gunicorn.sock "
workers = multiprocessing.cpu_count()

accesslog = '/tmp/gunicorn_access.log'
errorlog = '/tmp/gunicorn_error.log'

raw_env = ['PRODUCTION=True', 'DEBUG=True']
