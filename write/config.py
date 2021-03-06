import os
from configparser import ConfigParser


def conn_params(filename='database.ini', section='localhost'):
    # create a parser
    parser = ConfigParser()
    # read config file
    parser.read(os.path.join(os.path.dirname(__file__), filename))

    # get section, default to localhost
    if parser.has_section(section):
        params = {param[0]: param[1] for param in parser.items(section)}
    else:
        raise Exception('Section {0} not found in the {1} file'.format(section, filename))

    return params
