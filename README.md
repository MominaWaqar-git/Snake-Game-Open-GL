# 🐍 Snake Game using OpenGL (Python)

## 📌 Project Overview

This project is a **classic Snake Game** developed using **Python with OpenGL (PyOpenGL + GLUT)**.
The game features a graphical interface, smooth animations, and interactive controls.

## 🎮 Features

* 🟢 Smooth snake movement using arrow keys
* 🍎 Random food generation
* 📈 Score tracking system
* ⏸ Pause / Resume functionality (button + keyboard)
* ▶ Start Game button (interactive UI)
* 💀 Game Over screen with final score
* 🔁 Restart game option
* 🧱 Solid boundary walls for collision detection
* 🎬 Demo animation before game starts

## 🛠 Technologies Used

* Python
* PyOpenGL (`OpenGL.GL`, `OpenGL.GLUT`, `OpenGL.GLU`)
* GLUT (for windowing and input handling)

## ▶ How to Run the Game

### 1. Install Dependencies

Make sure Python is installed, then install required libraries:

On bash: 
pip install PyOpenGL PyOpenGL_accelerate

### 2. Run the Game

On bash: 
python snake_game.py

## 🎯 Controls

| Action         | Key / Mouse       |
| -------------- | ----------------- |
| Move Up        | ↑ Arrow Key       |
| Move Down      | ↓ Arrow Key       |
| Move Left      | ← Arrow Key       |
| Move Right     | → Arrow Key       |
| Pause / Resume | `P` key or Button |
| Restart Game   | `R` key           |
| Start Game     | Mouse Click       |

## 🧠 Game Logic

* The snake moves in a grid-based system.
* Food appears randomly inside the boundary.
* Eating food:
  * Increases snake length
  * Adds **+10 score**
* Game ends if:
  * Snake hits boundary walls
  * Snake collides with itself
    
## 🎨 UI Elements

* 🟩 Green boundary walls
* 🟠 Snake body (circular segments)
* 🔴 Food (circle)
* 🔘 Interactive buttons:

  * Start Game
  * Pause / Resume

## 🔄 Game States

* **Start Screen** → Demo snake animation
* **Playing Mode** → User controls snake
* **Paused Mode** → Game temporarily stops
* **Game Over** → Final score displayed

## 📂 File Structure

snake_game.py 
README.md    

## 🚀 Future Improvements

* Add sound effects 🎵
* Add difficulty levels ⚡
* High score system 🏆
* Better UI/graphics ✨
* Mobile or web version 🌐

## 👩‍💻 Author

 Momina Waqar

## 📜 Note

This project is for educational purpose.
