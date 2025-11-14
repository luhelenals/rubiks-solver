/**
 * @file cube_renderer.h
 * @brief OpenGL renderer for visualizing Rubik's cube state
 */

#ifndef CUBE_RENDERER_H
#define CUBE_RENDERER_H

#include <GL/gl.h>
#include <GL/glu.h>
#include <string>
#include <vector>
#include <map>

namespace rubiks {

/**
 * @brief Color representation for cube faces
 */
struct Color {
    float r, g, b;
    
    Color(float red = 1.0f, float green = 1.0f, float blue = 1.0f) 
        : r(red), g(green), b(blue) {}
};

/**
 * @brief Position and rotation for a single cubelet
 */
struct Cubelet {
    float x, y, z;           // Position
    float rx, ry, rz;        // Rotation angles
    std::vector<Color> faces; // Colors for each visible face
    
    Cubelet(float px = 0.0f, float py = 0.0f, float pz = 0.0f)
        : x(px), y(py), z(pz), rx(0.0f), ry(0.0f), rz(0.0f) {}
};

/**
 * @brief Main renderer class for the Rubik's cube
 */
class CubeRenderer {
public:
    /**
     * @brief Constructor
     */
    CubeRenderer();
    
    /**
     * @brief Destructor
     */
    ~CubeRenderer();
    
    /**
     * @brief Initialize OpenGL and create window
     * @param width Window width
     * @param height Window height
     * @param title Window title
     * @return true if initialization successful
     */
    bool initialize(int width, int height, const std::string& title);
    
    /**
     * @brief Set cube state from color data
     * @param cubeState Map of face names to 3x3 color grids
     */
    void setCubeState(const std::map<std::string, std::vector<std::vector<std::string>>>& cubeState);
    
    /**
     * @brief Render the cube
     */
    void render();
    
    /**
     * @brief Update camera rotation
     * @param dx Horizontal rotation delta
     * @param dy Vertical rotation delta
     */
    void rotateCamera(float dx, float dy);
    
    /**
     * @brief Update camera zoom
     * @param delta Zoom delta
     */
    void zoom(float delta);
    
    /**
     * @brief Check if window should close
     * @return true if window should close
     */
    bool shouldClose() const;
    
    /**
     * @brief Cleanup resources
     */
    void cleanup();

private:
    /**
     * @brief Initialize OpenGL settings
     */
    void setupOpenGL();
    
    /**
     * @brief Draw a single cubelet
     * @param cubelet The cubelet to draw
     */
    void drawCubelet(const Cubelet& cubelet);
    
    /**
     * @brief Draw a single face of a cubelet
     * @param color Face color
     */
    void drawFace(const Color& color);
    
    /**
     * @brief Convert color name to RGB color
     * @param colorName Name of color (white, yellow, red, etc.)
     * @return Color struct with RGB values
     */
    Color getColor(const std::string& colorName);
    
    /**
     * @brief Initialize cubelets from cube state
     */
    void initializeCubelets();

    // Window and rendering state
    int windowWidth_;
    int windowHeight_;
    bool initialized_;
    
    // Camera state
    float cameraDistance_;
    float cameraRotationX_;
    float cameraRotationY_;
    
    // Cube state
    std::vector<Cubelet> cubelets_;
    std::map<std::string, std::vector<std::vector<std::string>>> cubeState_;
    
    // Color mapping
    std::map<std::string, Color> colorMap_;
};

} // namespace rubiks

#endif // CUBE_RENDERER_H
