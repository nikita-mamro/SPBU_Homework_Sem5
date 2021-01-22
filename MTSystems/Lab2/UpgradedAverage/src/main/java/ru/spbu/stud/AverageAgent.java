package ru.spbu.stud;

import jade.core.AID;
import jade.core.Agent;

import java.security.InvalidParameterException;
import java.util.ArrayList;
import java.util.concurrent.TimeUnit;

public class AverageAgent extends Agent {
    @Override
    protected void setup() {
        // Value in current node + total number of nodes including center node
        Object[] args = getArguments();

        ArrayList<AID> neighbours;

        if (args != null && args.length > 0) {
            if (args.length != 1) {
                throw new InvalidParameterException("Invalid parameters for agent setup");
            }

            var value = Double.parseDouble(args[0].toString());
            var id = Integer.parseInt(getAID().getLocalName());
            StateHolder.getInstance().setAgentValue(id, value);

            neighbours = new ArrayList<>(9);
            for (var i = 0; i < 10; ++i) {
                if (i != id) {
                    neighbours.add(new AID(Integer.toString(id), AID.ISLOCALNAME));
                }
            }
        }
        else {
            throw new InvalidParameterException("Invalid neighbours param");
        }

        addBehaviour(new FindAverageBehaviour(this, neighbours, TimeUnit.SECONDS.toMillis(1)));
    }
}