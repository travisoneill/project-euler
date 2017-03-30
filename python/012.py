from generators import triangular
from primesandfactors import prime_factors, all_factors

def first_tri_num_with_more_than_n_factors(n):
    for tri_number in triangular(None):
        if 2**len(prime_factors(tri_number)) >= n:
            if len(all_factors(tri_number, include_self=True)) > n:
                return tri_number
