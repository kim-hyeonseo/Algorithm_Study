import java.util.Scanner;

public class 백준_2941_크로아티아알파벳 {
    public static void main(String[] args) {
        // 백준 2941 _ 크로아티아 알파벳

        // 입력변수
        Scanner sc = new Scanner(System.in);
        String input = sc.nextLine();

        // 크로아티아 알파벳 배열
        String[] crozhe = {"c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="};

        for (String s: crozhe) { // for each 문을 통한 배열 문자 대입
            if(input.contains(s)) { // input 문자열과 비교
                input = input.replace(s, "i"); // 비교된 문자열을 임의 문자 i로 변경
            }
        }
        System.out.println(input.length()); // 문자열 길이 출력
    }
}