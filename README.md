# DNA Replication Simulator

An interactive 3D simulation of DNA replication  built with Python and OpenGL. It shows a double-helix DNA molecule being unwound by a helicase enzyme at a moving replication fork, while two daughter DNA molecules form behind it. Each daughter keeps one original strand and gets one new strand, which is the **semi-conservative** model of replication.

## Features
- 3D double helix with sugar-phosphate backbones, nucleotide bases and hydrogen bonds
- Animated replication fork moving along the DNA
- Helicase enzyme shown at the fork
- Two daughter DNA molecules (one old strand + one new strand each)
- Real-time controls: pause/resume, restart, speed up/down
- On-screen status text (in progress / paused / completed)
- Lighting and shading for a realistic 3D look

## Technologies Used

- Python 3 | Programming language |
-PyOpenGL (`OpenGL.GL`) | 3D rendering, lighting, transformations |
-GLU | Perspective projection, camera, quadric cylinders |
-GLUT | Window, keyboard input, timer, bitmap text, solid spheres |
-`math` | Trigonometry and vector calculations |

## Methods and Algorithms Used
The following Computer Graphics concepts have been implemented in this project:

1. **OpenGL Basics**
   - Window Creation
   - OpenGL Initialization
   - Display Callback
   - Rendering

2. **3D Object Modeling**
   - 3D Sphere Modeling
   - 3D Cylinder Modeling
   - DNA Double Helix Construction

3. **Color Representation**
   - RGB Color Model
   - Object Coloring

4. **3D Transformations**
   - Translation
   - Rotation
   - Matrix Operations (Push and Pop Matrix)

5. **Projection and Viewing**
   - Perspective Projection
   - Camera Positioning
   - Viewing Transformation
   - Orthographic Projection (2D UI)

6. **Lighting and Shading**
   - OpenGL Lighting
   - Light Source Configuration
   - Material Properties
   - Smooth Surface Normals

7. **Depth Testing**
   - Depth Buffer
   - 3D Object Visibility

8. **Animation and Interaction**
   - Timer-Based Animation
   - Keyboard Interaction
   - Play/Pause Control
   - Reset Functionality
   - Animation Speed Control

9. **Mathematical Concepts**
   - Trigonometric Functions (Sine and Cosine)
   - 3D Coordinate System
   - Vector Calculation
   - Euclidean Distance
   - Angle Calculation



## Colour Legend

| Cyan, Green | Original (parent) strands |
| Red, Yellow | Newly synthesized strands |
| Purple sphere | Helicase enzyme |
| White lines | Replication fork |

## How to Run
```bash
pip install PyOpenGL PyOpenGL_accelerate
python dna.py
