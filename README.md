# Sudoku Solver using OpenCV

This repository contains a web-based Sudoku Solver implemented using the OpenCV library for image processing and streamlit for deployment. The goal of this project is to provide a user-friendly tool for solving Sudoku puzzles automatically using computer vision techniques.

## Installation

Clone the repository:

```bash
git clone https://github.com/LokeshNaganaboina/SudokuSolverApp.git
```
Set up a virtual environment (optional but recommended):

```bash
python -m venv venv-name
source venv-name/bin/activate #For Linux or macOS users
venv-name\Scripts\activate #For Windows users
```

Install the necessary packages to run this project from requirements.txt

```bash
pip install -r requirements.txt
```
To run the app, run the following command
```bash
streamlit run app.py
```

## Usage
Run the Sudoku Solver application:
```python
streamlit run app.py
```
Select an image: You can select to input an image file containing an unsolved sudoku puzzle. Ensure that the image is of good quality and images should be recognized.

Press the 'Solve' button to initiate the solving process. The application will display the solved puzzle on the screen.

## How it Works

The Sudoku Solver uses OpenCV for image processing and computer vision tasks. Here's a high-level overview of the solving process:

Input Processing: The input image is preprocessed using various techniques like thresholding, contour detection, and perspective transformation to extract the Sudoku grid.

Digit Recognition: Each cell of the grid is isolated, and digit recognition is performed using a custom OCR trained model.

Backtracking Algorithm: The recognized puzzle is then solved using a backtracking algorithm, a common approach for solving Sudoku puzzles.



##

Enjoy solving Sudoku puzzles with the power of OpenCV and Flask! If you have any questions or need assistance, feel free to contact me.
