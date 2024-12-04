import os
from tkinter.filedialog import askdirectory

caminho = askdirectory(title="Selecione uma pasta")

lista_arquivos = os.listdir(caminho)

# dicionario de locais para a organização

locais = {
    "Imagens": [".png", ".jpg", ".jpeg"],
    "Videos": [".mp4"],
    "Documentos": [".pdf"],
    "Planilias": [".csv",".xlsx"],
    "Executavel": [".exe",".msi"]
}

for arquivo in lista_arquivos:
    # separa o nome da extensão
    nome,extensão = os.path.splitext(f"{caminho}/{arquivo}")

    for pasta in locais:
        if extensão in locais[pasta]:
            if not os.path.exists(f"{caminho}/{pasta}"):
                os.makedirs(f"{caminho}/{pasta}")
            os.rename(f"{caminho}/{arquivo}", f"{caminho}/{pasta}/{arquivo}")
            print(f"Arquivo {arquivo} movido para a pasta {pasta}")
            