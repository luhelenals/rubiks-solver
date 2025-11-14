"""
Main interface for the Rubik's Cube Solver application.
Coordinates between scanner, solver, and renderer.
"""
import sys
import json
from typing import List, Dict, Optional
from ..scanner import CubeScanner
from ..solver import CubeSolver, Move


class CubeInterface:
    """Main interface for the Rubik's cube solver application."""
    
    def __init__(self, camera_id: int = 0):
        """
        Initialize the cube interface.
        
        Args:
            camera_id: Camera device ID
        """
        self.camera_id = camera_id
        self.scanner = None
        self.solver = None
        self.cube_state = None
        self.solution_steps = None
        self.current_step = 0
        
    def scan_cube(self) -> bool:
        """
        Start the cube scanning process.
        
        Returns:
            True if scanning successful, False otherwise
        """
        try:
            self.scanner = CubeScanner(self.camera_id)
            print("\n" + "="*60)
            print("SCANNING MODE")
            print("="*60)
            
            self.cube_state = self.scanner.start_scanning()
            
            # Validate cube state
            is_valid, message = self.scanner.validate_cube_state()
            if not is_valid:
                print(f"Error: {message}")
                return False
            
            print("\n✓ Cube scanned successfully!")
            print(f"✓ Validation: {message}")
            return True
            
        except Exception as e:
            print(f"Error during scanning: {e}")
            return False
    
    def solve_cube(self) -> bool:
        """
        Generate solution for the scanned cube.
        
        Returns:
            True if solution generated, False otherwise
        """
        if not self.cube_state:
            print("Error: No cube has been scanned yet")
            return False
        
        try:
            print("\n" + "="*60)
            print("SOLVING CUBE")
            print("="*60)
            
            self.solver = CubeSolver(self.cube_state)
            self.solution_steps = self.solver.solve()
            
            total_moves = sum(len(moves) for _, moves, _ in self.solution_steps)
            print(f"\n✓ Solution found!")
            print(f"✓ Total steps: {len(self.solution_steps)}")
            print(f"✓ Total moves: {total_moves}")
            
            return True
            
        except Exception as e:
            print(f"Error during solving: {e}")
            return False
    
    def show_solution_summary(self):
        """Display a summary of the solution steps."""
        if not self.solution_steps:
            print("No solution available")
            return
        
        print("\n" + "="*60)
        print("SOLUTION SUMMARY")
        print("="*60)
        
        for i, (description, moves, result) in enumerate(self.solution_steps, 1):
            print(f"\n{i}. {description}")
            print(f"   Moves: {' '.join(str(m) for m in moves)}")
            print(f"   Result: {result}")
    
    def get_step(self, step_number: int) -> Optional[tuple]:
        """
        Get a specific solution step.
        
        Args:
            step_number: Step number (0-indexed)
            
        Returns:
            Tuple of (description, moves, result) or None
        """
        if not self.solution_steps or step_number < 0 or step_number >= len(self.solution_steps):
            return None
        return self.solution_steps[step_number]
    
    def export_solution(self, filename: str):
        """
        Export solution to JSON file.
        
        Args:
            filename: Output filename
        """
        if not self.solution_steps:
            print("No solution to export")
            return
        
        data = {
            'cube_state': self.cube_state,
            'solution_steps': [
                {
                    'step_number': i + 1,
                    'description': desc,
                    'moves': [{'face': m.face, 'direction': m.direction} for m in moves],
                    'expected_result': result
                }
                for i, (desc, moves, result) in enumerate(self.solution_steps)
            ]
        }
        
        with open(filename, 'w') as f:
            json.dump(data, f, indent=2)
        
        print(f"Solution exported to {filename}")
    
    def interactive_guide(self):
        """
        Run an interactive step-by-step guide through the solution.
        """
        if not self.solution_steps:
            print("No solution available. Please scan and solve the cube first.")
            return
        
        print("\n" + "="*60)
        print("INTERACTIVE SOLUTION GUIDE")
        print("="*60)
        print("Commands:")
        print("  n/next    - Go to next step")
        print("  p/prev    - Go to previous step")
        print("  r/repeat  - Show current step again")
        print("  s/summary - Show all steps")
        print("  q/quit    - Exit guide")
        print("="*60)
        
        self.current_step = 0
        
        while True:
            # Show current step
            if 0 <= self.current_step < len(self.solution_steps):
                desc, moves, result = self.solution_steps[self.current_step]
                print(f"\n{'='*60}")
                print(f"Step {self.current_step + 1}/{len(self.solution_steps)}: {desc}")
                print(f"{'='*60}")
                print(f"\nMoves to perform: {' '.join(str(m) for m in moves)}")
                print(f"\nWhat you should see after:")
                print(f"  {result}")
                print(f"\n{'='*60}")
            
            # Get user input
            command = input("\nEnter command: ").strip().lower()
            
            if command in ['q', 'quit']:
                print("Exiting guide.")
                break
            elif command in ['n', 'next']:
                if self.current_step < len(self.solution_steps) - 1:
                    self.current_step += 1
                else:
                    print("✓ You've completed all steps! The cube should be solved.")
            elif command in ['p', 'prev']:
                if self.current_step > 0:
                    self.current_step -= 1
                else:
                    print("Already at first step.")
            elif command in ['r', 'repeat']:
                continue  # Just loop again to show current step
            elif command in ['s', 'summary']:
                self.show_solution_summary()
            else:
                print("Unknown command. Use n/next, p/prev, r/repeat, s/summary, or q/quit")
    
    def run(self):
        """
        Run the complete application workflow.
        """
        print("="*60)
        print("RUBIK'S CUBE SOLVER")
        print("="*60)
        print("\nThis application will:")
        print("1. Scan your Rubik's cube using the camera")
        print("2. Calculate a solution")
        print("3. Guide you through solving it step-by-step")
        print("\nPress Enter to start, or Ctrl+C to exit...")
        
        try:
            input()
        except KeyboardInterrupt:
            print("\nExiting...")
            return
        
        # Step 1: Scan
        if not self.scan_cube():
            print("Failed to scan cube. Exiting.")
            return
        
        # Step 2: Solve
        if not self.solve_cube():
            print("Failed to generate solution. Exiting.")
            return
        
        # Step 3: Show summary
        self.show_solution_summary()
        
        # Step 4: Interactive guide
        print("\n" + "="*60)
        print("Ready to start solving?")
        print("="*60)
        choice = input("Start interactive guide? (y/n): ").strip().lower()
        
        if choice == 'y':
            self.interactive_guide()
        
        # Option to export
        choice = input("\nExport solution to file? (y/n): ").strip().lower()
        if choice == 'y':
            filename = input("Enter filename (default: solution.json): ").strip()
            if not filename:
                filename = "solution.json"
            self.export_solution(filename)
        
        print("\n✓ Thank you for using Rubik's Cube Solver!")
