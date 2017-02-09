public class Euler003 {
  private static void primeFactors(long n) {
    int i = 2;
    while ( i * i < n || i < 4) {
      if ( n % i == 0 ) {
        System.out.println(i);
        n = n / i;
        i = 2;
      } else {
        i++;
      }
    }
    if ( n > 1 ) {
      System.out.println(n);
    }
  }

  public static void main(String[] args) {
    long n = 600851475143L;
    primeFactors(n);
  }
}
