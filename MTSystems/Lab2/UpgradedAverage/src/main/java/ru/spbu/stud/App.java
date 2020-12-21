package ru.spbu.stud;

import ru.spbu.stud.utils.ParametersReader;
import java.util.Scanner;

public class App {
    public  static  void main(String[] args) {
        var parameters = ParametersReader.getTopologyParameters("parameters.txt");

        var myInput = new Scanner( System.in );
        System.out.print( "Введите шаг протокола локального голосования: " );
        var step = myInput.nextDouble();

        MainController mc = new MainController(parameters, step);
        mc.initAgents();
    }
}
