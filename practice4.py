set_a = {1,2,3,4,5}
set_b = {4,5,6,7,8}

print(set_a.union(set_b))

print(set_a.intersection(set_b))



sample_dict = {1: "coffee", 2: "tea", 3: "juice"}

sample_dict[2] = "Mint tea"

print(sample_dict)

def sum_off(* args):
    sum = 0
    for x in args:
        sum = sum + x
    return sum

print(sum_off(4, 5, 6))



def sum_all(** kwargs):
    sum =0
    for k, v in kwargs.items():
        sum = sum + v
    return sum

print(sum_all(pigs=2, cows=10, fowls=8)) 