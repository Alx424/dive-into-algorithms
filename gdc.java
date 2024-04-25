public class gdc{
    public static int calculate(int x, int y) {
        int larger = Math.max(x, y);
        int smaller = Math.min(x, y);
        int remainder = larger % smaller;
        if(remainder == 0){
            return smaller;
        }
        if(remainder != 0){
            return calculate(smaller, remainder);
        }
        return 0;
    }
    public static void main(String[] args){
        System.out.println(calculate(33, 105));
    }
}