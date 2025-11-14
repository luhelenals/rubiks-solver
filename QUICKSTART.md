# Quick Start Guide

Get started with the Rubik's Cube Solver in just a few minutes!

## Installation

```bash
# Clone the repository
git clone https://github.com/luhelenals/rubiks-solver.git
cd rubiks-solver

# Install Python dependencies
pip install -r requirements.txt
```

## Try It Out (No Camera Required)

The easiest way to see the solver in action is to use the test mode:

```bash
python main.py --no-scan
```

This will:
1. Load a pre-scrambled test cube
2. Calculate a solution
3. Show you a summary of all steps
4. Let you navigate through the solution interactively

### Interactive Commands

When in the interactive guide:
- `n` or `next` - Go to the next step
- `p` or `prev` - Go to the previous step
- `r` or `repeat` - Show the current step again
- `s` or `summary` - Show all steps at once
- `q` or `quit` - Exit the guide

## Using With a Camera

If you have a webcam, you can scan a real cube:

```bash
python main.py
```

Follow the on-screen instructions:
1. Show each face of your cube to the camera
2. Align the cube with the 3x3 grid overlay
3. Press SPACE to capture each face
4. After all 6 faces are scanned, the solver will calculate a solution
5. Follow the step-by-step guide to solve your cube!

### Scanning Tips

- Use good lighting (natural light works best)
- Hold the cube steady
- Ensure all stickers are visible
- The center color identifies each face

## Export Your Solution

Save your solution to a JSON file:

```bash
python main.py --no-scan --export my_solution.json
```

## Run Examples

See how to use the modules programmatically:

```bash
python examples/example_usage.py
```

## Understanding Move Notation

- **U** = Turn the Up (top) face clockwise
- **U'** = Turn the Up face counter-clockwise (prime)
- **U2** = Turn the Up face 180 degrees
- **D** = Down face
- **F** = Front face
- **B** = Back face
- **L** = Left face
- **R** = Right face

Example: `R U R' U'` means:
1. Turn right face clockwise
2. Turn top face clockwise
3. Turn right face counter-clockwise
4. Turn top face counter-clockwise

## Next Steps

- Read the full [README.md](README.md) for detailed documentation
- Check out [examples/](examples/) for code examples
- See [CONTRIBUTING.md](CONTRIBUTING.md) to contribute
- Adjust camera settings in [config/camera_config.json](config/camera_config.json)

## Troubleshooting

### Camera not working?
- Check camera permissions
- Try a different camera with `--camera 1` or `--camera 2`
- Use `--no-scan` mode to test without a camera

### Colors not detecting correctly?
- Improve lighting conditions
- Adjust HSV color ranges in `src/python/scanner/cube_scanner.py`
- Or modify `config/camera_config.json`

### Need help?
Open an issue on GitHub with:
- Your OS and Python version
- Error messages
- Steps to reproduce the problem

Happy solving! 🎲✨
