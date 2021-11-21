summ = 2
fib_num_prev = 1
fib_num_next = 2
fib_num_prom = fib_num_prev + fib_num_next
while fib_num_prom < 4000000:
    #    print(fib_num_prom)
    if fib_num_prom % 2 == 0:
        summ += fib_num_prom
    fib_num_prev = fib_num_next
    fib_num_next = fib_num_prom
    fib_num_prom = fib_num_prev + fib_num_next
print(summ)
