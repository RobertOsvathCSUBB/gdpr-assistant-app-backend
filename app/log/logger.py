import logging

logging.basicConfig(
    filename='app.log',
    filemode='w',  # 'w' to overwrite the file each time, 'a' to append
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

logger = logging.getLogger(__name__)
logger.info('Logger initialized')
