def jump(jump_l):
    sub_list = []
    for i in range(1, len(jump_l) + 1):
        if jump_l[-i] - i >= -1:
            sub_list = jump_l[:len(jump_l) - i + 1]
    return sub_list

jump_list = [2, 3, 5, 1, 5, 1, 4, 1, 1]
jumps = 1

sub_jump = jump(jump_list)

while len(sub_jump) > 1:
    jumps += 1
    sub_jump = jump(sub_jump)
print(jumps)