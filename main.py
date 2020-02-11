import rand_utils as ru

print('size \t\t    M \t\t    D')
for size in [10, 100, 1000, 10000]:
    rands = ru.get_rand_list(size)
    specs = ru.get_specs(rands)
    print(size, '\t\t', round(specs['expected value'], 5), '\t', round(specs['dispersion'], 5))
