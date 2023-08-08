import cv2
import mediapipe as mp

cap = cv2.VideoCapture(0)

mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

hands = mp_hands.Hands(min_detection_confidence=0.8, min_tracking_confidence=0.5)

tipIds = [4, 8, 12, 16, 20]

# Defina uma função para contar os dedos
def contar_dedos(imagem, pontos_mao, mao_num=0):
    if pontos_mao:
        # Obtenha todos os pontos de referência da PRIMEIRA mão VISÍVEL
        pontos_referencia = pontos_mao[mao_num].landmark

        # Conte os dedos
        

        for indice_ponto in tipIds:
            # Obtenha os valores y da ponta e da parte inferior do dedo
            

            # Obtenha o valor x da ponta e da parte inferior do polegar
            x_ponta_polegar = pontos_referencia[indice_ponto].x
            x_base_polegar = pontos_referencia[indice_ponto - 2].x

            # Verifique se ALGUM DEDO está ABERTO ou FECHADO
            if indice_ponto != 4:
              
                if y_ponta_dedo > y_base_dedo:
                    dedos.append(0)
                    print("DEDO com id ", indice_ponto, " está Fechado")
            else:
                

                if x_ponta_polegar < x_base_polegar:
                    dedos.append(0)
                    print("POLEGAR está Fechado")

        total_dedos = dedos.count(1)

        # Exiba o texto
        
# Defina uma função para desenhar os pontos de referência da mão na imagem
def desenhar_pontos_referencia(imagem, pontos_mao):
    # Desenhar as conexões entre os pontos de referência
    
while True:
    sucesso, imagem = cap.read()

    imagem = cv2.flip(imagem, 1)

    # Detecte os pontos de referência das mãos
    resultados = hands.process(imagem)

    # Obtenha a posição do ponto de referência do resultado processado
    pontos_mao = resultados.multi_hand_landmarks

    # Desenhe os pontos de referência da mão na imagem
    

    # Obtenha a posição dos dedos da mão
    contar_dedos(imagem, pontos_mao)

    cv2.imshow("Controlador de Mídia", imagem)

    # Saia da tela ao pressionar a barra de espaço
    

cv2.destroyAllWindows()
