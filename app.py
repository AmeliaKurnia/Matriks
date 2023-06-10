import streamlit as st
import numpy as np
from sympy import symbols, diff, expand

# Fungsi untuk mencari bentuk kuadrat matriks
def square_matrix(matrix):
    n = len(matrix)
    m = len(matrix[0])

    # Membangun matriks kuadrat
    squared_matrix = [[None] * m for _ in range(n)]

    for i in range(n):
        for j in range(m):
            element = matrix[i][j]
            try:
                x = symbols('x')
                expression = eval(element)  # Mengubah bentuk polinomial menjadi objek simbolik
                squared_matrix[i][j] = expand(expression ** 2)  # Menghitung kuadrat
            except (NameError, SyntaxError):
                squared_matrix[i][j] = element

    return squared_matrix

# Fungsi untuk mencari turunan pertama matriks
def first_derivative(matrix):
    n = len(matrix)
    m = len(matrix[0])

    # Membangun matriks turunan pertama
    first_der = [[None] * m for _ in range(n)]

    x = symbols('x')

    for i in range(n):
        for j in range(m):
            element = matrix[i][j]
            try:
                expression = eval(element)  # Mengubah bentuk polinomial menjadi objek simbolik
                first_der[i][j] = expand(diff(expression, x))  # Menghitung turunan pertama
            except (NameError, SyntaxError):
                first_der[i][j] = element

    return first_der

# Fungsi untuk mencari turunan kedua matriks
def second_derivative(matrix):
    n = len(matrix)
    m = len(matrix[0])

    # Membangun matriks turunan kedua
    second_der = [[None] * m for _ in range(n)]

    x = symbols('x')

    for i in range(n):
        for j in range(m):
            element = matrix[i][j]
            try:
                expression = eval(element)  # Mengubah bentuk polinomial menjadi objek simbolik
                second_der[i][j] = expand(diff(expression, x, 2))  # Menghitung turunan kedua
            except (NameError, SyntaxError):
                second_der[i][j] = element

    return second_der

# Halaman Home
def home():
    st.title("Aplikasi Matriks dan Turunan")
    st.write("Selamat datang di aplikasi ini!")
    st.write("Aplikasi ini dapat digunakan untuk mencari bentuk kuadrat matriks, turunan pertama matriks, dan turunan kedua matriks. (Semoga tidak error yea, klo error yaudalahya...)")
    st.write("Pilih halaman yang diinginkan dari sidebar.")

# Halaman Bentuk Kuadrat Matriks
def bentuk_kuadrat_matriks():
    st.title("Bentuk Kuadrat Matriks")
    matrix_cols = st.number_input("Masukkan jumlah kolom matriks:", min_value=1, step=1)
    matrix_rows = st.number_input("Masukkan jumlah baris matriks:", min_value=1, step=1)
    matrix_input = st.text_area("Masukkan matriks (pisahkan elemen dengan spasi dan baris dengan enter, gunakan tanda [*] untuk perkalian):")
    if st.button("Cari Bentuk Kuadrat"):
        matrix = [[element.strip() for element in row.split()] for row in matrix_input.strip().split('\n')]
        squared_matrix = square_matrix(matrix)
        squared_matrix = np.array(squared_matrix)
        st.write(np.array2string(squared_matrix, separator=" "))

# Halaman Turunan Pertama Matriks
def turunan_pertama():
    st.title("Turunan Pertama Matriks")
    matrix_cols = st.number_input("Masukkan jumlah kolom matriks:", min_value=1, step=1)
    matrix_rows = st.number_input("Masukkan jumlah baris matriks:", min_value=1, step=1)
    matrix_input = st.text_area("Masukkan matriks (pisahkan elemen dengan spasi dan baris dengan enter, gunakan tanda [*] untuk perkalian):")
    if st.button("Cari Turunan Pertama"):
        matrix = [[element.strip() for element in row.split()] for row in matrix_input.strip().split('\n')]
        first_der = first_derivative(matrix)
        first_der = np.array(first_der)
        st.write(np.array2string(first_der, separator=" "))

# Halaman Turunan Kedua Matriks
def turunan_kedua():
    st.title("Turunan Kedua Matriks")
    matrix_cols = st.number_input("Masukkan jumlah kolom matriks:", min_value=1, step=1)
    matrix_rows = st.number_input("Masukkan jumlah baris matriks:", min_value=1, step=1)
    matrix_input = st.text_area("Masukkan matriks (pisahkan elemen dengan spasi dan baris dengan enter, gunakan tanda [*] untuk perkalian):")
    if st.button("Cari Turunan Kedua"):
        matrix = [[element.strip() for element in row.split()] for row in matrix_input.strip().split('\n')]
        second_der = second_derivative(matrix)
        second_der = np.array(second_der)
        st.write(np.array2string(second_der, separator=" "))

# Sidebar
pages = {
    "Home": home,
    "Bentuk Kuadrat Matriks": bentuk_kuadrat_matriks,
    "Turunan Pertama Matriks": turunan_pertama,
    "Turunan Kedua Matriks": turunan_kedua
}

# Main Program
st.sidebar.title("Aplikasi Matriks dan Turunan")
page = st.sidebar.radio("Pilih Halaman", tuple(pages.keys()))

if page in pages:
    pages[page]()
