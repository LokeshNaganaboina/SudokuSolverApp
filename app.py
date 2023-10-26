import streamlit as st
from PIL import Image
from sudukoMain import solve_sudoku
import tempfile

st.title('Sudoku Solver')

uploaded_file = st.file_uploader("Upload an image of a Sudoku puzzle", type=["jpg", "jpeg", "png"])

# Define the fixed size for the images
fixed_size = (450, 450)

if uploaded_file is not None:
    image = Image.open(uploaded_file)

    # Resize the uploaded image to the fixed size
    image = image.resize(fixed_size)

    # Save the uploaded image to a temporary file
    with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as temp_file:
        image.save(temp_file.name)
        solved_image_array = solve_sudoku(temp_file.name)
    
    #Converting to image from numpy array and also resizing it.
    solved_image = Image.fromarray(solved_image_array).resize(fixed_size)

    col1, col2 = st.columns(2)

    # Displaying the uploaded and solved images
    col1.header('Uploaded Sudoku')
    col1.image(image, use_column_width=True)

    col2.header('Solved Sudoku')
    col2.image(solved_image, use_column_width=True)
