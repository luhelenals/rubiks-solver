# System Architecture Diagram

## High-Level System Flow

The Rubik's Cube Solver follows a three-phase workflow:
1. **Scanning Phase**: Capture cube state using camera
2. **Solving Phase**: Calculate solution using algorithm
3. **Presentation Phase**: Guide user through solution

## Component Architecture

```
main.py (Entry Point)
    │
    └─→ CubeInterface (Orchestrator)
            │
            ├─→ CubeScanner (OpenCV)
            │     └─→ Color detection via HSV
            │
            ├─→ CubeSolver (Algorithm)
            │     └─→ Layer-by-Layer method
            │
            └─→ RendererBridge (Optional)
                  └─→ C++ OpenGL renderer
```

## Data Flow

```
Camera → HSV Analysis → Cube State Dict → Solver → Solution Steps → User Interface
```

See PROJECT_SUMMARY.md for detailed architecture information.
