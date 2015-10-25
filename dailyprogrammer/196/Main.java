package org.writemorecode.DailyProgrammer196;

import java.util.Arrays;

public class Main {

    public static void main(String[] args) {
        IntegerSet set_x = new IntegerSet(Arrays.asList(1,2,3,4));
        IntegerSet set_y = new IntegerSet(Arrays.asList(4,5,1,2));

        System.out.println("Set X: " + set_x);
        System.out.println("Set Y: " + set_y);

        if(set_y.Contains(9)) {
            System.out.println(set_y + " contains '9'");
        }

        if(set_x.Equals(set_y)) {
            System.out.println("Set X equals set Y");
        }

        System.out.println(IntegerSet.Intersection(set_x, set_y));
        System.out.println(IntegerSet.Union(set_x, set_y));

    }
}
