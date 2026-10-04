import pygame
import cv2
import math
import mediapipe as mp
import random 

pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
last_spawn_time = pygame.time.get_ticks()
running = True
pygame.display.set_caption("SAVE THE WORLD")
camera = cv2.VideoCapture(0)
hands = mp.solutions.hands.Hands()
is_pinching = False 
is_alive = True



monsters = [[10,0]]

while running:
    if not camera.isOpened():
        break

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    success, frame = camera.read()
    if not success:
        print("Başarisiz kare okuma")
        break
    frame2 = cv2.flip(frame, 1)
    frame3 = cv2.cvtColor(frame2, cv2.COLOR_BGR2RGB)
    results = hands.process(frame3)
    time = pygame.time.get_ticks()
    screen.fill((0, 0, 0))

    if time - last_spawn_time >= 5000 :
        monsters.append([random.randint(0,800),0])
        last_spawn_time = time

    
    for monster in monsters:
        pygame.draw.circle(screen, (255,0,0), monster, 5)
        if monster[1] < 605:
            monster[1] += 1

    

        
    
    if results.multi_hand_landmarks:
        hand = results.multi_hand_landmarks[0]
        index_tip = hand.landmark[8]
        x1 = int(index_tip.x * 800)
        y1 = int(index_tip.y * 600)
        p1 = (x1,y1)
        pygame.draw.circle(screen, (0, 255, 0), p1, 10)
        tombul_parmak = hand.landmark[4]
        x2 = int(tombul_parmak.x * 800)
        y2 = int(tombul_parmak.y * 600)
        p2 = (x2,y2)
        pygame.draw.circle(screen, (0, 0, 255), p2, 10)
        l1 = math.hypot(x1-x2, y1-y2)
        bilek = hand.landmark[0]
        x3 = int(bilek.x * 800)
        y3 = int(bilek.y * 600)
        p3 = (x3,y3)
        orta_barnak = hand.landmark[9]
        x4 = int(orta_barnak.x * 800)
        y4 = int(orta_barnak.y * 600)
        p4 = (x4,y4)
        referans_mesafe = math.hypot(x4-x3,y4-y3)
        if not referans_mesafe == 0:
            cimcik_orani = l1 / referans_mesafe
            if not is_pinching and cimcik_orani < 0.35:
                is_pinching = True
            elif is_pinching and cimcik_orani > 0.45:
                is_pinching = False
            pygame.display.set_caption("Save the world " + str(cimcik_orani) + str(is_pinching) )
                
            

    else:
        is_pinching = False
        print("El YOK")
    pygame.display.flip()
    clock.tick(60)

hands.close()
camera.release()
pygame.quit()
