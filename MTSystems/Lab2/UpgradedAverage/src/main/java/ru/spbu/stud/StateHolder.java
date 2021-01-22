package ru.spbu.stud;

import java.util.ArrayList;

public class StateHolder {
    private double alpha = 0.1;
    private double b = 1;
    private int counter = 0;
    private int maxCounter = 15;
    private ArrayList<Boolean> sent = new ArrayList<>(10);
    private ArrayList<Double> values = new ArrayList<>(10);
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

    public boolean sentAgent(int id) {
        return sent.get(id);
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
