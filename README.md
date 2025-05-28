# 🤖 Robot Vacuum Simulator

---

Welcome to the **Robot Vacuum Simulator**! This project, developed in Python, is a robust simulation of next-generation autonomous robot vacuums designed to clean complex environments. Starting from basic movement and cleaning, the simulator evolves to manage multiple cleaning agents (dirt, water, mud, soap), navigate various obstructions (walls, cats, other robots), and execute a sequence of coordinated commands for an entire fleet of vacuums.

This project demonstrates a strong understanding of state management, object interaction, file I/O, and complex logical decision-making within a simulated environment. It's the culmination of several progressive tasks, each adding layers of complexity and functionality.

---

## 📋 Table of Contents

* [🌟 Features](#-features)
* [🛠️ Technologies Used](#️-technologies-used)
* [🚀 Getting Started](#-getting-started)
    * [Prerequisites](#prerequisites)
    * [Installation](#installation)
    * [How to Run](#how-to-run)
* [💡 Example Usage](#-example-usage)
* [🧠 Project Evolution & Logic](#-project-evolution--logic)
* [🤝 Contributing](#-contributing)
* [📄 License](#-license)
* [📞 Contact](#-contact)

---

## 🌟 Features

* **Grid-Based Environment:** Simulates a 2D `cleaning_space` (10x10 grid) representing areas to be cleaned and `obstruction_space` for static and dynamic obstacles.
* **Diverse Cleaning States:** Handles various floor conditions: `None` (clean), `"d"` (dirt), `"l"` (water), `"m"` (mud), and `"s"` (soap).
* **Sophisticated Robot Actions:** Supports a range of actions:
    * `turn-left`, `turn-right`: Adjusts robot's facing (8 compass directions).
    * `clean`: Removes dirt (`"d"`) from the current location.
    * `mop`: Removes water (`"l"`) from the current location.
    * `forward`: Complex movement logic including:
        * Standard one-step movement.
        * **Smearing:** Spreads dirt or mud into new locations.
        * **Slipping:** Vacuums on water or soap move two steps, affecting skipped locations.
* **Dynamic Obstacle Handling:**
    * **Walls (`"w"`):** Robots turn right if they would collide.
    * **Cats (`"c"`):** Cats attempt to move out of the way; robots turn right if collision is imminent.
    * **Other Robots (`"r"`):** Robots turn left if they would collide with another robot.
* **Boundary Awareness:** Robots gracefully handle attempts to move outside the grid by performing a `turn-right` action.
* **Multi-Robot Coordination:** Manages a fleet of multiple robot vacuums simultaneously, processing sequential commands for different robots.
* **Action Logging:** Records the actual actions performed by each robot in a dedicated log file, providing a detailed audit trail of their movements and cleaning operations.
* **Configurable Initial State:** Easily set up different `cleaning_space` and `obstruction_space` configurations, as well as initial vacuum positions, for varied simulation scenarios.

---

## 🛠️ Technologies Used

* **Python 3:** The primary language for the simulation logic.

---

## 🚀 Getting Started

These instructions will get you a copy of the project up and running on your local machine for demonstration and testing.

### Prerequisites

You'll need Python 3 installed on your system. If you don't have it, you can download it from [python.org](https://www.python.org/downloads/).

### Installation

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/suveer-dhawan/robot-vacuum-simulator.git
    ```

2.  **Navigate into the project directory:**

    ```bash
    cd robot-vacuum-simulator
    ```

### How to Run

The simulation runs by executing the main `vacuum_simulation.py` script. You'll need an `instructions` file (e.g., `test_commands.txt` provided in the repository) and a list of vacuum initial states and desired log file paths.

```bash
python vacuum_simulation.py
```

The `if __name__ == "__main__":` block at the end of `vacuum_simulation.py` demonstrates how to set up the **cleaning_space**, **obstruction_space**, **vacuums** list, and **logs** list, and then calls `perform_cleaning` to start the simulation. You can modify these initial conditions to test different scenarios.

---

## 💡 Example Usage

The `test_commands.txt` file illustrates how instructions are structured for multiple robots. Each line specifies a robot index and a comma-separated list of actions. Actions for one robot on a line are completed before any actions on the next line begin.

**`test_commands.txt` example:**

```bash
0 forward,clean,turn-right,turn-right,turn-right
1 forward,clean,turn-right,turn-right,turn-right,turn-right,forward
```

After running the simulation, log files (e.g., `log_0.txt`, `log_1.txt`) will be created in the project directory, detailing the actions performed by each robot.

---

## 🧠 Project Evolution & Logic

This project was developed incrementally, with each "Task" building upon the last, adding more realistic and complex behaviors to the robot vacuums and their environment:

* **Task 3 (Robot Revolution):** Established the fundamental movement, basic cleaning (`True`/`False` for dirty/clean), and boundary handling. Introduced the concept of smearing dirt.
* **Task 4 (Unexpected Obstruction):** Introduced a separate `obstruction_space` grid for static (`"w"` for wall) and dynamic (`"c"` for cat, `"r"` for robot) obstacles. Added logging of actual actions performed.
* **Task 5 (Sticky Business):** Significantly expanded the `cleaning_space` to include various types of "dirt" (`"d"`, `"l"`, `"m"` for dirt, water, mud). Introduced specialized actions like `mop` and complex `forward` behaviors (slipping on water, varying smear effects).
* **Task 6 (Scrub a' Dub Dub - *Current Implementation*):** The final stage, integrating all previous features. Added **soap (`"s"`)** as a new cleaning state with unique slipping and cleaning properties. Most importantly, it enabled **multi-robot simulation** with coordinated instruction processing and inter-robot collision detection.

The `vacuum_action` function, at its core, orchestrates the complex interaction logic between the robot's state, the type of surface it's on, and any potential obstructions, returning the **actual action taken**. The `perform_cleaning` function then manages the instruction parsing and sequential execution for potentially multiple robots, ensuring proper logging.

---

## 🤝 Contributing

While this project was part of a university assignment, feel free to open issues if you notice any bugs or have suggestions for improvements or extensions.

---

## 📄 License

This project is open-source and available under the [MIT License](https://opensource.org/licenses/MIT).

---

## 📞 Contact

Have questions or want to connect? You can reach me at:

[Suveer Dhawan](https://github.com/suveer-dhawan)
