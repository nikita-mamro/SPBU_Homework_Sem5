package ru.spbu.stud;

import jade.core.Profile;
import jade.core.ProfileImpl;
import jade.core.Runtime;
import jade.wrapper.AgentController;
import jade.wrapper.ContainerController;

import java.util.HashMap;

public class MainController {
    private final HashMap<Integer, Double> parameters;

    public MainController(HashMap<Integer, Double> parameters) {
        this.parameters = parameters;
    }

    public void initAgents() {
        Runtime rt = Runtime.instance();
        Profile p = new ProfileImpl();
        p.setParameter(Profile.MAIN_HOST, "localhost");
        p.setParameter(Profile.MAIN_PORT, "10098");
        p.setParameter(Profile.GUI, "true");
        ContainerController cc = rt.createMainContainer(p);

        try {
            for(int i = 0; i < parameters.size(); i++) {
                AgentController agent = cc.createNewAgent(Integer.toString(i),
                        "ru.spbu.stud.AverageAgent", new Object[] { parameters.get(i) });
                agent.start();
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
