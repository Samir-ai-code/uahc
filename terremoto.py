import pandas as pd
import requests
from io import StringIO
import streamlit as st

def leer_csv_desde_url(url, sep=',', encoding='utf-8'):
    try:
        response = requests.get(url)
        response.raise_for_status() # Lanza una excepción para códigos de estado HTTP 4xx/5xx
        content = response.content.decode(encoding)
        csv_data = StringIO(content)
        df = pd.read_csv(csv_data, sep=sep)
        return df

    except requests.exceptions.RequestException as e:
        raise Exception(f"Error de red o al acceder a la URL: {e}")
    except pd.errors.EmptyDataError:
        raise Exception("Error: El archivo CSV está vacío o solo contiene encabezados.")
    except pd.errors.ParserError as e:
        raise Exception(f"Error de análisis CSV. Revisa el delimitador (sep) o el formato del archivo: {e}")
    except Exception as e:
        raise Exception(f"Ocurrió un error inesperado: {e}")
    
url = "https://drive.google.com/uc?export=download&id=1UyX7sRATSNbadNxUZ7AAmbeOUm7sVpGF"
df = leer_csv_desde_url(url)
# st.write(df)
# st.metric(df)
mag_agno = df.nlargest(1, ['Magnitude'])['Year'].iloc[0]
st.write(mag_agno)
mag_valor = df.nlargest(1, ['Magnitude'])['Magnitude'].iloc[0]
st.write(mag_valor)
mag_ubicacion = df.nlargest(1, ['Magnitude'])['Location_Name'].iloc[0]

