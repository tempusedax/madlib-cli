import re

print("Welcome to Madlib")


def read_template (path):
    file = open(path, "r")
    # except FileNotFoundError:
    # raise FileNotFoundError("Cannot find {}.".format(PATH_OF_FILE))
    read = file.read()
    file.close()
    return read.strip()


def parse_template(template: str):

    parse = re.findall(r'\{(.*?)\}', template)

    for word in parse:

        template = template.replace((word), '')

    return template, tuple(parse)


def merge(string, tup):
    return string.format(*tup)
