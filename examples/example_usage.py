#!/usr/bin/env python3
"""
Example usage of the Rubik's Cube Solver modules.
"""
import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.python.scanner import CubeScanner
from src.python.solver import CubeSolver, Move
from src.python.interface import CubeInterface


def example_basic_workflow():
    """Example: Complete workflow with test data."""
    print("Example: Basic Workflow")
    print("=" * 60)
    
    # Create test cube state
    test_state = {
        'U': [['white', 'white', 'white'], ['white', 'white', 'white'], ['white', 'white', 'white']],
        'D': [['yellow', 'yellow', 'yellow'], ['yellow', 'yellow', 'yellow'], ['yellow', 'yellow', 'yellow']],
        'F': [['red', 'red', 'red'], ['red', 'red', 'red'], ['red', 'red', 'red']],
        'B': [['orange', 'orange', 'orange'], ['orange', 'orange', 'orange'], ['orange', 'orange', 'orange']],
        'L': [['blue', 'blue', 'blue'], ['blue', 'blue', 'blue'], ['blue', 'blue', 'blue']],
        'R': [['green', 'green', 'green'], ['green', 'green', 'green'], ['green', 'green', 'green']]
    }
    
    # Create solver
    solver = CubeSolver(test_state)
    
    # Generate solution
    solution_steps = solver.solve()
    
    # Print solution
    print(f"\nGenerated {len(solution_steps)} solution steps:")
    for i, (description, moves, result) in enumerate(solution_steps, 1):
        print(f"\n{i}. {description}")
        print(f"   Moves: {' '.join(str(m) for m in moves)}")
        print(f"   Result: {result}")


def example_move_notation():
    """Example: Working with cube moves."""
    print("\n\nExample: Move Notation")
    print("=" * 60)
    
    # Create different types of moves
    moves = [
        Move('U', 'CW'),      # U
        Move('R', 'CCW'),     # R'
        Move('F', '2'),       # F2
        Move('D', 'CW'),      # D
    ]
    
    print("\nMove sequence:")
    for move in moves:
        print(f"  {move} - Face: {move.face}, Direction: {move.direction}")
    
    print(f"\nAs string: {' '.join(str(m) for m in moves)}")


def example_scanner_validation():
    """Example: Validating cube state."""
    print("\n\nExample: Scanner Validation")
    print("=" * 60)
    
    # Valid cube state
    valid_state = {
        'U': [['white']*3 for _ in range(3)],
        'D': [['yellow']*3 for _ in range(3)],
        'F': [['red']*3 for _ in range(3)],
        'B': [['orange']*3 for _ in range(3)],
        'L': [['blue']*3 for _ in range(3)],
        'R': [['green']*3 for _ in range(3)]
    }
    
    scanner = CubeScanner()
    scanner.cube_state = valid_state
    
    is_valid, message = scanner.validate_cube_state()
    print(f"\nValid cube state: {is_valid}")
    print(f"Message: {message}")
    
    # Invalid cube state (missing colors)
    invalid_state = {
        'U': [['white']*3 for _ in range(3)],
        'D': [['white']*3 for _ in range(3)],  # Wrong!
        'F': [['red']*3 for _ in range(3)],
        'B': [['orange']*3 for _ in range(3)],
        'L': [['blue']*3 for _ in range(3)],
        'R': [['green']*3 for _ in range(3)]
    }
    
    scanner.cube_state = invalid_state
    is_valid, message = scanner.validate_cube_state()
    print(f"\nInvalid cube state: {is_valid}")
    print(f"Message: {message}")


def example_solution_export():
    """Example: Exporting solution to JSON."""
    print("\n\nExample: Solution Export")
    print("=" * 60)
    
    # Create interface with test data
    interface = CubeInterface()
    interface.cube_state = {
        'U': [['white']*3 for _ in range(3)],
        'D': [['yellow']*3 for _ in range(3)],
        'F': [['red']*3 for _ in range(3)],
        'B': [['orange']*3 for _ in range(3)],
        'L': [['blue']*3 for _ in range(3)],
        'R': [['green']*3 for _ in range(3)]
    }
    
    # Solve
    interface.solve_cube()
    
    # Export
    interface.export_solution('/tmp/example_solution.json')
    print("\nSolution exported to /tmp/example_solution.json")


if __name__ == '__main__':
    example_basic_workflow()
    example_move_notation()
    example_scanner_validation()
    example_solution_export()
    
    print("\n\n" + "=" * 60)
    print("Examples completed!")
    print("=" * 60)
