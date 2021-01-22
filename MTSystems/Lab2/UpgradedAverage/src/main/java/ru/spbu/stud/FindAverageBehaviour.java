package ru.spbu.stud;

import jade.core.AID;
import jade.core.behaviours.TickerBehaviour;
import jade.lang.acl.ACLMessage;

import java.util.ArrayList;
import java.util.concurrent.ThreadLocalRandom;

public class FindAverageBehaviour extends TickerBehaviour {
    private final AverageAgent agent;
    private final int aid;
    private final double alpha;
    private final double b;
    private final ArrayList<AID> neighbours;

    FindAverageBehaviour(AverageAgent agent, ArrayList<AID> neighbours,  long period) {
        super(agent, period);
        this.setFixedPeriod(true);
        this.agent = agent;
        this.neighbours = neighbours;
        this.alpha = StateHolder.getInstance().getAlpha();
        this.b = StateHolder.getInstance().getB();
        this.aid = Integer.parseInt(agent.getAID().getLocalName());
    }

    @Override
    protected void onTick() {
        // Check if agent has already sent a message
        if (StateHolder.getInstance().checkSentAgent(aid)) {
            // Sending messages to neighbours
            for (var nAID: neighbours) {
                // Check if connection fails
                if (Math.random() < 0.8) {
                    return;
                }
                var msg = new ACLMessage(ACLMessage.INFORM);
                msg.addReceiver(nAID);
                // Add interference
                var valueWithInterference = StateHolder.getInstance().getAgentValue(aid) + ThreadLocalRandom.current().nextDouble(-1, 1);
                msg.setContent(Double.toString(valueWithInterference));
                agent.send(msg);
            }

            StateHolder.getInstance().setSentAgent(aid);
        }

        if (aid == 0) {
            var res = StateHolder.getInstance().getAgentValue(aid);
            System.out.printf("STATE: %f", res);

            if (StateHolder.getInstance().counterFinished()) {
                System.out.printf("FINISH with %f", res);
            }
        }

        var msg = agent.blockingReceive();

        if (msg != null) {
            var current = StateHolder.getInstance().getAgentValue(aid);
            var uDelta = b * (Double.parseDouble(msg.getContent()) - current);
            var uCurrent = StateHolder.getInstance().getUValue(aid);
            StateHolder.getInstance().setUValue(aid, uCurrent + uDelta);
        }

        if (StateHolder.getInstance().checkAllSentAgents()) {
            StateHolder.
        }
    }
}