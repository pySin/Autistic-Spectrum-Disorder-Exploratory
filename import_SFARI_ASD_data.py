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
                     ensembl-id VARCHAR(255),
                     chromosome VARCHAR(4),
                     genetic-category TEXT,
                     gene_score VARCHAR(11),
                     syndromic TINYINT,
                     number-of-reports TINYINT,
                     gene_biotype VARCHAR(255),
                     ID VARCHAR(50)
                     """

    query = f"CREATE TABLE IF NOT EXISTS {table_name} ({columns_create})"
    return query


def create_table(table_name):
    query = create_table_in_sql(table_name)
