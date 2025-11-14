"""Tests for the cube scanner module."""
import pytest
from src.python.scanner import CubeScanner


class TestCubeScanner:
    """Test cases for CubeScanner class."""
    
    def test_scanner_initialization(self):
        """Test that scanner initializes correctly."""
        scanner = CubeScanner(camera_id=0)
        assert scanner.camera_id == 0
        assert len(scanner.cube_state) == 6
        assert scanner.current_face_index == 0
    
    def test_color_identification(self):
        """Test color identification from HSV values."""
        scanner = CubeScanner()
        
        # Test white detection (high value, low saturation)
        import numpy as np
        white_hsv = np.array([0, 10, 250])
        color = scanner._identify_color(white_hsv)
        assert color == 'white'
        
    def test_valid_cube_state(self):
        """Test validation of a valid cube state."""
        scanner = CubeScanner()
        scanner.cube_state = {
            'U': [['white']*3 for _ in range(3)],
            'D': [['yellow']*3 for _ in range(3)],
            'F': [['red']*3 for _ in range(3)],
            'B': [['orange']*3 for _ in range(3)],
            'L': [['blue']*3 for _ in range(3)],
            'R': [['green']*3 for _ in range(3)]
        }
        
        is_valid, message = scanner.validate_cube_state()
        assert is_valid is True
        assert "valid" in message.lower()
    
    def test_invalid_cube_state_missing_colors(self):
        """Test validation catches missing colors."""
        scanner = CubeScanner()
        scanner.cube_state = {
            'U': [['white']*3 for _ in range(3)],
            'D': [['white']*3 for _ in range(3)],  # Should be yellow
            'F': [['red']*3 for _ in range(3)],
            'B': [['orange']*3 for _ in range(3)],
            'L': [['blue']*3 for _ in range(3)],
            'R': [['green']*3 for _ in range(3)]
        }
        
        is_valid, message = scanner.validate_cube_state()
        assert is_valid is False
    
    def test_invalid_cube_state_wrong_count(self):
        """Test validation catches wrong color counts."""
        scanner = CubeScanner()
        scanner.cube_state = {
            'U': [['white']*3 for _ in range(3)],
            'D': [['yellow']*3 for _ in range(2)],  # Only 6 yellows
            'F': [['red']*3 for _ in range(3)],
            'B': [['orange']*3 for _ in range(3)],
            'L': [['blue']*3 for _ in range(3)],
            'R': [['green']*3 for _ in range(3)]
        }
        
        # Manually complete the D face with wrong color
        scanner.cube_state['D'].append(['white']*3)
        
        is_valid, message = scanner.validate_cube_state()
        assert is_valid is False
        assert "appears" in message.lower()
