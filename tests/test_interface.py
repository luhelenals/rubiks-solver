"""Tests for the interface module."""
import pytest
from src.python.interface import CubeInterface


class TestCubeInterface:
    """Test cases for CubeInterface class."""
    
    def test_interface_initialization(self):
        """Test that interface initializes correctly."""
        interface = CubeInterface(camera_id=1)
        
        assert interface.camera_id == 1
        assert interface.scanner is None
        assert interface.solver is None
        assert interface.cube_state is None
        assert interface.solution_steps is None
        assert interface.current_step == 0
    
    def test_solve_without_scan(self):
        """Test that solve fails without scanning first."""
        interface = CubeInterface()
        result = interface.solve_cube()
        
        assert result is False
    
    def test_solve_with_cube_state(self):
        """Test solving with a valid cube state."""
        interface = CubeInterface()
        interface.cube_state = self._create_test_cube()
        
        result = interface.solve_cube()
        
        assert result is True
        assert interface.solver is not None
        assert interface.solution_steps is not None
        assert len(interface.solution_steps) > 0
    
    def test_get_step(self):
        """Test getting a specific solution step."""
        interface = CubeInterface()
        interface.cube_state = self._create_test_cube()
        interface.solve_cube()
        
        step = interface.get_step(0)
        assert step is not None
        
        description, moves, result = step
        assert isinstance(description, str)
        assert isinstance(moves, list)
        assert isinstance(result, str)
    
    def test_get_step_invalid_index(self):
        """Test getting step with invalid index."""
        interface = CubeInterface()
        interface.cube_state = self._create_test_cube()
        interface.solve_cube()
        
        step = interface.get_step(-1)
        assert step is None
        
        step = interface.get_step(999)
        assert step is None
    
    def test_export_solution(self, tmp_path):
        """Test exporting solution to JSON."""
        interface = CubeInterface()
        interface.cube_state = self._create_test_cube()
        interface.solve_cube()
        
        output_file = tmp_path / "test_solution.json"
        interface.export_solution(str(output_file))
        
        assert output_file.exists()
        
        # Verify JSON content
        import json
        with open(output_file, 'r') as f:
            data = json.load(f)
        
        assert 'cube_state' in data
        assert 'solution_steps' in data
        assert len(data['solution_steps']) > 0
    
    @staticmethod
    def _create_test_cube():
        """Create a test cube state."""
        return {
            'U': [['white']*3 for _ in range(3)],
            'D': [['yellow']*3 for _ in range(3)],
            'F': [['red']*3 for _ in range(3)],
            'B': [['orange']*3 for _ in range(3)],
            'L': [['blue']*3 for _ in range(3)],
            'R': [['green']*3 for _ in range(3)]
        }
