package ru.spbu.stud;

import jade.core.AID;
import jade.core.behaviours.TickerBehaviour;
import jade.lang.acl.ACLMessage;

import java.util.ArrayList;
import java.util.concurrent.ThreadLocalRandom;

public class FindAverageBehaviour extends TickerBehaviour {
    private final AverageAgent agent;
    private final int aid;
    private final ArrayList<AID> neighbours;

    FindAverageBehaviour(AverageAgent agent, ArrayList<AID> neighbours,  long period) {
        super(agent, period);
        this.setFixedPeriod(true);
        this.agent = agent;
        this.neighbours = neighbours;
        this.aid = Integer.parseInt(agent.getAID().getLocalName());
    }

    @Override
    protected void onTick() {
        // Check if agent has already sent a message
        if (!StateHolder.getInstance().checkSentAgent(aid)) {
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
            System.out.printf("STATE: %f\n", res);

            System.out.println(StateHolder.getInstance().counterFinished());
            if (StateHolder.getInstance().counterFinished()) {
                System.out.printf("FINISH with %f\n", res);
                stop();
            }
        }

        var msg = agent.blockingReceive(5);

        if (msg != null) {
            var current = StateHolder.getInstance().getAgentValue(aid);
            var uDelta = StateHolder.getInstance().getB() * (Double.parseDouble(msg.getContent()) - current);
            var uCurrent = StateHolder.getInstance().getUValue(aid);
            StateHolder.getInstance().setUValue(aid, uCurrent + uDelta);
        }

        if (StateHolder.getInstance().checkAllSentAgents()) {
            StateHolder.getInstance().resetSentList();
            for (var id = 0; id < 5; ++id) {
                var u = StateHolder.getInstance().getUValue(aid);
                var current = StateHolder.getInstance().getAgentValue(aid);
                StateHolder.getInstance().setAgentValue(aid, current + u * StateHolder.getInstance().getAlpha());
            }
            StateHolder.getInstance().resetUS();
            StateHolder.getInstance().incrementCounter();
        }

        agent.doWait(10);
    }
}