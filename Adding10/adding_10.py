
num_dict = {
    'a':1,
    'b':2,
    'c':3,
    'd':4,
    'e':5
    }

def add10(sample_dict):
    for k in sample_dict.keys():
        sample_dict[k] += 10
    return sample_dict


print(num_dict)
result = add10(num_dict)

print(result)