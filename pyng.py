# https://gist.github.com/josephl/65a0ff5bee4a7adf8300163be3618bb9

from argparse import ArgumentParser
from datetime import datetime
import logging
import re
import subprocess
from sys import argv



thresh = 100.
ptn = r'^.*time=([0-9.]+) ms$'

if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('-H', '--host', required=True, help='Host to ping')
    parser.add_argument('-f', '--file', help='Log output file')
    args = parser.parse_args()

    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    formatter = logging.Formatter(
        '%(asctime)s - %(levelname)s - %(message)s')
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.DEBUG)
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)
    if args.file:
        file_handler = logging.FileHandler(filename=args.file, mode='a')
        file_handler.setLevel(logging.WARNING)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    try:
        proc = subprocess.Popen(['ping', args.host], stdout=subprocess.PIPE)

        # Chuck the header
        proc.stdout.readline()
        while not proc.poll():
            line = proc.stdout.readline()
            match = re.match(ptn, line)
            if match:
                resp_time = float(match.group(1))
                if resp_time > thresh:
                    logger.warn(resp_time)
                else:
                    logger.info(resp_time)
            else:
                logger.error('dropped ping')
    except KeyboardInterrupt:
        if proc.poll():
            proc.terminate()