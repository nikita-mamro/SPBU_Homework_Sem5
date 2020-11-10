package ru.spbu.stud;

import jade.core.AID;
import jade.core.Agent;
import jade.lang.acl.ACLMessage;

import java.security.InvalidParameterException;
import java.util.ArrayList;
import java.util.concurrent.TimeUnit;

public class AverageAgent extends Agent {
    private double value;
    private AID receiverAID;
    // Shows if ready to send message to receiver
    private boolean isPending;
    private boolean isTriggered;

    public boolean isPending() {
        return isPending;
    }

    public boolean isTriggered() {
        return isTriggered;
    }

    public boolean isCenter() {
        return Integer.parseInt(getAID().getLocalName()) == 0;
    }

    public double getValue() {
        return value;
    }

    public void sendMessage() {
        if (isPending) {
            ACLMessage newMes = new ACLMessage(ACLMessage.INFORM);
            newMes.addReceiver(receiverAID);
            newMes.setContent(Double.toString(value));
            send(newMes);
            isPending = false;
            isTriggered = true;
        }
    }

    public void proceedIncomingMessage(String msgContent) {
        double msgDoubleValue = Double.parseDouble(msgContent);
        isPending = true;
        value = (value + msgDoubleValue) / 2;
    }

    @Override
    protected void setup() {
        // Value in current node + total number of nodes including center node
        Object[] args = getArguments();

        if (args != null && args.length > 0) {
            if (args.length != 2) {
                throw new InvalidParameterException("Invalid parameters for agent setup");
            }

            value = Double.parseDouble(args[0].toString());

            // Number of agents without center element
            var numberOfAgents = Integer.parseInt(args[1].toString()) - 1;

            var id = Integer.parseInt(getAID().getLocalName());

            isPending = id % 2 == 1 && id != numberOfAgents;

            if (id != 0) {
                receiverAID = getReceiverAID(id, numberOfAgents);
            }
        }
        else {
            throw new InvalidParameterException("Invalid neighbours param");
        }

        addBehaviour(new FindAverageBehaviour(this, TimeUnit.SECONDS.toMillis(1)));
    }

    private AID getReceiverAID(int id, int totalAgents) {
        var buffer = new ArrayList<Integer>();

        for (var i = 0; i < totalAgents; ++i) {
            buffer.add(i + 1);
        }

        while (true) {
            var elementIndex = buffer.indexOf(id);

            if (elementIndex % 2 == 0) {
                if (elementIndex != buffer.size() - 1) {
                    return new AID(Integer.toString(buffer.get(elementIndex + 1)), AID.ISLOCALNAME);
                }

                return new AID(Integer.toString(0), AID.ISLOCALNAME);
            }

            var tmp = new ArrayList<Integer>();

            for (var i = 1; i < buffer.size(); i += 2) {
                tmp.add(buffer.get(i));
            }

            buffer = tmp;
        }
    }
}