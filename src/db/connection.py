import psycopg2

def create_connection(config):
    return psycopg2.connect(**config)
