import argparse
import random

entries = []


def generate_entry(length_arg, base_string_arg):
    return ''.join(random.choice(base_string_arg) for i in range(length_arg))


def list2file(filename_arg):
    with open(filename_arg, "w") as f:
        for e in entries:
            f.write(f'{e}\n')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument("-a", "--amount", help="Amount of entries", type=int)
    parser.add_argument("-l", "--length", help="Length of an entry", type=int)
    parser.add_argument("-s", "--string", help="String of which the random entries are generated of", type=str)
    parser.add_argument("-o", "--output", help="Destination file", type=str)
    args = parser.parse_args()

    amount = 500
    if args.amount:
        amount = args.amount

    base_string = 'ABCDEFGHJKLMNPQRSTUVWXYZ0123456789'
    if args.string:
        base_string = args.string

    length = 5
    if args.length:
        length = args.length

    filename = 'output.csv'
    if args.output:
        filename = args.output

    while len(entries) < amount:
        entry = generate_entry(length, base_string)
        while entry in entries:
            entry = generate_entry(length, base_string)
        entries.append(entry)

    list2file(filename)

    print("Generated list")
