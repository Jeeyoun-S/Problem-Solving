import java.util.*;

class Solution {
    public int[] solution(String[] genres, int[] plays) {
        int N = genres.length;
        HashMap<String, Integer> totals = new HashMap<>();

        for (int i=0; i<N; i++) {
            String genre = genres[i];
            int play = plays[i];
            
            if (totals.containsKey(genre)) totals.put(genre, totals.get(genre) + play);
            else totals.put(genre, play);
        }
        
        // System.out.println(totals.toString());
        
        ArrayList<Integer> indexes = new ArrayList<>();
        for (int i=0; i<genres.length; i++) indexes.add(i);
        
        Collections.sort(indexes, new Comparator<Integer>() {
            @Override
            public int compare(Integer o1, Integer o2) {
                String genreA = genres[o1];
                int totalA = totals.get(genreA);
                int playA = plays[o1];
                
                String genreB = genres[o2];
                int totalB = totals.get(genreB);
                int playB = plays[o2];
                
                if (totalA > totalB) return -1;
                else if (totalA < totalB) return 1;
                else {
                    if (playA > playB) return -1;
                    else if (playA < playB) return 1;
                    else {
                        if (o1 > o2) return 1;
                        else return -1;
                    }
                }
            }
        });
        
        // System.out.println(arr.toString());
        ArrayList<Integer> answer = new ArrayList<>();
        String before = "";
        int cnt = 0;
        for (int index : indexes) {
            String genre = genres[index];
            if (genre.equals(before)) {
                if (cnt >= 2) continue;
                cnt++;
                answer.add(index);
            } else {
                cnt = 1;
                before = genre;
                answer.add(index);
            }
        }
        
        return answer.stream().mapToInt(x -> x).toArray();
    }
}