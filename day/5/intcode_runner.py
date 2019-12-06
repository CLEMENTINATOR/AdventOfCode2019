from enum import Enum
import collections

def load(intcode_data, mode, idx):
    if mode == 0:
        return intcode_data[idx]
    elif mode == 1:
        return idx

with open("input", "r") as f:
    intcode_file = f.read()
    intcode_data = intcode_file.split(',')
    for i in range(len(intcode_data)):
        intcode_data[i] = int(intcode_data[i])
    program_counter = 0

    while True:
        # decode op
        op_int      = intcode_data[program_counter]
        op          = op_int % 100
        first_mode  = (op_int % 1000)  // 100
        second_mode = (op_int % 10000) // 1000
        third_mode  = op_int // 10000
        #print("--------")
        #print("pc: {}".format(program_counter))
        #print("op_int: {}".format(op_int))
        #print("first_mode: {}".format(first_mode))
        #print("second_mode: {}".format(second_mode))
        #print("third_mode: {}".format(third_mode))

        if op == 99:
            print("Halt operation")
            break
        elif op == 1 or op == 2:
            arg1 = load(intcode_data, first_mode, intcode_data[program_counter + 1])
            arg2 = load(intcode_data, second_mode, intcode_data[program_counter + 2])
            arg3 = intcode_data[program_counter + 3]
            op_len = 4

            if op == 1:
                print("Addition operation ({} + {}) -> {}".format(arg1, arg2, arg3))
                output = arg1 + arg2
            if op == 2:
                print("Multiplication operation ({} x {}) -> {}".format(arg1, arg2, arg3))
                output = arg1 * arg2

            #print("arg1: {}".format(arg1))
            #print("arg2: {}".format(arg2))
            #print("arg3: {}".format(arg3))

            intcode_data[arg3] = output
        elif op == 3 or op == 4:
            op_len  = 2
            addr = intcode_data[program_counter + 1]

            if op == 3:
                print("Input operation (@{}): ".format(addr), end='')
                intcode_data[addr] = int(input())
            if op == 4:
                arg1 = load(intcode_data, first_mode, addr)
                print("Output operation (@{}): {}".format(addr, arg1))
        elif op == 5 or op == 6:
            arg1   = load(intcode_data, first_mode, intcode_data[program_counter + 1])
            arg2   = load(intcode_data, second_mode, intcode_data[program_counter + 2])
            op_len = 3
            if op == 5:
                print("Jump-if-true ({} != 0 -> {})".format(arg1, arg2))
                if arg1 != 0:
                    program_counter = arg2
                    continue
            if op == 6:
                print("Jump-if-false  ({} == 0 -> {})".format(arg1, arg2))
                if arg1 == 0:
                    program_counter = arg2
                    continue
        elif op == 7 or op == 8:
            arg1   = load(intcode_data, first_mode, intcode_data[program_counter + 1])
            arg2   = load(intcode_data, second_mode, intcode_data[program_counter + 2])
            arg3   = intcode_data[program_counter + 3]
            output = 0
            op_len = 4

            if op == 7:
                print("Less than ({} < {})".format(arg1, arg2))
                if arg1 < arg2:
                    output = 1

            if op == 8:
                print("Equals ({} == {})".format(arg1, arg2))
                if arg1 == arg2:
                    output = 1

            #print("arg1: {}".format(arg1))
            #print("arg2: {}".format(arg2))
            #print("arg3: {}".format(arg3))

            intcode_data[arg3] = output

        else:
            print("invalid opcode : {}".format(op))
            break

        program_counter += op_len