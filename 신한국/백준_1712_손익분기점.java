public class Main{
    public static void main(String[] args) {
        // 백준 1712 _ 손익분기점

        // 입력변수
        Scanner sc = new Scanner(System.in);
        int A = sc.nextInt(); // 고정 비용
        int B = sc.nextInt(); // 가변 비용
        int C = sc.nextInt(); // 노트북 가격

        int profit = C - B; // 노트북 가격 - 가변 비용 즉, 순이익

        if(profit <= 0) { // 순이익이 0보다 작거나 같으면 의미가 없음
            System.out.println("-1");
        } else {
            System.out.println(A/profit + 1);
        }
    }
}