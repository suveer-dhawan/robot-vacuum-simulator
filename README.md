# Robot Vacuum Simulator

This is a Python simulation of a robot vacuum cleaner navigating and cleaning a 2D grid. The robot interprets instruction sets like `["turn-left", "turn-right", "clean", "mop", "forward"]`, handles obstructions, and adapts to different types of dirty terrain.

## Features

- Movement based on compass directions 
- Obstruction detection (walls, cats, other vacuums)
- Dirty surface interactions (mud, wet, soapy tiles)
- Multiple vacuum support
- Action logging per robot

## Getting Started

1. Clone the repository:

```bash
git clone https://github.com/suveer-dhawan/robot-vacuum-simulator.git
cd robot-vacuum-simulator