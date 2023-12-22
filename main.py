import random
import string

def gerar_chave_ativacao(tamanho=4, prefixo=""):
    # Gera uma chave aleatória com números e letras, incluindo o prefixo
    caracteres = string.ascii_letters + string.digits
    sufixo = ''.join(random.choice(caracteres) for _ in range(tamanho))
    chave = prefixo + sufixo
    return chave

def gerar_gift_card():
    # Gera números aleatórios para as posições 9 a 15 e 22 a 25
    aleatorios1 = ''.join(random.choice(string.digits) for _ in range(7))
    aleatorios2 = ''.join(random.choice(string.digits) for _ in range(4))
    
    # Combina os elementos para formar o código de gift card
    codigo_gift_card = f"63982100{aleatorios1}117046{aleatorios2}"
    return codigo_gift_card

# Exemplo de uso
if __name__ == "__main__":
    chave_gerada = gerar_chave_ativacao()
    gift_card_gerado = gerar_gift_card()

    print("Chave de Ativação:", chave_gerada)
    print("Código de Gift Card:", gift_card_gerado)
