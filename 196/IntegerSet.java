package org.writemorecode.DailyProgrammer196;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class IntegerSet {

    private List<Integer> values;

    /**
     * Constructor for IntegerSet.
     * @param v The values for the set.
     */
    public IntegerSet(List<Integer> v) {
        values = v;
    }

    /**
     * Returns the set as a string.
     * @return A string-representation of the set.
     */
    public String toString() {
        return values.toString();
    }

    /**
     * Checks if the set contains a value.
     * @param value The value to check for.
     * @return Returns true if the set contains a value.
     */
    public boolean Contains(int value) {
        return values.contains(value);
    }

    /**
     * Checks if set_b is equal to the other set.
     * @param set_b The set to compare to the other set.
     * @return Returns true is set_b is equal to the other set.
     */
    public boolean Equals(IntegerSet set_b) {
        if(values.size() != set_b.values.size()) {
            return false;
        } else {
            List<Integer> list_a = new ArrayList<>(values);
            List<Integer> list_b = new ArrayList<>(set_b.values);

            Collections.sort(list_a);
            Collections.sort(list_b);

            if(list_a.equals(list_b)) {
                return true;
            } else {
                return false;
            }
        }
    }

    /**
     * Returns the union from set_a and set_b
     * @param set_a The first set.
     * @param set_b The second set.
     * @return The intersection of set_a and set_b
     */
    public static List<Integer> Union(IntegerSet set_a, IntegerSet set_b) {
        List<Integer> set_c = new ArrayList<>();
        List<Integer> set_d = new ArrayList<>();

        // Add all values from set_a and set_b to set_c
        set_c.addAll(set_a.values);
        set_c.addAll(set_b.values);

        for(int i : set_c) {
            if(!set_d.contains(i)) {
                set_d.add(i);
            }
        }

        return set_d;
    }

    /**
     * Returns the intersection from set_a and set_b
     * @param set_a The first set.
     * @param set_b The second set.
     * @return The intersection of set_a and set_b
     */
    public static List<Integer> Intersection(IntegerSet set_a, IntegerSet set_b) {
        List<Integer> set_c = new ArrayList<>();
        for(int i : set_a.values) {
            for(int j : set_b.values) {
                if(i == j) {
                    set_c.add(i);
                }
            }
        }

        return set_c;

    }
}
