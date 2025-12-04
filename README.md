# Workshop No. 3 — Applying SOLID Principles to a Domotic Circuit Simulator

### Universidad Nacional de Colombia  
**Object-Oriented Programming — Eng. Carlos Andrés Sierra Virgüez**  
**Authors:** Ricardo Esteban Cepeda Gómez, Johan Sebastian Liévano García, Sebastián Vanegas Ariza  
**Date:** November 25, 2025

---

## 📘 Overview

This workshop focused on refactoring and extending a **Domotic Circuit Simulator** using the **SOLID principles** of object-oriented design.  
The goal was to improve modularity, organization, extensibility, and maintainability while preserving the existing functionality of the simulator.

The project includes components such as sensors, actuators, power sources, a workspace UI, a simulator engine, and file management utilities.

---

## 🧩 SOLID Principles Applied

### **S — Single Responsibility Principle (SRP)**
Each class now has only one responsibility.  
In the simulator this meant separating **simulation logic** from **visual representation**, preventing classes from handling unrelated concerns like rendering, saving, or UI interaction.

---

### **O — Open/Closed Principle (OCP)**
Classes are open for extension but closed for modification.  
The simulator allows adding new components (e.g., new sensors or actuators) **without altering existing code**, thanks to abstract base classes and clear inheritance structures.

---

### **L — Liskov Substitution Principle (LSP)**
Subclasses must be replaceable by their base class.  
For example, different types of power sources (AC/DC) behave consistently when substituted, safely providing voltage and current through shared interfaces.

---

### **I — Interface Segregation Principle (ISP)**
Classes depend only on the methods they actually need.  
Component functionality was divided so that no class is forced to implement unrelated behavior.  
Every component follows focused interfaces with clear responsibilities.

---

### **D — Dependency Inversion Principle (DIP)**
High-level modules depend on **abstractions**, not concrete implementations.  
The simulator engine interacts with components, the workspace, and UI modules through abstract definitions, making the architecture flexible and reusable.

---

## 🗂️ Updated UML and CRC Cards

The project includes updated diagrams and role cards for:

- **Components** — store type, state, and handle simulation behavior and rendering  
- **Workspace** — manages all components, positions, user actions, and connections  
- **Simulator** — runs/pause simulation and updates visual feedback  
- **FileManager** — save/load project files (`.bsm`) and workspace data  
- **Toolbar** — tool selection and component creation interface  
- **StatusBar** — displays messages and simulation state  
- Additional component types such as:
  - Alarm  
  - Resistor  
  - LED  
  - Motor  
  - Sensor  
  - Transistor  
  - Source  
  - Probe  
  - Screen  
  - Switch  

---

## 🧪 Python Code Snippets

The workshop includes modular code implementations for each major element of the simulator:

- `Component` (abstract base class)  
- Electrical components (LED, Motor, Resistor, Transistor, Switch, Sensor…)  
- `Source` (power source)  
- `Simulator` (logic engine)  
- `Workspace` (manages connections and drawing)  
- `FileManager`  
- `StatusBar`  
- `Toolbar`  

These classes apply SOLID principles through inheritance, composition, and clear abstractions.

---

## 📝 Reflection

Applying SOLID principles proved challenging but extremely valuable.  
Initially, multiple classes performed unrelated tasks, making the system rigid and difficult to scale.  
Through refactoring and abstraction:

- Code became cleaner and easier to understand  
- New components could be added without modifying existing classes  
- Dependencies were reduced and reused more effectively  
- We learned how essential software design is, beyond simply writing functional code  

The workshop strengthened our understanding of creating **sustainable**, **scalable**, and **maintainable** object-oriented systems.

---

## 🔗 Repository

GitHub Repository:  
https://github.com/Ricardo-Esteban-Cepeda-Gomez/DomoticCircuitSimulator

---

## 📚 Contents

- Workshop No. 3 — Applying SOLID Principles to a Domotic Circuit Simulator  
- SOLID Principles Analysis  
- Updated UML and CRC Cards  
- Python Code Snippets  
- Reflection  
- Submission Format  