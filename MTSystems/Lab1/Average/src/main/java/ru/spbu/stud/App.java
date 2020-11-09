package ru.spbu.stud;

import ru.spbu.stud.utils.ParametersReader;

import java.util.HashMap;

public class App {
    public  static  void main(String[] args) {
        var parameters = ParametersReader.getTopologyParameters("parameters.txt");

        MainController mc = new MainController(parameters);
        mc.initAgents();
    }
}
