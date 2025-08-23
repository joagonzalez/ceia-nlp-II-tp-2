import sys
from pathlib import Path

# Agregar el directorio raíz al path para importar módulos
sys.path.append(str(Path(__file__).parent))

from src.vectorService import load_data_into_vectordb
from src.config.settings import DATASET


def main():
    """
    Función principal que carga los datos del CV en la base de datos vectorial
    """
    print("Iniciando carga de datos del CV en la base de datos vectorial...")
    
    # Verificar que los archivos del dataset existen
    data_dir = Path(__file__).parent / "data"
    dataset_paths = []
    
    for file_name in DATASET:
        file_path = data_dir / file_name
        if file_path.exists():
            dataset_paths.append(str(file_path))
            print(f"Archivo encontrado: {file_path}")
        else:
            print(f"Error: Archivo no encontrado: {file_path}")
            sys.exit(1)
    
    if not dataset_paths:
        print("No se encontraron archivos para procesar")
        sys.exit(1)
    
    try:
        # Cargar datos usando vectorService
        print("\nProcesando y cargando datos en la base de datos vectorial...")
        load_data_into_vectordb(dataset_paths)
        
        print("\n¡Datos cargados exitosamente en la base de datos vectorial!")
        print(f"Archivos procesados: {len(dataset_paths)}")
        print("Los datos ya están disponibles para búsquedas")
        
    except Exception as e:
        print(f"\nError durante la carga de datos: {str(e)}")
        sys.exit(1)


if __name__ == "__main__":
    main()