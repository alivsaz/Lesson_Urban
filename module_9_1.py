# Вызов разом

def apply_all_func(int_list, *functions):
    functions = list(functions)
    num_list = list(map(int, int_list))
    results = {}
    for function in functions:
        result = function(num_list)
        results[function.__name__] = result
    return results

print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))