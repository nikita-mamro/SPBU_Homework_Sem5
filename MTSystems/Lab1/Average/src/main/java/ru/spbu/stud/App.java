package ru.spbu.stud;

import ru.spbu.stud.utils.ParametersReader;

public class App {
    public  static  void main(String[] args) {
        var parameters = ParametersReader.getTopologyParameters("parameters.txt");

        MainController mc = new MainController(parameters);
        mc.initAgents();
    }
}
