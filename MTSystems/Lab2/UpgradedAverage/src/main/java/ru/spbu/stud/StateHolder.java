package ru.spbu.stud;

import java.util.ArrayList;

public class StateHolder {
    // Alpha from local voting protocol formula
    private double alpha = 0.1;
    // Fixed b from local voting protocol formula
    private double b = 1;
    // Ticks counter
    private int counter = 0;
    // Maximum number of ticks
    private int maxCounter = 15;
    // Flags to check if agent has sent message on current tick
    private ArrayList<Boolean> sent = new ArrayList<>(10);
    // Current values in agents
    private ArrayList<Double> values = new ArrayList<>(10);
    // Intermediate results for 'u'
    private ArrayList<Double> us = new ArrayList<>(10);

    private static StateHolder self = new StateHolder();
    public static StateHolder getInstance() { return self; }

    public double getAlpha() {
        return alpha;
    }

    public double getB() {
        return b;
    }

    public void incrementCounter() {
        counter++;
    }

    public boolean counterFinished() {
        return counter >= maxCounter;
    }

    public boolean checkSentAgent(int id) {
        return sent.get(id);
    }

    public boolean checkAllSentAgents() {
        return !sent.contains(false);
    }

    public void setSentAgent(int id) {
        sent.set(id, true);
    }

    public double getAgentValue(int id) {
        return values.get(id);
    }

    public void setAgentValue(int id, double val) {
        values.set(id, val);
    }

    public double getUValue(int id) {
        return us.get(id);
    }

    public void setUValue(int id, double val) {
        us.set(id, val);
    }

    public void resetSentList() {
        sent = new ArrayList<>(10);
    }

    public void resetUS() {
        us = new ArrayList<>(10);
    }
}
