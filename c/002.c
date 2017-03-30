#include <stdio.h>
#include <time.h>

int fibonacci_sum(int limit) {
  int a = 0;
  int b = 1;
  long temp;
  long sum = 0L;
  while (b < limit) {
    if (b % 2 == 0) {
      sum += b;
    }
    temp = a + b;
    a = b;
    b = temp;
  }
  return sum;
}

int main() {
  time_t t0 = clock();
  int sum = fibonacci_sum(4000000);
  time_t t1 = clock();
  int runtime = t1 - t0;
  printf("%ld\n", sum);
  printf("run time: %ld μs\n", runtime);
}
