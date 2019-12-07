from intcode_computer import IntCodeComputer
import itertools

intcode_file = "input"
phase_settings = list(itertools.permutations([0, 1, 2, 3, 4]))
max_output = 0
max_output_phase_settings = None

for phase_setting in phase_settings:
    input_signal = 0

    for phase in phase_setting:
        ic = IntCodeComputer(intcode_file)
        args = [phase, input_signal]
        input_signal = ic.run(args)

    if input_signal > max_output:
        max_output = input_signal

print("part 1: {}".format(max_output))


intcode_file = "input"
phase_settings = list(itertools.permutations([5, 6, 7, 8, 9]))
max_output = 0

for phase_setting in phase_settings:
    input_signal = 0
    amps = []
    first_run = True
    output = 0
    last_output = 0

    for i in range(5):
        amp = IntCodeComputer(intcode_file)
        amps.append(amp)

    while True:
        for i in range(5):
            if first_run:
                input_args = [phase_setting[i], input_signal]
            else:
                input_args = [input_signal]

            input_signal = amps[i].run(input_args)
            if not input_signal:
                break
        if not input_signal:
            break
        last_output = input_signal
        first_run = False
    if last_output > max_output:
        max_output = last_output

print("part2: {}".format(max_output))

