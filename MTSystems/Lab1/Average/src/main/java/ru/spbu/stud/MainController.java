package ru.spbu.stud;

import jade.core.Profile;
import jade.core.ProfileImpl;
import jade.core.Runtime;
import jade.wrapper.AgentController;
import jade.wrapper.ContainerController;

import java.util.HashMap;

public class MainController {
    private HashMap<Integer, String> parameters;

    public MainController(HashMap<Integer, String> parameters) {
        this.parameters = parameters;
    }

    void initAgents() {
        Runtime rt = Runtime.instance();
        Profile p = new ProfileImpl();
        p.setParameter(Profile.MAIN_HOST, "localhost");
        p.setParameter(Profile.MAIN_PORT, "10098");
        p.setParameter(Profile.GUI, "true");
        ContainerController cc = rt.createMainContainer(p);

        try {
            for(int i=1; i <= parameters.size(); i++) {
                AgentController agent = cc.createNewAgent(Integer.toString(i),
                        "ru.spbu.stud.AverageAgent", new Object[] {parameters.get(i), parameters.size()});
                agent.start();
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
