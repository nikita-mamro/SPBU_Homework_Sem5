package ru.spbu.stud;

import java.util.HashMap;
import java.util.concurrent.ThreadLocalRandom;

public class App {
    public static void main(String[] args) {
        var parameters = new HashMap<Integer, String>();

        for (var i = 0; i < 10; ++i) {
            var randomDouble = ThreadLocalRandom.current().nextDouble(-10, 10);
            parameters.put(i, Double.toString(randomDouble));
            System.out.println(randomDouble);
        }

        var average = parameters.keySet().stream().mapToDouble(a -> a).average();
        System.out.println("Average:");
        System.out.println(average);

        MainController mc = new MainController(parameters);
        mc.initAgents();
    }
}
