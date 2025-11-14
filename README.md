# Rubik's Cube Solver

A comprehensive Rubik's cube solver that uses computer vision to scan an arbitrary cube and provides step-by-step guidance on how to solve it.

## Features

- **Camera Scanning**: Show your cube to the camera and let it detect the state of each face
- **Step-by-Step Guide**: Get detailed instructions on which movements to make to solve the cube
- **3D Visualization**: View how the cube should look before and after each step (C++/OpenGL renderer)
- **Interactive Interface**: Manipulate and explore the solution at your own pace

## Technology Stack

- **Computer Vision & Algorithm**: Python with OpenCV
- **3D Rendering**: C++/OpenGL (structural implementation provided)
- **Architecture**: Modular design with clear separation between CV, solving logic, and rendering

## Installation

### Prerequisites

- Python 3.8 or higher
- OpenCV
- NumPy
- (Optional) CMake and OpenGL for C++ renderer

### Install Python Dependencies

```bash
pip install -r requirements.txt
```

Or install the package:

```bash
pip install -e .
```

### Build C++ Renderer (Optional)

```bash
cd src/cpp
mkdir build
cd build
cmake ..
make
```

## Usage

### Basic Usage

Run the complete workflow (scan, solve, and guide):

```bash
python main.py
```

### Using Test Data

Skip scanning and use a test cube state:

```bash
python main.py --no-scan
```

### Export Solution

Export the solution to a JSON file:

```bash
python main.py --no-scan --export solution.json
```

### Specify Camera

Use a specific camera device:

```bash
python main.py --camera 1
```

## How It Works

### 1. Scanning Phase

The application opens your camera and guides you through scanning all 6 faces of the cube:

- Show each face to the camera
- A 3x3 grid overlay helps you align the cube
- Press SPACE to capture each face
- The system detects colors using HSV color space analysis

### 2. Solving Phase

The solver analyzes the cube state and generates a solution using the Layer-by-Layer (Beginner's) method:

1. White cross on top
2. White corners
3. Middle layer edges
4. Yellow cross on bottom
5. Orient yellow corners
6. Position yellow corners
7. Position yellow edges

### 3. Interactive Guide

Follow the step-by-step instructions:

- View each step with the moves you need to perform
- Navigate forward/backward through steps
- See expected results after each step
- Export solution for later reference

## Project Structure

```
rubiks-solver/
├── src/
│   ├── python/
│   │   ├── scanner/          # Camera scanning and color detection
│   │   │   └── cube_scanner.py
│   │   ├── solver/           # Cube solving algorithms
│   │   │   └── cube_solver.py
│   │   ├── interface/        # Main application interface
│   │   │   └── cube_interface.py
│   │   └── renderer_bridge.py # Python-C++ bridge
│   └── cpp/
│       └── renderer/         # OpenGL 3D renderer
│           ├── cube_renderer.h
│           └── cube_renderer.cpp
├── tests/                    # Test files
├── examples/                 # Example cube states
├── config/                   # Configuration files
├── main.py                   # Main entry point
├── requirements.txt          # Python dependencies
└── setup.py                  # Package setup
```

## Module Documentation

### Scanner Module

**CubeScanner** (`src/python/scanner/cube_scanner.py`)
- Captures cube state using camera
- Detects colors using HSV color ranges
- Validates cube state (9 of each color)
- Provides real-time visual feedback with grid overlay

### Solver Module

**CubeSolver** (`src/python/solver/cube_solver.py`)
- Implements Layer-by-Layer solving method
- Generates step-by-step move sequences
- Returns human-readable instructions
- Tracks cube state through solution

### Interface Module

**CubeInterface** (`src/python/interface/cube_interface.py`)
- Coordinates scanner and solver
- Provides interactive command-line interface
- Manages solution navigation
- Exports solutions to JSON

### Renderer Module

**CubeRenderer** (`src/cpp/renderer/cube_renderer.cpp`)
- OpenGL-based 3D visualization
- Renders cube with proper colors
- Camera controls (rotation, zoom)
- Shows cube state before/after moves

## Notation

The solver uses standard Rubik's cube notation:

- **U** = Up face (clockwise)
- **U'** = Up face (counter-clockwise)
- **U2** = Up face (180 degrees)
- **D** = Down face
- **F** = Front face
- **B** = Back face
- **L** = Left face
- **R** = Right face

## Development

### Running Tests

```bash
python -m pytest tests/
```

### Adding New Solving Algorithms

Extend the `CubeSolver` class in `src/python/solver/cube_solver.py` to implement additional algorithms like CFOP, Roux, or ZZ method.

### Improving Color Detection

Adjust HSV color ranges in `CubeScanner.COLOR_RANGES` to improve detection accuracy for different lighting conditions.

## Future Enhancements

- Advanced solving algorithms (CFOP, Roux)
- Real-time 3D visualization during solving
- Pattern detection and recognition
- Mobile app version
- Augmented reality overlay
- Web-based interface

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

MIT License - see LICENSE file for details

## Acknowledgments

- OpenCV community for computer vision tools
- Rubik's cube solving community for algorithm documentation
- OpenGL for 3D graphics capabilities
