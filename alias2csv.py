def process(line):
    """Reformat a line from mutt-alias to csv.

    Assumes following format:
    'alias NICK_NAME FIRST_NAMEs LAST_NAME <EMAIL>'
    """
    alias_literal, nick, *firsts, last, mail = line.strip().split(" ")
    smail = mail.strip("><")
    first = " ".join(firsts)
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
            continue
            #  print(f"ERROR: '{ex}'\nSkippd line {idx}:\t'{line}'")

    return "\n".join(header)


def main():
    INPUT_FNAME = "alias"
    OUTPUT_FNAME = "alias.csv"

    with open(INPUT_FNAME, "r") as handler:
        data = handler.read()

    with open(OUTPUT_FNAME, "w") as handler:
        handler.write(gen_output(data))

    print("Finished, output to:", OUTPUT_FNAME)


def test():
    data = "\n".join(
        [
            "alias phil Philipp Gaukler <pg@cif.core.net>",  # valid line
            "alias bert Bertram Chanson <bc@pro.vault.io>",  # valid line
            "INVALID LINE",  # skipped
            "    alias james William Archibald James Jr. Walterson <archi@who.the.not>",
            # leading whitespace gets stripped
        ]
    )
    expected = (
        "first name,last name,email-address,nickname\n"
        "Philipp,Gaukler,pg@cif.core.net,phil\n"
        "Bertram,Chanson,bc@pro.vault.io,bert\n"
        "William Archibald James Jr.,Walterson,archi@who.the.not,james"
    )
    processed = gen_output(data)
    assert processed == expected, "Test failed!"
    print("Passed!")


if __name__ == "__main__":
    main()
    #  test()
