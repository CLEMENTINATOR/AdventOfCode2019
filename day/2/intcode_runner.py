def process_intcode_program(int_code_ops):
    int_code_idx = 0

    while True:
        op      = int_code_ops[int_code_idx]
        if op == 99:
            break

        idx_1   = int_code_ops[int_code_idx + 1]
        idx_2   = int_code_ops[int_code_idx + 2]
        idx_3   = int_code_ops[int_code_idx + 3]

        value_1 = int_code_ops[idx_1]
        value_2 = int_code_ops[idx_2]

        if op == 1:
            int_code_ops[idx_3] = value_1 + value_2
        elif op == 2:
            int_code_ops[idx_3] = value_1 * value_2

        int_code_idx += 4
        if int_code_idx >= len(int_code_ops):
            break

    return int_code_ops[0]

with open("input", "r") as f:
    int_code_file = f.read()
    int_code_ops = int_code_file.split(',')

    for i in range(len(int_code_ops)):
        int_code_ops[i] = int(int_code_ops[i])

    int_code_ops_backup = int_code_ops.copy()

    # part 1
    int_code_ops[1] = 12
    int_code_ops[2] = 2

    print("part1 output: {}".format(process_intcode_program(int_code_ops)))

    for noun in range(99):
        for verb in range(99):
            int_code_ops = int_code_ops_backup.copy()
            int_code_ops[1] = noun
            int_code_ops[2] = verb

            if process_intcode_program(int_code_ops) == 19690720:
                print("part 2 output : {}".format(100 * noun + verb))
