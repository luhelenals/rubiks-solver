/**
 * @file cube_renderer.cpp
 * @brief Implementation of OpenGL renderer for Rubik's cube
 */

#include "cube_renderer.h"
#include <cmath>
#include <iostream>

namespace rubiks {

CubeRenderer::CubeRenderer()
    : windowWidth_(800)
    , windowHeight_(600)
    , initialized_(false)
    , cameraDistance_(10.0f)
    , cameraRotationX_(30.0f)
    , cameraRotationY_(45.0f)
{
    // Initialize color map
    colorMap_["white"] = Color(1.0f, 1.0f, 1.0f);
    colorMap_["yellow"] = Color(1.0f, 1.0f, 0.0f);
    colorMap_["red"] = Color(1.0f, 0.0f, 0.0f);
    colorMap_["orange"] = Color(1.0f, 0.5f, 0.0f);
    colorMap_["blue"] = Color(0.0f, 0.0f, 1.0f);
    colorMap_["green"] = Color(0.0f, 1.0f, 0.0f);
}

CubeRenderer::~CubeRenderer() {
    cleanup();
}

bool CubeRenderer::initialize(int width, int height, const std::string& title) {
    windowWidth_ = width;
    windowHeight_ = height;
    
    // Note: Actual OpenGL/GLFW initialization would go here
    // For now, this is a structural implementation
    
    setupOpenGL();
    initialized_ = true;
    
    return true;
}

void CubeRenderer::setupOpenGL() {
    // Enable depth testing
    glEnable(GL_DEPTH_TEST);
    glDepthFunc(GL_LESS);
    
    // Enable lighting
    glEnable(GL_LIGHTING);
    glEnable(GL_LIGHT0);
    
    // Set light properties
    GLfloat light_position[] = {5.0f, 5.0f, 5.0f, 1.0f};
    GLfloat light_ambient[] = {0.3f, 0.3f, 0.3f, 1.0f};
    GLfloat light_diffuse[] = {0.8f, 0.8f, 0.8f, 1.0f};
    
    glLightfv(GL_LIGHT0, GL_POSITION, light_position);
    glLightfv(GL_LIGHT0, GL_AMBIENT, light_ambient);
    glLightfv(GL_LIGHT0, GL_DIFFUSE, light_diffuse);
    
    // Set material properties
    glEnable(GL_COLOR_MATERIAL);
    glColorMaterial(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE);
    
    // Set background color
    glClearColor(0.1f, 0.1f, 0.15f, 1.0f);
}

void CubeRenderer::setCubeState(
    const std::map<std::string, std::vector<std::vector<std::string>>>& cubeState) {
    cubeState_ = cubeState;
    initializeCubelets();
}

void CubeRenderer::initializeCubelets() {
    cubelets_.clear();
    
    // Create 27 cubelets (3x3x3)
    for (int x = -1; x <= 1; ++x) {
        for (int y = -1; y <= 1; ++y) {
            for (int z = -1; z <= 1; ++z) {
                Cubelet cubelet(x * 1.1f, y * 1.1f, z * 1.1f);
                
                // Assign colors based on position
                // This is simplified - real implementation would map from cubeState_
                
                cubelets_.push_back(cubelet);
            }
        }
    }
}

void CubeRenderer::render() {
    if (!initialized_) return;
    
    // Clear buffers
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);
    
    // Reset transformations
    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();
    gluPerspective(45.0f, (float)windowWidth_ / (float)windowHeight_, 0.1f, 100.0f);
    
    glMatrixMode(GL_MODELVIEW);
    glLoadIdentity();
    
    // Set camera position
    glTranslatef(0.0f, 0.0f, -cameraDistance_);
    glRotatef(cameraRotationX_, 1.0f, 0.0f, 0.0f);
    glRotatef(cameraRotationY_, 0.0f, 1.0f, 0.0f);
    
    // Draw all cubelets
    for (const auto& cubelet : cubelets_) {
        drawCubelet(cubelet);
    }
}

void CubeRenderer::drawCubelet(const Cubelet& cubelet) {
    glPushMatrix();
    
    // Position cubelet
    glTranslatef(cubelet.x, cubelet.y, cubelet.z);
    glRotatef(cubelet.rx, 1.0f, 0.0f, 0.0f);
    glRotatef(cubelet.ry, 0.0f, 1.0f, 0.0f);
    glRotatef(cubelet.rz, 0.0f, 0.0f, 1.0f);
    
    float size = 0.5f;
    float gap = 0.05f;
    
    // Draw each face with appropriate color
    // Front face (Z+)
    glPushMatrix();
    glTranslatef(0.0f, 0.0f, size);
    drawFace(Color(1.0f, 0.0f, 0.0f)); // Red
    glPopMatrix();
    
    // Back face (Z-)
    glPushMatrix();
    glTranslatef(0.0f, 0.0f, -size);
    glRotatef(180.0f, 0.0f, 1.0f, 0.0f);
    drawFace(Color(1.0f, 0.5f, 0.0f)); // Orange
    glPopMatrix();
    
    // Top face (Y+)
    glPushMatrix();
    glTranslatef(0.0f, size, 0.0f);
    glRotatef(-90.0f, 1.0f, 0.0f, 0.0f);
    drawFace(Color(1.0f, 1.0f, 1.0f)); // White
    glPopMatrix();
    
    // Bottom face (Y-)
    glPushMatrix();
    glTranslatef(0.0f, -size, 0.0f);
    glRotatef(90.0f, 1.0f, 0.0f, 0.0f);
    drawFace(Color(1.0f, 1.0f, 0.0f)); // Yellow
    glPopMatrix();
    
    // Right face (X+)
    glPushMatrix();
    glTranslatef(size, 0.0f, 0.0f);
    glRotatef(90.0f, 0.0f, 1.0f, 0.0f);
    drawFace(Color(0.0f, 1.0f, 0.0f)); // Green
    glPopMatrix();
    
    // Left face (X-)
    glPushMatrix();
    glTranslatef(-size, 0.0f, 0.0f);
    glRotatef(-90.0f, 0.0f, 1.0f, 0.0f);
    drawFace(Color(0.0f, 0.0f, 1.0f)); // Blue
    glPopMatrix();
    
    glPopMatrix();
}

void CubeRenderer::drawFace(const Color& color) {
    float size = 0.48f; // Slightly smaller than cubelet for gaps
    
    glColor3f(color.r, color.g, color.b);
    
    glBegin(GL_QUADS);
    glNormal3f(0.0f, 0.0f, 1.0f);
    glVertex3f(-size, -size, 0.0f);
    glVertex3f(size, -size, 0.0f);
    glVertex3f(size, size, 0.0f);
    glVertex3f(-size, size, 0.0f);
    glEnd();
    
    // Draw black border
    glColor3f(0.0f, 0.0f, 0.0f);
    glLineWidth(2.0f);
    glBegin(GL_LINE_LOOP);
    glVertex3f(-size, -size, 0.0f);
    glVertex3f(size, -size, 0.0f);
    glVertex3f(size, size, 0.0f);
    glVertex3f(-size, size, 0.0f);
    glEnd();
}

void CubeRenderer::rotateCamera(float dx, float dy) {
    cameraRotationY_ += dx;
    cameraRotationX_ += dy;
    
    // Clamp vertical rotation
    if (cameraRotationX_ > 89.0f) cameraRotationX_ = 89.0f;
    if (cameraRotationX_ < -89.0f) cameraRotationX_ = -89.0f;
}

void CubeRenderer::zoom(float delta) {
    cameraDistance_ += delta;
    
    // Clamp zoom
    if (cameraDistance_ < 5.0f) cameraDistance_ = 5.0f;
    if (cameraDistance_ > 20.0f) cameraDistance_ = 20.0f;
}

Color CubeRenderer::getColor(const std::string& colorName) {
    auto it = colorMap_.find(colorName);
    if (it != colorMap_.end()) {
        return it->second;
    }
    return Color(0.5f, 0.5f, 0.5f); // Default gray
}

bool CubeRenderer::shouldClose() const {
    // This would check window close events in a real implementation
    return false;
}

void CubeRenderer::cleanup() {
    // Cleanup OpenGL resources
    initialized_ = false;
}

} // namespace rubiks
