#include <stdio.h>
#include <time.h>

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

long largest_prime_factor(long n) {
  int largest = 0;
  while (n % 2 == 0) {
    largest = 2;
    n /= 2;
  }
  int i = 3;
  int limit = int_sqrt(n);
  while (i <= limit) {
    if (n % i == 0) {
      largest = i;
      n /= i;
      limit = int_sqrt(n);
    } else {
      i += 2;
    }
  }
  if (n > largest) {
    return n;
  } else {
    return largest;
  }
}

int main() {
  time_t t0 = clock();
  printf("%ld\n", largest_prime_factor(600851475143L));
  time_t t1 = clock();
  int runtime = t1 - t0;
  printf("run time: %d μs\n", runtime);
}
