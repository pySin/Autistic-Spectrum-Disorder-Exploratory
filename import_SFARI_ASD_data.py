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
                     gene_symbol VARCHAR(20),
                     gene_name VARCHAR(255),
                     ensembl_id VARCHAR(255),
                     chromosome VARCHAR(4),
                     genetic_category TEXT,
                     gene_score VARCHAR(11),
                     syndromic TINYINT,
                     number_of_reports TINYINT,
                     gene_biotype VARCHAR(255),
                     ID VARCHAR(50)
                     """

    query = f"CREATE TABLE IF NOT EXISTS {table_name} ({columns_create})"
    return query


def create_table(table_name):
    query = create_table_in_sql(table_name)

    conn = mysql.connector.connect(host='localhost', user='root',
                                   password='dance')  # MySQL connection.
    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()


def create_insert_query(values_line):
    query = f"INSERT INTO asd_rna_seq.gen_human VALUES({values_line})"
    return query

# create_table("asd_rna_seq.SFARI_results")
