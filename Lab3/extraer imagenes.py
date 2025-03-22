import os

def obtener_nombres_imagenes(carpeta="imagenes"):
    if not os.path.exists(carpeta):
        print(f"La carpeta '{carpeta}' no existe.")
        return []
    
    # Filtrar solo archivos de imagen (jpg, png, jpeg, etc.)
    imagenes = [f for f in os.listdir(carpeta) if f.lower().endswith((".jpg", ".jpeg", ".png", ".gif"))]
    
    return imagenes

if __name__ == "__main__":
    carpeta_imagenes = "imagenes"  # Cambia esto si tu carpeta tiene otro nombre
    nombres = obtener_nombres_imagenes(carpeta_imagenes)
    
    if nombres:
        print("Imágenes encontradas:")
        for nombre in nombres:
            print(nombre)
    else:
        print("No se encontraron imágenes en la carpeta.")
