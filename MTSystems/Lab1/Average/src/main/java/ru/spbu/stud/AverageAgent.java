package ru.spbu.stud;

import jade.core.AID;
import jade.core.Agent;
import jade.lang.acl.ACLMessage;

import java.security.InvalidParameterException;
import java.util.ArrayList;
import java.util.concurrent.TimeUnit;

public class AverageAgent extends Agent {
    private double value;
    private int numberOfAgents;

    public boolean isCenter() {
        return Integer.parseInt(getAID().getLocalName()) == 1;
    }

    public double getValue() {

        return value;
    }

    @Override
    protected void setup() {
        Object[] args = getArguments();

        if (args != null && args.length > 0) {
            if (args.length != 2) {
                throw new InvalidParameterException("Invalid parameters for agent setup");
            }

            value = Double.valueOf(args[0].toString());

            // Number of agents without center element
            numberOfAgents = Integer.valueOf(args[1].toString()) - 1;

            /*for (var neighbour : neighbours) {
                var uid = new AID(neighbour, AID.ISLOCALNAME);
                linkedAgents.add(uid);
            }*/
        }
        else {
            throw new InvalidParameterException("Invalid neighbours param");
        }

        addBehaviour(new FindAverageBehaviour(this, TimeUnit.SECONDS.toMillis(1)));
    }

    public void sendMessage() {
        ACLMessage newMes = new ACLMessage(ACLMessage.INFORM);
        //newMes.addReceiver();
        newMes.setContent(Double.toString(value));
        send(newMes);
    }

    public void proceedIncomingMessage(String msgContent) {
        var msgDoubleValue = Double.valueOf(msgContent);
        value = (value + msgDoubleValue) / 2;
    }
}