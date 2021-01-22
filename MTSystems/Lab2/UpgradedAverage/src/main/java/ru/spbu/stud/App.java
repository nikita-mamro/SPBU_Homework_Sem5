package ru.spbu.stud;

import java.util.HashMap;
import java.util.concurrent.ThreadLocalRandom;

public class App {
    public static void main(String[] args) {
        var parameters = new HashMap<Integer, Double>();

        for (var i = 0; i < 5; ++i) {
            var randomDouble = ThreadLocalRandom.current().nextDouble(-10, 10);
            parameters.put(i, randomDouble);
            System.out.println(randomDouble);
        }

        var average = parameters.values().stream().mapToDouble(a -> a).average();
        System.out.println("Average:");
        System.out.println(average.getAsDouble());

        MainController mc = new MainController(parameters);
        mc.initAgents();
    }
}
