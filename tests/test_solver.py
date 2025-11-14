"""Tests for the cube solver module."""
import pytest
from src.python.solver import CubeSolver, Move


class TestMove:
    """Test cases for Move class."""
    
    def test_move_string_representation_cw(self):
        """Test clockwise move string representation."""
        move = Move('U', 'CW')
        assert str(move) == 'U'
    
    def test_move_string_representation_ccw(self):
        """Test counter-clockwise move string representation."""
        move = Move('R', 'CCW')
        assert str(move) == "R'"
    
    def test_move_string_representation_180(self):
        """Test 180-degree move string representation."""
        move = Move('F', '2')
        assert str(move) == 'F2'


class TestCubeSolver:
    """Test cases for CubeSolver class."""
    
    def test_solver_initialization(self):
        """Test that solver initializes correctly."""
        test_state = self._create_solved_cube()
        solver = CubeSolver(test_state)
        
        assert solver.initial_state == test_state
        assert solver.current_state == test_state
        assert len(solver.solution_steps) == 0
    
    def test_solve_generates_steps(self):
        """Test that solve generates solution steps."""
        test_state = self._create_solved_cube()
        solver = CubeSolver(test_state)
        
        solution_steps = solver.solve()
        
        assert len(solution_steps) > 0
        assert len(solution_steps) == 7  # Should have 7 steps
        
        # Verify structure of steps
        for step in solution_steps:
            description, moves, result = step
            assert isinstance(description, str)
            assert isinstance(moves, list)
            assert isinstance(result, str)
            assert len(description) > 0
            assert len(result) > 0
    
    def test_get_all_moves(self):
        """Test getting all moves as flat list."""
        test_state = self._create_solved_cube()
        solver = CubeSolver(test_state)
        
        solver.solve()
        all_moves = solver.get_all_moves()
        
        assert len(all_moves) > 0
        assert all(isinstance(m, Move) for m in all_moves)
    
    def test_solution_steps_have_moves(self):
        """Test that each step has moves."""
        test_state = self._create_solved_cube()
        solver = CubeSolver(test_state)
        
        solution_steps = solver.solve()
        
        for description, moves, result in solution_steps:
            assert len(moves) > 0, f"Step '{description}' has no moves"
            assert all(isinstance(m, Move) for m in moves)
    
    def test_get_current_state(self):
        """Test getting current cube state."""
        test_state = self._create_solved_cube()
        solver = CubeSolver(test_state)
        
        current = solver.get_current_state()
        assert current == test_state
    
    @staticmethod
    def _create_solved_cube():
        """Create a solved cube state for testing."""
        return {
            'U': [['white']*3 for _ in range(3)],
            'D': [['yellow']*3 for _ in range(3)],
            'F': [['red']*3 for _ in range(3)],
            'B': [['orange']*3 for _ in range(3)],
            'L': [['blue']*3 for _ in range(3)],
            'R': [['green']*3 for _ in range(3)]
        }
