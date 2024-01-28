import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import requests
import os
from io import StringIO
import plotly.express as px

# Configuration de la clé API Plotly
plotly_username = "aidimamahfouz"
plotly_api_key = "ygewwWcLud5Zgq3FqxyU"

# Configuration des informations d'authentification
px.set_mapbox_access_token(plotly_api_key)

# Exemple de graphique
fig = px.scatter_mapbox(...)

# Publier le graphique en ligne
fig.show()


# Function to import data from GitHub
def import_data_from_github(url, file_type):
    try:
        if file_type.lower() == 'csv':
            return pd.read_csv(url)
        elif file_type.lower() in ['xls', 'xlsx']:
            return pd.read_excel(url)
        else:
            st.error("File type not supported. Supported types: CSV, Excel")
            return None
    except Exception as e:
        st.error(f"Error importing data: {e}")
        return None

# URL of the CSV or Excel file on GitHub
github_csv_url = "https://github.com/aidimamahfouz/test4/blob/main/expat_dakar_appartement_data_whith_BeautifulSoup.csv"

# Choose the type of file to import ('csv' or 'excel')
file_type = st.radio("Select file type to import", ['csv', 'excel'])

# Use the appropriate URL based on the selected file type
github_url = github_csv_url  # Assuming CSV for this example

# Import data
data = import_data_from_github(github_url, file_type)

# Continue with the rest of your code
# ...

# If data is successfully imported, display a sample
if data is not None:
    st.subheader("Sample Data")
    st.write(data.head())

    # Plotly Visualization Examples
    st.header("Plotly Visualizations")

    # Line Chart
    st.subheader("Line Chart")
    line_chart = px.line(data, x=data.columns[0], y=data.columns[1])
    st.plotly_chart(line_chart)

    # Bar Chart
    st.subheader("Bar Chart")
    bar_chart = px.bar(data, x=data.columns[0], y=data.columns[1])
    st.plotly_chart(bar_chart)

    # Scatter Plot
    st.subheader("Scatter Plot")
    scatter_plot = px.scatter(data, x=data.columns[0], y=data.columns[1])
    st.plotly_chart(scatter_plot)

    # Pie Chart
    st.subheader("Pie Chart")
    pie_chart = px.pie(data, names=data.columns[0], values=data.columns[1])
    st.plotly_chart(pie_chart)

    # Box Plot
    st.subheader("Box Plot")
    box_plot = px.box(data, x=data.columns[0], y=data.columns[1])
    st.plotly_chart(box_plot)


# Function to import data from GitHub
def import_data_from_github(url, file_type):
    response = requests.get(url)
    if response.status_code == 200:
        if file_type.lower() == 'csv':
            return pd.read_csv(StringIO(response.text))
        elif file_type.lower() in ['xls', 'xlsx']:
            return pd.read_excel(StringIO(response.content))
        else:
            st.error("File type not supported. Supported types: CSV, Excel")
            return None
    else:
        st.error(f"Error downloading data from GitHub. Error code: {response.status_code}")
        return None

# URL of the CSV or Excel file on GitHub
github_csv_url = "https://github.com/aidimamahfouz/test4/blob/main/expat_dakar_appartement_data_whith_BeautifulSoup.csv"
github_excel_url = "https://github.com/aidimamahfouz/test4/blob/main/expat_dakar_appartement_data_whith_BeautifulSoup.xlsx"

# Choose the type of file to import ('csv' or 'excel')
file_type = st.radio("Select file type to import", ['csv', 'excel'])

# Use the appropriate URL based on the selected file type
github_url = github_csv_url if file_type == 'csv' else github_excel_url

# Import data
data = import_data_from_github(github_url, file_type)

# Continue with the rest of your code
# ...

# If data is successfully imported, display a sample
if data is not None:
    st.subheader("Sample Data")
    st.write(data.head())

    # Add other visualizations or analysis as needed
    # ...




# Set PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION environment variable
os.environ['PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION'] = 'python'


# Fonction principale de l'application Streamlit
def main():
    st.title("Analyse Graphique avec Streamlit")

    # Bouton pour importer un fichier de données
    uploaded_file = st.file_uploader("Importer un fichier de données (CSV, Excel, etc.)", type=["csv", "xlsx"])

    # Si un fichier a été importé
    if uploaded_file is not None:
        # Charger les données dans un DataFrame
        data = pd.read_csv(uploaded_file)  # Changez la fonction selon le type de fichier

        # Afficher un échantillon des données
        st.subheader("Échantillon des Données")
        st.write(data.head())

        # Graphiques
        st.subheader("Graphiques")

        # Histogramme
        st.subheader("Histogramme")
        selected_column = st.selectbox("Sélectionnez une colonne pour l'histogramme", data.columns)
        plt.hist(data[selected_column], bins=5, edgecolor='black')
        st.pyplot()

        # Nuage de points
        st.subheader("Nuage de Points")
        x_column = st.selectbox("Sélectionnez la colonne x", data.columns)
        y_column = st.selectbox("Sélectionnez la colonne y", data.columns)
        sns.scatterplot(x=x_column, y=y_column, data=data)
        st.pyplot()

        # Autres graphiques...

# Exécuter l'application
if __name__ == "__main__":
    main()
