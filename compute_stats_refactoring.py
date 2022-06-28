import math

def read_list_numbers(file):
    list_numbers = []
    with open(file, "r") as reader:
        for line in reader:
            number = int(line)
            list_numbers.append(number)
    return list_numbers

def compute_length(list_numbers):
    return len(list_numbers)
def compute_sum(list_numbers):
    return sum(list_numbers)
def compute_average(list_numbers):
    return round(compute_sum(list_numbers)/compute_length(list_numbers))
def compute_min(list_numbers):
    return min(list_numbers)
def compute_max(list_numbers):
    return max(list_numbers)

def compute_statistics(list_numbers):
    dict_key_func = {
        "total":compute_length,
        "summation": compute_sum,
        "average": compute_average,
        "Minimum": compute_min,
        "Maximum": compute_max
    }
    d_statistics = {
        k:f(list_numbers) for k,f in dict_key_func.items() 
    }
    return d_statistics

def print_statistics(d_statistics):
    for k,v in d_statistics.items():
        print(f"{k}: {v}")

def compute_harmonic_mean(list_numbers):
    n_numbers = compute_length(list_numbers)
    sum_of_inverse = sum([(1/number) for number in list_numbers])
    return n_numbers/sum_of_inverse

def compute_variance(list_numbers):
    mean = compute_average(list_numbers)
    n_numbers = compute_length(list_numbers)
    list_squared_mean_diff = [(number-mean)**2 for number in list_numbers]
    tp_sum = sum(list_squared_mean_diff)
    return tp_sum/(n_numbers-1)

def compute_standard_deviation(list_numbers):
    variance = compute_variance(list_numbers)
    std = math.sqrt(variance)
    return std

FILE_PATH = 'random_nums.txt'
if __name__ == '__main__':
    list_numbers = read_list_numbers(FILE_PATH)
    d_statistics = compute_statistics(list_numbers)
    print_statistics(d_statistics)
