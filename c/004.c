#include <stdio.h>
#include <time.h>
#include <stdbool.h>
#include "euler.h"

// A palindromic number reads the same both ways. The largest palindrome made
// from the product of two 2-digit numbers is 9009 = 91 × 99.
// Find the largest palindrome made from the product of two 3-digit numbers.


int reverse(int n) {
  int input = n;
  int reversed = 0;
  while (n > 0) {
    reversed *= 10;
    reversed += n % 10;
    n /= 10;
  }
  return reversed;
}

int is_palindrome(int n) {
  return reverse(n) == n;
}

int palindrome_from(int n) {
  return n * 1000 + reverse(n);
}

int main() {
  int x = is_palindrome(1234321);
  printf("%d\n", x);
  long y = int_sqrt(24);
  printf("%ld\n", y);
}
