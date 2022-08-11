import java.util.Scanner;

public class 백준_10809_알파벳찾기 {
    public static void main(String[] args) {
        // 백준 10809 _ 알파벳 찾기

        // 입력변수
        Scanner sc = new Scanner(System.in);
        String input = sc.nextLine(); // 문자열 입력

        char[] c = input.toCharArray(); // 문자열 -> char 배열로 변환
        for(int i = 'a'; i <= 'z'; i++) { // 'a'를 int로 변환 즉, 아스키코드 이용 -> 97을 return함
            for(int j = 0; j < c.length; j++) { // 문자열 안에 i번째 문자가 있을 때까지 순환함
                if(i == c[j]) { // 있다면 문자열 내 자릿 수를 출력
                    System.out.print(j+ " ");
                    break;
                }
                if(j == c.length - 1) { // 없다면 -1을 출력
                    System.out.print(-1 + " ");
                }
            }
        }
    }
}