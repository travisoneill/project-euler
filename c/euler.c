#include "euler.h" 

long int_sqrt(long n) {
  long lo = 1L;
  long hi = n / 2;
  long mid;
  long val;
  while (hi - lo > 1) {
    mid = (hi + lo) / 2;
    val = mid * mid;
    if (val == n) {
      return mid;
    }
    if (val > n) {
      hi = mid;
    }
    if (val < n) {
      lo = mid;
    }
  }
  return lo;
}

int is_perfect_square(long n) {
  return int_sqrt(n) == int_sqrt(n - 1);
}
