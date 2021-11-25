import logging

logging.basicConfig(filename='log.log', level=logging.INFO,
                    format='%(levelname)s:%(module)s:%(message)s')
logging.info('Program Started')

try:
    import mod_terminalUI as cmdUI
except ImportError as IE:
    logging.critical(f'Import Failure: {IE}')
    exit()


def main():
    pass


if __name__ == '__main__':
    main()
