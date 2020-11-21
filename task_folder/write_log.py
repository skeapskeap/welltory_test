from logging import handlers
import logging

handler = logging.FileHandler(filename='json_schema_validation.txt')
formatter = logging.Formatter('')
handler.setFormatter(formatter)
logging.basicConfig(level=logging.INFO, handlers=[handler])
logger = logging.getLogger()