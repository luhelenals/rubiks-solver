# Examples

This directory contains example scripts demonstrating how to use the Rubik's Cube Solver.

## Available Examples

### example_usage.py

Demonstrates basic usage of the solver modules:

- Complete workflow with test data
- Working with move notation
- Validating cube states
- Exporting solutions

Run it with:
```bash
python examples/example_usage.py
```

## Creating Your Own Examples

You can create your own cube states and test the solver:

```python
from src.python.solver import CubeSolver

# Define your cube state
my_cube = {
    'U': [['white', 'yellow', 'white'], ...],
    'D': [['yellow', 'white', 'yellow'], ...],
    # ... other faces
}

# Solve it
solver = CubeSolver(my_cube)
solution = solver.solve()

# Print steps
for desc, moves, result in solution:
    print(f"{desc}: {' '.join(str(m) for m in moves)}")
```
