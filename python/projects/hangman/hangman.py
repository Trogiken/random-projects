import logging

logging.basicConfig(filename='log.log', level=logging.INFO,
                    format='%(levelname)s:%(module)s:%(message)s')
logging.info('Program Started')

try:
    from assets import print_red_on_cyan
except ImportError as IE:
    logging.critical(f'Import Failure: {IE}')
    exit()


def main():
    print("Blank Space NORM")
    print_red_on_cyan("Green")


if __name__ == '__main__':
    main()
