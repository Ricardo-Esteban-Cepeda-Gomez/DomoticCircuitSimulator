### Universidad Nacional de Colombia  
**Object-Oriented Programming — Eng. Carlos Andrés Sierra Virgüez**  
**Authors:** Ricardo Esteban Cepeda Gómez, Johan Sebastian Liévano García, Sebastián Vanegas Ariza  
**Date:** November 25, 2025

---

## User Guide — How to Use the System

### 🚀 Purpose

This guide teaches users how to build circuits, connect components, and run simulations inside the system.

---

## 🖥 Program Interface

On startup, the user sees:

- *Menubar* — software options.
- *Toolbar* — list of available circuit components.
- *Workspace* — area where projects are built.
- *Statusbar* — system execution status.

---

## 🛠 Creating a Circuit

### 1. Adding components

1. Open the *Toolbar*.
2. Choose a component (LED, resistor, switch, etc.).
3. Click inside the *Workspace* to place it.

You may add as many elements as needed.

---

### 2. Wiring components

1. Select *Cable/Wire tool*.
2. Click the output pin of a component.
3. Click the input pin of another component.

A *Source* is required for circuit power.

---

### 3. Running the simulation

1. Click *Run/Start* on the *Statusbar*.
2. Observe component reactions:
   - LED turns ON
   - Alarm activates
   - Capacitor charges/discharges
   - Probe measures values

To modify or stop → press *Pause*.

---

### 4. Saving and loading projects

Menubar → File → Save / Load  
The entire circuit is serialized using pickle.

---

### 5. Quick Examples

| Goal | Basic Setup |
|---|---|
| Turn on a LED | Source → Switch → LED (connected with wires) → Run |
| Trigger alarm | Source → Switch → Alarm → Run |
| Measure current | Place Probe in circuit path |

---

# Technical Documentation — Internal System Functionality

## 1. Technical Documentation — Internal System Functionality

### 📌 Introduction
This system is a platform designed to build and simulate home automation electrical circuits through a graphical user interface.  
It allows users to place electronic components, connect them using wires, and run simulations to observe how the circuit behaves in real time.  
The project is developed using OOP with SOLID principles, ensuring scalability, maintainability, and clean architecture.

---

## 🏗 General Architecture

### � Graphical User Interface (GUI)

The GUI is the main interaction layer for the user. It consists of:

| GUI Component | Description |
|---|---|
| *Menubar* | Top bar containing menu options such as file, view, tools, help, etc. |
| *Toolbar* | Panel with icons to add components into the circuit. |
| *Workspace* | Main area where circuit components are placed and arranged. |
| *Statusbar* | Displays the system state: Running/Paused, alerts, messages. |

---

### 🔌 Circuit Components

The system includes different electrical elements, all inheriting from a base class Component.  
Each component has individual behavior and can interact with others through connections.

Available components:

- Alarm  
- Capacitor  
- LED  
- Probe  
- Resistor  
- Source (power supply)  
- Switch  
- Cables (connection links)

Examples of behaviors:

- *LED* lights up when receiving current.
- *Switch* opens or closes the circuit path.
- *Resistor* limits current flow.
- *Probe* allows data reading inside the circuit.
- *Capacitor* stores and releases energy with time.

---

### 🧠 Controller

The *Controller* manages system functionality and logic flow.  
It acts as the bridge between GUI components and internal logic.

Responsibilities:

- Handle user actions and component creation.
- Manage and store circuit elements within the workspace.
- Communicate changes between visual and logical layers.
- Control simulation events and updates.

---

### 🌀 Simulator

The *Simulator* processes circuit logic and evaluates electrical behavior.

Main functions:

- Iterate through circuit components and propagate energy.
- Update each component state based on input/output.
- Refresh the GUI according to events (like LED ON, alarm active).
- Operates in execution cycles controlled by the Statusbar.

---

### 💾 File Manager (Pickle)

The system uses Python pickle to save and load projects.  
This allows preserving:

- All components placed on the workspace
- Their properties and configuration
- Cable connections and links

Users can stop and resume projects at any time.

---

## 🔄 Internal Workflow

1. The user places components from *Toolbar → Workspace*.
2. The *Controller* registers the component inside the system.
3. *Cables* are used to connect outputs to inputs.
4. User starts simulation — *Simulator* activates.
5. Circuit logic is processed and electricity flows.
6. *Statusbar* updates state changes (Running/Paused).
7. Project can be saved or loaded using *File Manager*.

---

## 🔗 Repository

GitHub Repository:  
https://github.com/Ricardo-Esteban-Cepeda-Gomez/DomoticCircuitSimulator

---

## Recommended Improvements

- Add UML diagrams and interaction flow charts.
- Create a styled PDF version with images.
- Expand component documentation with input/output specification.
- Generate automated README for GitHub.

---

## Team / Credits

- Authors: Ricardo Esteban Cepeda Gómez, Johan Sebastian Liévano García, Sebastián Vanegas Ariza
- Professor: Eng. Carlos Andrés Sierra Virgüez
- Universidad: Universidad Nacional de Colombia

---

*End of file*