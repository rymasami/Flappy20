import os
import sys


def resource_path(relative_path: str) -> str:
    """
    Retorna o caminho correto para um asset, tanto rodando via Python
    quanto compilado com PyInstaller (--onefile).

    Por que isso é necessário?
    Quando o PyInstaller cria um .exe com --onefile, ele extrai os arquivos
    para uma pasta temporária acessível via sys._MEIPASS.
    Sem essa função, pygame.image.load('asset/player.png') funciona no
    Python mas quebra no .exe porque o caminho relativo não existe mais.
    """
    if hasattr(sys, '_MEIPASS'):
        base_path = sys._MEIPASS
    else:
        base_path = os.path.abspath('.')

    return os.path.join(base_path, relative_path)
