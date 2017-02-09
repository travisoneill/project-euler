public class Euler004 {
  private static Boolean isPalindrome(int n) {
    int[] digits = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
    int idx = 11;
    while ( n > 0 ) {
      digits[idx] = n % 10;
      n = n / 10;
      idx--;
    }
    idx++;
    int r = digits.length - 1;
    while ( r > idx ) {
      if ( digits[r] != digits[idx] ) {
        return false;
      }
      r--;
      idx++;
    }
    return true;
  }

  public static void main(String[] args){
    int maxSeen = 0;
    int breakPoint = 0;
    int limit = 1000;
    for ( int x = limit; x > 0; x-- ) {
      for ( int y = x; y < limit; y++ ){
        if ( isPalindrome(x*y) ) {
          System.out.println(x*y);
          if( x*y > maxSeen ) {
            maxSeen = x * y;
          }
        }
      }
    }
    System.out.println(maxSeen);
  }
}
