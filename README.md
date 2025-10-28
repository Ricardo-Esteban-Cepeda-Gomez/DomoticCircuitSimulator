# Domotic Circuit Simulator

## Workshop 1 — Conceptual Design and Mockups

This document is part of the **Domotic Circuit Simulator** project and corresponds to **Workshop 1** of the Object-Oriented Programming course.  
Its purpose is to present the **conceptual design**, **interface mockups**, and **initial class structure** that will guide the future development of the simulator.

---

### Summary of the Design

#### Functional Highlights
- Library of **electronic and domotic components**.  
- **Drag-and-drop workspace** to build and connect circuits.  
- **Simulation** of voltage and current.  
- Ability to **edit component properties**.  
- **Import/export** circuits using specific file extensions.  
- **Visual feedback** for simulation results.  

#### Non-Functional Goals
- Intuitive and accessible interface.  
- Consistent colors and a coherent visual identity.  

---

### User Interface Mockups

All interface mockups were designed using **Penpot** to visualize the core screens of the simulator.  

| Page | Description |
|------|--------------|
| **Main Page** | Displays all components and the main toolbar. |
| **Probes / Sensors / Motors / Screens / Microcontrollers** | Allows users to select type, orientation, and parameters for each component. |
| **Resistors / Capacitors / Diodes / Sources / Switches / Transistors** | Pages to adjust electrical parameters (resistance, voltage, polarity, etc.). |
| **Circuit Page** | Example of a complete circuit with *Run/Stop* simulation controls. |

> The mockups maintain a visual style similar to *Crocodile Clips*

---

### CRC Cards Overview

| **Class** | **Responsibilities** | **Collaborators** |
|------------|----------------------|--------------------|
| **Component** | Stores type, value, and state; updates its visual and logical behavior. | Workspace, Simulator |
| **Workspace** | Manages all components, user actions (drag, connect, delete), and rendering. | Component, Simulator, Interface |
| **Simulator** | Calculates circuit behavior and manages simulation flow. | Workspace, Component, Interface |
| **Interface** | Handles UI elements and user commands. | Workspace, Simulator, FileManager |
| **FileManager** | Manages saving and loading of project files (.bsm). | Workspace, Interface |
| **Toolbar** | Contains tools and detects selected actions. | Interface, Workspace, Simulator |
| **StatusBar** | Displays simulation messages and status. | Interface, Simulator |

---

### Tools and References

- **Design Tool:** [Penpot](https://penpot.app)  
- **Inspiration:** [Crocodile Clips](https://en.wikipedia.org/wiki/Crocodile_Clips)  
- **Main Repository:** [Domotic Circuit Simulator – GitHub](https://github.com/Ricardo-Esteban-Cepeda-Gomez/DomoticCircuitSimulator)
