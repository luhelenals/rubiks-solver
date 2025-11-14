# Contributing to Rubik's Cube Solver

Thank you for your interest in contributing to this project!

## How to Contribute

1. **Fork the repository**
2. **Create a feature branch**: `git checkout -b feature/your-feature-name`
3. **Make your changes**
4. **Write/update tests** for your changes
5. **Ensure all tests pass**: `python -m pytest tests/`
6. **Update documentation** as needed
7. **Commit your changes**: `git commit -m "Add your feature"`
8. **Push to your fork**: `git push origin feature/your-feature-name`
9. **Create a Pull Request**

## Development Setup

```bash
# Clone the repository
git clone https://github.com/luhelenals/rubiks-solver.git
cd rubiks-solver

# Install dependencies
pip install -r requirements.txt
pip install pytest

# Run tests
python -m pytest tests/
```

## Code Style

- Follow PEP 8 for Python code
- Use meaningful variable and function names
- Add docstrings to all classes and functions
- Keep functions focused and concise

## Testing

- Write tests for all new functionality
- Ensure existing tests still pass
- Aim for high code coverage
- Test edge cases and error conditions

## Areas for Contribution

### Computer Vision
- Improve color detection accuracy
- Add support for different lighting conditions
- Implement automatic cube orientation detection
- Add augmented reality overlay

### Solving Algorithms
- Implement advanced methods (CFOP, Roux, ZZ)
- Optimize move sequences
- Add pattern recognition
- Implement move count minimization

### 3D Renderer
- Complete OpenGL implementation with GLFW
- Add animation between moves
- Implement interactive cube manipulation
- Add visual effects and themes

### User Interface
- Create GUI using Qt or Tkinter
- Add mobile app support
- Implement web interface
- Add accessibility features

### Documentation
- Add more examples
- Create video tutorials
- Improve API documentation
- Add internationalization

## Reporting Issues

When reporting issues, please include:
- Description of the problem
- Steps to reproduce
- Expected behavior
- Actual behavior
- System information (OS, Python version, etc.)
- Error messages and logs

## Questions?

Feel free to open an issue for any questions or discussions!
