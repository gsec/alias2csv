def process(line):
    """Reformat a line from mutt-alias to csv.

    Assumes following format:
    'alias NICK_NAME FIRST_NAME LAST_NAME <EMAIL>'
    """
    alias_literal, nick, first, last, mail = line.split(" ")
    smail = mail.strip("><")
    return ",".join([first, last, smail, nick])


def gen_output(data):
    header = ["first name,last name,email-address,nickname"]
    lines = data.split("\n")
    for idx, line in enumerate(lines):
        if not line:
            continue
        try:
            header.append(process(line))
        except Exception as ex:
            print(f"ERROR: '{ex}'\nSkippd line {idx}:\t'{line}'")

    return "\n".join(header)


def main():
    INPUT_FNAME = "alias"
    OUTPUT_FNAME = "alias.csv"

    with open(INPUT_FNAME, "r") as handler:
        data = handler.read()

    with open(OUTPUT_FNAME, "w") as handler:
        handler.write(gen_output(data))

    print("All good, output to:", OUTPUT_FNAME)


if __name__ == "__main__":
    main()
