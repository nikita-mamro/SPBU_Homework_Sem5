package ru.spbu.stud;

import jade.core.behaviours.TickerBehaviour;
import jade.lang.acl.ACLMessage;

public class FindAverageBehaviour extends TickerBehaviour {
    private final AverageAgent agent;
    private int currentTick;
    private boolean IsFinished = false;
    private final int MAX_TICKS = 10000;
    private final int CENTER_ID = 1;

    FindAverageBehaviour(AverageAgent agent, long period) {
        super(agent, period);
        this.setFixedPeriod(true);
        this.agent = agent;
        this.currentTick = 0;
    }

    @Override
    protected void onTick() {
        agent.sendMessage();

        var msg = agent.blockingReceive();

        if (msg != null) {
            agent.proceedIncomingMessage(msg.getContent());

            if (agent.isCenter()) {
                System.out.println("Answer is " + agent.getValue());
            }

            this.stop();
        }


        if (!IsFinished && currentTick < MAX_TICKS) {
            //System.out.println("Agent " + this.agent.getLocalName() + ": tick=" + getTickCount());
            this.currentTick++;
        } else {
            if (!IsFinished) {
                System.out.println("Stopping agent" + agent.getLocalName() + ": Out of ticks :(");
            } else {
                System.out.println("Stopping agent" + agent.getLocalName() + ": Average has been found, :)");
            }
            this.stop();
        }
    }
}