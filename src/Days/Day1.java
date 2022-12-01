package Days;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.LinkedList;
import java.util.Scanner;

public class Day1 {
    public static void run() {
        /*int[] array = {3, 2, 1, 0, 10, 9, 8};
        int[] top3 = {0, 0, 0};

        for (int i = 0; i < array.length; i++) {
            check_top(top3, array[i]);
            for (int j = 0; j < top3.length; j++) {
                System.out.println(top3[j]);
            }
            System.out.println("---");
        }
        //shiftRightFromIndex(array, 0);

        for (int i = 0; i < top3.length; i++) {
            System.out.println(top3[i]);
        }*/


        LinkedList<Integer> food_by_elf = new LinkedList<>();

        try {
            File file = new File("data/day1.txt");
            Scanner fileScanner = new Scanner(file);
            int temp_food = 0;
            while (fileScanner.hasNextLine()) {
                try {
                    int temp = Integer.parseInt(fileScanner.nextLine());
                    temp_food += temp;
                }catch (NumberFormatException ignored) {
                    food_by_elf.add(temp_food);
                    temp_food = 0;
                }
            }

            food_by_elf.add(temp_food);
            temp_food = 0;
            int[] top3_food = {0, 0, 0};

            for (Integer elf_food : food_by_elf) {
                //if (elf_food > temp_food) temp_food = elf_food;
                check_top(top3_food, elf_food);
                System.out.println(food_by_elf.indexOf(elf_food) + "- " + elf_food);
            }
            //System.out.println("max: " + temp_food);
            for (int f : top3_food) {
                System.out.println(f);
                temp_food += f;
            }
            System.out.println("total: " + temp_food);
        }
        catch(FileNotFoundException e) {
            e.printStackTrace();
        }
    }

    private static void check_top (int[] top3, int number) {
        for (int i = 0; i < top3.length; i++) {
            if (number > top3[i]) {
                shiftRightFromIndex(top3, i);
                top3[i] = number;
                return;
            }
        }
    }

    private static void shiftRightFromIndex (int[] array, int index) {
        int tmp1, tmp2 = array[index];
        for (int i = index+1; i < array.length; i++) {
            tmp1 = array[i];
            array[i] = tmp2;
            tmp2 = tmp1;
        }
    }
}
