import java.util.Scanner; // [1] 입력을 위한 클래스 임포트

public class SimpleReview {

    public static void main(String[] args) {
        // [2] 변수 및 배열 선언
        Scanner scanner = new Scanner(System.in);
        String[] menuNames = {"아메리카노", "카페라떼", "아이스티"}; // 메뉴 이름 배열
        int[] menuPrices = {3000, 4000, 3500};                   // 메뉴 가격 배열
        int totalPrice = 0;                                      // 총 결제 금액
        boolean isRunning = true;                                // 반복 제어 변수

        System.out.println("=== 간단한 카페 키오스크 시작 ===");

        // [3] while 반복문 (사용자가 종료할 때까지 계속 실행)
        while (isRunning) {
            printMenu(menuNames, menuPrices); // 메서드 호출

            System.out.print("메뉴 번호를 선택하세요 (0: 종료/계산): ");
            int choice = scanner.nextInt(); // 정수 입력 받기

            // [4] 조건문 (if - else if - else)
            if (choice == 0) {
                System.out.println("\n주문을 종료합니다.");
                isRunning = false; // 반복문 탈출 조건
            } 
            else if (choice >= 1 && choice <= menuNames.length) {
                // 배열 인덱스는 0부터 시작하므로 (입력값 - 1)
                int index = choice - 1;
                System.out.println("✅ " + menuNames[index] + "를 장바구니에 담았습니다.");
                totalPrice += menuPrices[index]; // 누적 합계 계산
            } 
            else {
                System.out.println("⚠ 잘못된 번호입니다. 다시 입력해주세요.");
            }
            
            System.out.println("현재 총 금액: " + totalPrice + "원\n");
        }

        // [5] 결과 출력
        System.out.println("===============================");
        System.out.println("최종 결제 금액은 " + totalPrice + "원 입니다.");
        System.out.println("이용해 주셔서 감사합니다!");
        
        scanner.close(); // 리소스 해제
    }

    // [6] 메서드 분리: 메뉴판을 출력하는 기능
    public static void printMenu(String[] names, int[] prices) {
        System.out.println("----------- [MENU] -----------");
        // for 반복문 (배열 길이만큼 반복)
        for (int i = 0; i < names.length; i++) {
            // (i+1)을 해서 메뉴 번호를 1번부터 표시
            System.out.printf("%d. %s \t: %d원\n", (i + 1), names[i], prices[i]);
        }
        System.out.println("------------------------------");
    }
}