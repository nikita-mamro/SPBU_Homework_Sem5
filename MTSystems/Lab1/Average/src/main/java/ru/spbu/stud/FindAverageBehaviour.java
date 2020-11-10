package ru.spbu.stud;

import jade.core.behaviours.TickerBehaviour;

public class FindAverageBehaviour extends TickerBehaviour {
    private final AverageAgent agent;

    FindAverageBehaviour(AverageAgent agent, long period) {
        super(agent, period);
        this.setFixedPeriod(true);
        this.agent = agent;
    }

    @Override
    protected void onTick() {
        if (agent.isTriggered()) {
            stop();
        }

        if (!agent.isCenter()) {
            agent.sendMessage();
        }

        var msg = agent.blockingReceive();

        if (msg != null) {
            agent.proceedIncomingMessage(msg.getContent());

            if (agent.isCenter()) {
                System.out.println("Average has been found. Answer is " + agent.getValue());
                stop();
            }
        }
    }
}