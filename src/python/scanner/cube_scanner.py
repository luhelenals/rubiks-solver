"""
Rubik's Cube Scanner using OpenCV for color detection.
"""
import cv2
import numpy as np
from typing import List, Dict, Tuple, Optional


class CubeScanner:
    """Scans a Rubik's cube using a camera and detects the state of each face."""
    
    # Color ranges in HSV space for each face color
    COLOR_RANGES = {
        'white': ([0, 0, 168], [180, 30, 255]),
        'yellow': ([20, 100, 100], [30, 255, 255]),
        'red': ([0, 100, 100], [10, 255, 255]),
        'orange': ([10, 100, 100], [20, 255, 255]),
        'blue': ([100, 100, 100], [130, 255, 255]),
        'green': ([40, 100, 100], [80, 255, 255])
    }
    
    FACE_NAMES = ['U', 'D', 'F', 'B', 'L', 'R']  # Up, Down, Front, Back, Left, Right
    
    def __init__(self, camera_id: int = 0):
        """
        Initialize the cube scanner.
        
        Args:
            camera_id: Camera device ID (default 0 for primary camera)
        """
        self.camera_id = camera_id
        self.cube_state = {face: [[None]*3 for _ in range(3)] for face in self.FACE_NAMES}
        self.current_face_index = 0
        
    def start_scanning(self) -> Dict[str, List[List[str]]]:
        """
        Start the scanning process to capture all 6 faces of the cube.
        
        Returns:
            Dictionary mapping face names to 3x3 color grids
        """
        cap = cv2.VideoCapture(self.camera_id)
        
        if not cap.isOpened():
            raise RuntimeError("Cannot open camera")
        
        print("Rubik's Cube Scanner")
        print("=" * 50)
        print("Instructions:")
        print("- Show each face of the cube to the camera")
        print("- Press SPACE to capture current face")
        print("- Press ESC to cancel")
        print("=" * 50)
        
        while self.current_face_index < len(self.FACE_NAMES):
            ret, frame = cap.read()
            if not ret:
                break
            
            # Process and display frame
            processed_frame = self._process_frame(frame)
            
            # Display current face being scanned
            face_name = self.FACE_NAMES[self.current_face_index]
            cv2.putText(processed_frame, f"Scanning face: {face_name} ({self.current_face_index + 1}/6)",
                       (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
            cv2.putText(processed_frame, "Press SPACE to capture", 
                       (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
            
            cv2.imshow('Rubik\'s Cube Scanner', processed_frame)
            
            key = cv2.waitKey(1) & 0xFF
            if key == 27:  # ESC
                print("Scanning cancelled")
                break
            elif key == 32:  # SPACE
                colors = self._detect_face_colors(frame)
                if colors:
                    self.cube_state[face_name] = colors
                    print(f"Face {face_name} captured: {colors}")
                    self.current_face_index += 1
        
        cap.release()
        cv2.destroyAllWindows()
        
        return self.cube_state
    
    def _process_frame(self, frame: np.ndarray) -> np.ndarray:
        """
        Process frame to show detection grid overlay.
        
        Args:
            frame: Input camera frame
            
        Returns:
            Processed frame with overlay
        """
        height, width = frame.shape[:2]
        center_x, center_y = width // 2, height // 2
        
        # Draw 3x3 grid for cube face detection
        grid_size = min(width, height) // 3
        offset = grid_size // 2
        
        for i in range(3):
            for j in range(3):
                x = center_x - offset + (i - 1) * (grid_size // 3)
                y = center_y - offset + (j - 1) * (grid_size // 3)
                cv2.rectangle(frame, (x, y), (x + grid_size // 3, y + grid_size // 3), 
                             (0, 255, 0), 2)
        
        return frame
    
    def _detect_face_colors(self, frame: np.ndarray) -> Optional[List[List[str]]]:
        """
        Detect colors of the 9 stickers on current cube face.
        
        Args:
            frame: Camera frame showing cube face
            
        Returns:
            3x3 grid of color names, or None if detection failed
        """
        height, width = frame.shape[:2]
        center_x, center_y = width // 2, height // 2
        
        hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        colors = [[None]*3 for _ in range(3)]
        
        grid_size = min(width, height) // 3
        offset = grid_size // 2
        
        for i in range(3):
            for j in range(3):
                x = center_x - offset + (i - 1) * (grid_size // 3) + grid_size // 6
                y = center_y - offset + (j - 1) * (grid_size // 3) + grid_size // 6
                
                # Sample small region around center of each sticker
                sample_region = hsv_frame[max(0, y-10):min(height, y+10), 
                                         max(0, x-10):min(width, x+10)]
                
                if sample_region.size > 0:
                    avg_color = np.mean(sample_region, axis=(0, 1))
                    detected_color = self._identify_color(avg_color)
                    colors[j][i] = detected_color
        
        return colors if all(all(row) for row in colors) else None
    
    def _identify_color(self, hsv_color: np.ndarray) -> str:
        """
        Identify the cube color from HSV value.
        
        Args:
            hsv_color: HSV color value
            
        Returns:
            Color name (white, yellow, red, orange, blue, green)
        """
        for color_name, (lower, upper) in self.COLOR_RANGES.items():
            lower_bound = np.array(lower)
            upper_bound = np.array(upper)
            
            if np.all(hsv_color >= lower_bound) and np.all(hsv_color <= upper_bound):
                return color_name
        
        # Default to white if no match
        return 'white'
    
    def get_cube_state(self) -> Dict[str, List[List[str]]]:
        """
        Get the current state of the scanned cube.
        
        Returns:
            Dictionary mapping face names to 3x3 color grids
        """
        return self.cube_state
    
    def validate_cube_state(self) -> Tuple[bool, str]:
        """
        Validate that the scanned cube state is valid.
        
        Returns:
            Tuple of (is_valid, error_message)
        """
        # Check that we have all 6 faces
        if not all(self.cube_state[face] for face in self.FACE_NAMES):
            return False, "Not all faces have been scanned"
        
        # Count colors - should be 9 of each
        color_counts = {}
        for face in self.FACE_NAMES:
            for row in self.cube_state[face]:
                for color in row:
                    color_counts[color] = color_counts.get(color, 0) + 1
        
        if len(color_counts) != 6:
            return False, f"Expected 6 colors, found {len(color_counts)}"
        
        for color, count in color_counts.items():
            if count != 9:
                return False, f"Color {color} appears {count} times, expected 9"
        
        return True, "Cube state is valid"
