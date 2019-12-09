import collections

class IntCodeComputer:
    def load(self, mode, idx):
        if mode == 0:
            return self.memory[idx]
        elif mode == 1:
            return idx
        elif mode == 2:
            #print(self.relative_base + idx)
            return self.memory[self.relative_base + idx]

    def save(self, mode, idx, value):
        if mode == 0:
            self.memory[idx] = value
        elif mode == 1:
            return idx
        elif mode == 2:
            self.memory[self.relative_base + idx]  = value


    def __init__(self, intcode_file):
        with open(intcode_file, "r") as f:
            intcode_file = f.read()
            intcode_data = intcode_file.split(',')
            self.memory = collections.defaultdict(int)
            self.args = []
            for i in range(len(intcode_data)):
                self.memory[i] = int(intcode_data[i])
            self.program_counter = 0
            self.relative_base = 0

    def run(self, input_args = []):
        while True:
            # decode op
            op_int      = self.memory[self.program_counter]
            op          = op_int % 100
            first_mode  = (op_int % 1000)  // 100
            second_mode = (op_int % 10000) // 1000
            third_mode  = op_int // 10000
            #print("--------")
            #print("pc: {}".format(self.program_counter))
            #print("op_int: {}".format(op_int))
            #print("first_mode: {}".format(first_mode))
            #print("second_mode: {}".format(second_mode))
            #print("third_mode: {}".format(third_mode))

            if op == 99:
                #print("Halt operation")
                break
            elif op == 1 or op == 2:
                arg1 = self.load(first_mode, self.memory[self.program_counter + 1])
                arg2 = self.load(second_mode, self.memory[self.program_counter + 2])
                arg3 = self.memory[self.program_counter + 3]
                op_len = 4

                if op == 1:
                    #print("Addition operation ({} + {}) -> {}".format(arg1, arg2, arg3))
                    output = arg1 + arg2
                if op == 2:
                    #print("Multiplication operation ({} x {}) -> {}".format(arg1, arg2, arg3))
                    output = arg1 * arg2

                self.save(third_mode, arg3, output)
            elif op == 3 or op == 4:
                op_len  = 2
                addr = self.memory[self.program_counter + 1]

                if op == 3:
                    input_arg = input_args.pop(0)
                    #print("Input operation (@{}): {}".format(addr, input_arg))
                    self.save(first_mode, addr, input_arg)
                if op == 4:
                    arg1 = self.load(first_mode, addr)
                    #print("Output operation (@{}): {}".format(addr, arg1))
                    self.program_counter += op_len
                    return arg1
            elif op == 5 or op == 6:
                arg1   = self.load(first_mode, self.memory[self.program_counter + 1])
                arg2   = self.load(second_mode, self.memory[self.program_counter + 2])
                op_len = 3
                if op == 5:
                    #print("Jump-if-true ({} != 0 -> {})".format(arg1, arg2))
                    if arg1 != 0:
                        self.program_counter = arg2
                        continue
                if op == 6:
                    #print("Jump-if-false  ({} == 0 -> {})".format(arg1, arg2))
                    if arg1 == 0:
                        self.program_counter = arg2
                        continue
            elif op == 7 or op == 8:
                arg1   = self.load(first_mode, self.memory[self.program_counter + 1])
                arg2   = self.load(second_mode, self.memory[self.program_counter + 2])
                arg3   = self.memory[self.program_counter + 3]
                output = 0
                op_len = 4

                if op == 7:
                    #print("Less than ({} < {})".format(arg1, arg2))
                    if arg1 < arg2:
                        output = 1

                if op == 8:
                    #print("Equals ({} == {})".format(arg1, arg2))
                    if arg1 == arg2:
                        output = 1

                self.save(third_mode, arg3, output)
            elif op == 9:
                arg1   = self.load(first_mode, self.memory[self.program_counter + 1])
                #print("Set relative base (+{})".format(arg1))
                self.relative_base += arg1
                op_len = 2
            else:
                #print("invalid opcode : {}".format(op))
                break

            self.program_counter += op_len

        return None

    def __enter__(self):
      return self

    def __exit__(self, type, value, tb):
      pass
