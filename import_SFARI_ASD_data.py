# Import SFARI Autistic Spectrum Disorder file
import mysql.connector

FILE_PATH = r"C:\Users\1\PycharmProjects\Autistic-Spectrum-Disorder-Exploratory\data\SFARI_dataset.csv"


def read_first_line(file_path):
    with open(file_path, "r") as o_file:
        first_line = o_file.readline().split(",")
    return first_line


def create_table_in_sql(table_name: str):
    columns_create = """
                     status INT,
                     gene-symbol VARCHAR(20),
                     gene-name VARCHAR(255),
                     
                     """
