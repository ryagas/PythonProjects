import argparse
import sys


class Greeting:
    """
    Created with a greeting text.
    Writes the text to stdout.

    :param text: The greeting text.
    :type text: str
    """

    def __init__(self, text):
        self.text = text

    def write(self):
        print(self.text)

    def read(self):
        return self.text


def main(opts=None):
    if opts is None:
        greeting = Greeting("Hello, World!")
    else:
        parser = argparse.ArgumentParser()
        parser.add_argument("--who", default="World", help="Who to greet.")
        args = parser.parse_args(opts[1:])
        greeting = Greeting(f"Hello, {args.who}!")

    greeting.write()


if __name__ == "__main__":
    main(opts=sys.argv)
