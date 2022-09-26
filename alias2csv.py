INPUT_FNAME = "alias"
OUTPUT_FNAME = "alias.csv"

with open(INPUT_FNAME, "r") as handler:
    data = handler.read()


def process(line):
    try:
        a, nick, first, last, mail = line.split(" ")
    except Exception as ex:
        print("Error")
        return
    smail = mail.strip("><")
    return ",".join([first, last, smail, nick])


lines = data.split("\n")
header = "first name,last name,email-address,nickname"
processed = "\n".join(process(line) for line in lines if line)
output = header + "\n" + processed

with open(OUTPUT_FNAME, "w") as handler:
    handler.write(output)
