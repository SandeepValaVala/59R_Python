import logging
logging.basicConfig(
    # level=logging.INFO
    level=logging.DEBUG,
    filename='app.log',
    format="%(asctime)s-%(levelname)s-%(message)s"
)
logging.debug('This block started execcution')
logging.info('Function execution completed')
logging.warning('Warning')
logging.error('Error')
logging.critical('Criticcal error')

import mysql.connector

try:
    conn = mysql.connector.connect()
except Exception as e:
    logging.warning(e)
else:
    logging.info('connection establishment done')

finally:
    if conn.is_connected()==True:
        conn.close()
    logging.info('DB connection closed')