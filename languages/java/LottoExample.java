import java.util.*;

public class LottoExample {
    public static void main(String[] args) {
        Set<Integer> lottoSet = new HashSet<>();
        Random random = new Random();

        while(lottoSet.size() < 6){
            lottoSet.add(random.nextInt(45)+1);
        }

        List<Integer> sortedLotto = new ArrayList<>(lottoSet);
        Collections.sort(sortedLotto);
        System.out.println(sortedLotto);
    }
}