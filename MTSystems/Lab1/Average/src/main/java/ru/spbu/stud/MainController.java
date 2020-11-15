package ru.spbu.stud;

import jade.core.AID;
import jade.core.Profile;
import jade.core.ProfileImpl;
import jade.core.Runtime;
import jade.wrapper.AgentController;
import jade.wrapper.ContainerController;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.stream.Collector;
import java.util.stream.Collectors;

public class MainController {
    private HashMap<Integer, String> parameters;

    public MainController(HashMap<Integer, String> parameters) {
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
            var receivers = getReceivers(parameters);
            var requiredSendersCounts = getRequiredSendersCounts(receivers);

            for(int i = 0; i <= parameters.size(); i++) {
                AgentController agent = cc.createNewAgent(Integer.toString(i),
                        "ru.spbu.stud.AverageAgent", new Object[] {parameters.get(i), parameters.size(), receivers.get(i), requiredSendersCounts.get(i)});
                agent.start();
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    private HashMap<Integer, Integer> getReceivers(HashMap<Integer, String> parameters) {
        var receivers = new HashMap<Integer, Integer>();

        for (var id : parameters.keySet()) {
            receivers.put(id, findReceiverById(id, parameters.size()));
        }

        return  receivers;
    }

    private HashMap<Integer, Integer> getRequiredSendersCounts(HashMap<Integer, Integer> receivers) {
        var sendersCounts = new  HashMap<Integer, Integer>();

        for (var id : receivers.keySet()) {
            sendersCounts.put(id, receivers.values().stream().filter(item -> item == id).collect(Collectors.toList()).size());
        }

        return  sendersCounts;
    }

    private int findReceiverById(int id, int totalAgents) {
        if (id == 0) {
            return -1;
        }

        var buffer = new ArrayList<Integer>();

        for (var i = 0; i < totalAgents; ++i) {
            buffer.add(i + 1);
        }

        while (true) {
            var elementIndex = buffer.indexOf(id);

            if (elementIndex % 2 == 0) {
                if (elementIndex != buffer.size() - 1) {
                    return buffer.get(elementIndex + 1);
                }

                return 0;
            }

            var tmp = new ArrayList<Integer>();

            for (var i = 1; i < buffer.size(); i += 2) {
                tmp.add(buffer.get(i));
            }

            buffer = tmp;
        }
    }
}
