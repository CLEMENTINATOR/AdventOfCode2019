def is_part2_password_valid(password):
    last_digit = -1
    str_passwd = str(password)
    has_duplicate = False
    is_always_incrementing = True
    has_only_twice_dup = False
    dup_count = 0

    for c in str_passwd:
        c = int(c)
        if last_digit == c:
            has_duplicate = True
            dup_count += 1
        else:
            if dup_count == 1:
                has_only_twice_dup = True
            dup_count = 0
        if last_digit > c:
            is_always_incrementing = False
        last_digit = c

    if dup_count == 1:
        has_only_twice_dup = True

    return has_duplicate and is_always_incrementing and has_only_twice_dup

def is_part1_password_valid(password):
    last_digit = -1
    str_passwd = str(password)
    has_duplicate = False
    is_always_incrementing = True

    for c in str_passwd:
        c = int(c)
        if last_digit == c:
            has_duplicate = True
        if last_digit > c:
            is_always_incrementing = False
        last_digit = c

    return has_duplicate and is_always_incrementing

with open("input", "r") as f:
    password_range = f.read().split("-")
    password_start = int(password_range[0])
    password_end   = int(password_range[1])

    valid_part1_count = 0
    valid_part2_count = 0
    for passwd in range(password_start, password_end):
        if is_part1_password_valid(passwd):
            valid_part1_count += 1
        if is_part2_password_valid(passwd):
            valid_part2_count += 1

    print(f"number of part1 matches: {valid_part1_count}")
    print(f"number of part2 matches: {valid_part2_count}")
