import java.util.Scanner;

public class 백준_4344_평균은넘겠지 {
    public static void main(String[] args) {
        // 백준 4344 _ 평균은 넘겠지

        // 입력변수
        Scanner sc = new Scanner(System.in);
        int T = sc.nextInt(); // 테스트 케이스
        int[] arr;

        for(int i = 0; i < T; i++) {
            int num = sc.nextInt(); // 학생 수
            arr = new int[num]; // 성적 배열 크기 지정

            double sum = 0; // 점수 합

            for(int j = 0; j < arr.length; j++) {
                arr[j] = sc.nextInt(); // 점수 입력
                sum += arr[j];
            }
            double avg = sum / num; // 평균
            double count = 0; // 평균 이상 학생 수 세기

            for(int j = 0; j < num; j++) {
                if(arr[j] > avg) {
                    count++;
                }
            }
            System.out.printf("%.3f%%\n", (count/num) * 100);
        }
    }
}