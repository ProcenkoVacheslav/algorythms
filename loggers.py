import logging

from pathlib import Path

DECORATORS_DIR = Path(__file__).parent
PROJECT_ROOT = DECORATORS_DIR.parent
LOGS_DIR = DECORATORS_DIR / 'logs'
LOG_FILE = LOGS_DIR / 'algorythms_logs.log'

# ALGORYTHMS

algorythm_logger = logging.getLogger('algorythms')
algorythm_logger.setLevel(logging.DEBUG)

algorythm_consol_handler = logging.StreamHandler()
algorythm_file_handler = logging.FileHandler(LOG_FILE)

algorythm_formatter = logging.Formatter(
    fmt='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)


algorythm_consol_handler.setFormatter(algorythm_formatter)
algorythm_file_handler.setFormatter(algorythm_formatter)

algorythm_logger.addHandler(algorythm_consol_handler)
algorythm_logger.addHandler(algorythm_file_handler)
