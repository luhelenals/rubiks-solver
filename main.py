#!/usr/bin/env python3
"""
Main entry point for the Rubik's Cube Solver application.
"""
import sys
import argparse
from src.python.interface import CubeInterface


def main():
    """Main application entry point."""
    parser = argparse.ArgumentParser(
        description="Rubik's Cube Solver with Computer Vision and 3D Visualization"
    )
    parser.add_argument(
        '--camera',
        type=int,
        default=0,
        help='Camera device ID (default: 0)'
    )
    parser.add_argument(
        '--no-scan',
        action='store_true',
        help='Skip scanning and use a test cube state'
    )
    parser.add_argument(
        '--export',
        type=str,
        help='Export solution to JSON file'
    )
    
    args = parser.parse_args()
    
    try:
        # Create interface
        interface = CubeInterface(camera_id=args.camera)
        
        if args.no_scan:
            # Use a test cube state for development
            print("Using test cube state (no scanning)")
            interface.cube_state = create_test_cube_state()
            
            # Solve and show solution
            if interface.solve_cube():
                interface.show_solution_summary()
                
                if args.export:
                    interface.export_solution(args.export)
                else:
                    interface.interactive_guide()
        else:
            # Run full workflow
            interface.run()
            
    except KeyboardInterrupt:
        print("\n\nInterrupted by user. Exiting...")
        sys.exit(0)
    except Exception as e:
        print(f"\nError: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


def create_test_cube_state():
    """
    Create a test cube state for development/testing.
    
    Returns:
        Dictionary with a sample scrambled cube state
    """
    return {
        'U': [['white', 'yellow', 'white'], ['red', 'white', 'blue'], ['white', 'green', 'white']],
        'D': [['yellow', 'white', 'yellow'], ['orange', 'yellow', 'green'], ['yellow', 'red', 'yellow']],
        'F': [['red', 'red', 'blue'], ['white', 'red', 'yellow'], ['red', 'orange', 'red']],
        'B': [['orange', 'blue', 'orange'], ['yellow', 'orange', 'white'], ['orange', 'green', 'orange']],
        'L': [['blue', 'green', 'blue'], ['red', 'blue', 'orange'], ['blue', 'yellow', 'blue']],
        'R': [['green', 'orange', 'green'], ['blue', 'green', 'red'], ['green', 'white', 'green']]
    }


if __name__ == '__main__':
    main()
