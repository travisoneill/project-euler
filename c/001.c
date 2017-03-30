#include <stdio.h>
#include <time.h>

int euler001(int n) {
  int sum = 0;
  for (int i = 0; i < 1000; i += 1) {
    if ( i % 3 == 0 || i % 5 == 0 ) {
      sum = sum + i;
    }
  }
  return sum;
}

int main() {
  time_t t0 = clock();
  printf("%d\n", euler001(1000000));
  time_t t1 = clock();
  long runtime = t1 - t0;
  printf("run time: %ld μs\n", runtime);
  return 0;
}
