public class Euler002 {
  public static void main(String[] args) {
    // int[] fib = [1, 1];
    int a = 0;
    int b = 1;
    int total = 0;
    int temp;
    while ( b < 4000000 ) {
      if ( b % 2 == 0 ) {
        total += b;
      }

      temp = a + b;
      a = b;
      b = temp;
    }
    System.out.println(total);
  }
}
