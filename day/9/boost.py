from intcode_computer import IntCodeComputer

intcode_file = "input"

with IntCodeComputer(intcode_file) as ic:
    while True:
        out = ic.run([2])
        if out != None:
            print(out)
        else:
            break
