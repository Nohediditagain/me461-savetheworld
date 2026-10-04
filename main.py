import pygame
import cv2
import math
import mediapipe as mp
import random 

pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
last_spawn_time2 = pygame.time.get_ticks()
game_start_time = pygame.time.get_ticks()
last_spawn_time = pygame.time.get_ticks()
last_pinch_time = pygame.time.get_ticks()
running = True
pygame.display.set_caption("SAVE THE WORLD")
camera = cv2.VideoCapture(0)
hands = mp.solutions.hands.Hands()
is_pinching = False 
is_alive = True
is_attack = False
health = 5
life_points = [[300,0, True]]
is_ulting = False 
last_ult_time = pygame.time.get_ticks()





monsters = [[10,0,True]]


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
    if health <= 0 :
        break
    frame2 = cv2.flip(frame, 1)
    frame3 = cv2.cvtColor(frame2, cv2.COLOR_BGR2RGB)
    results = hands.process(frame3)
    
    screen.fill((0, 0, 0))
    time2 = pygame.time.get_ticks()
    time = pygame.time.get_ticks()
    time3 = pygame.time.get_ticks()
    time4 = pygame.time.get_ticks()
    gecen_zaman = pygame.time.get_ticks() - game_start_time

    u = min(gecen_zaman / 30000, 1)
    canavar_hizi = 2 + 1.5 * u ** 2

    saniyede_kac_canavar = 0.5 + 1.5 * u ** 2

    canavar_dogurma_suresi = 2000 / saniyede_kac_canavar

    if time2 - last_spawn_time2 >= canavar_dogurma_suresi :
        monsters.append([random.randint(0,800),0,True])
        last_spawn_time2 = time2

    if time3 - last_spawn_time >= 10000 :
        life_points.append([random.randint(0,800),0,True])
        last_spawn_time = time3

    if  time - last_pinch_time >= 1500 and not is_attack :
       print(str(time - last_pinch_time))
       is_attack = True

    if time4 - last_ult_time >= 10000 :
        last_ult_time = time4
        is_ulting = False 

 
    for life_point in life_points:
        if life_point[2] == True:
            pygame.draw.circle(screen, (0,255,0), (life_point[0],life_point[1]), 5)

        if life_point[1] < 505 and life_point[2] == True:
            life_point[1] += 4

        elif life_point[1] >= 505 and life_point[2] == True :
            life_point[2] = False
            health += 1
    
        if life_point[2] == True and is_pinching == True and is_attack == True :
            if min(x1-20,x2+20) <= life_point[0] <= max(x1-20,x2+20) and min(y1-25,y2+25) <= life_point[1] <= max(y1-25,y2+25):
                life_point[2] = False  
                is_attack = False
                last_pinch_time = time     
                health -= 1

    for monster in monsters:
    
        if monster[2] == True:
            pygame.draw.circle(screen, (255,0,0), (monster[0],int(monster[1])), 5)
    
        if monster[1] < 505 and monster[2] == True:
            monster[1] += canavar_hizi
        elif monster[1] >= 505 and monster[2] == True :
            monster[2] = False
            health -= 1

        if monster[2] == True and is_pinching == True and is_attack == True :
            if min(x1-20,x2+20) <= monster[0] <= max(x1-20,x2+20) and min(y1-25,y2+25) <= monster[1] <= max(y1-25,y2+25):
                monster[2] = False  
                is_attack = False
                last_pinch_time = time     

        
    
    if results.multi_hand_landmarks:
        hand = results.multi_hand_landmarks[0]

        isaret4 = hand.landmark[8]
        x1 = int(isaret4.x * 800)
        y1 = int(isaret4.y * 600)
        p1 = (x1,y1)
        pygame.draw.circle(screen, (0, 255, 0), p1, 10)

        isaret2 = hand.landmark[6]
        x6 = int(isaret2.x * 800)
        y6 = int(isaret2.y * 600)
        p6 = (x6,y6)
        pygame.draw.circle(screen,(0,0,255), p6, 10 )

        yuzuk2 = hand.landmark[14]
        x7 = int(yuzuk2.x * 800)
        y7 = int(yuzuk2.y * 600)
        p7 = (x7,y7)
        pygame.draw.circle(screen,(0,0,255), p7, 10 )

        yuzuk4 = hand.landmark[16]
        x8 = int(yuzuk4.x * 800)
        y8 = int(yuzuk4.y * 600)
        p8 = (x8,y8)
        pygame.draw.circle(screen,(0,0,255), p8, 10 )

        serce2 = hand.landmark[18]
        x9 = int(serce2.x * 800)
        y9 = int(serce2.y * 600)
        p9 = (x9,y9)
        pygame.draw.circle(screen,(0,0,255), p9, 10 )

        serce4 = hand.landmark[20]
        x10 = int(serce4.x * 800)
        y10 = int(serce4.y * 600)
        p10 = (x10,y10)
        pygame.draw.circle(screen,(0,0,255), p10, 10 )

        orta_barnak2 = hand.landmark[10]
        x12 = int(orta_barnak2.x * 800)
        y12 = int(orta_barnak2.y * 600)
        p12 = (x12,y12)
        pygame.draw.circle(screen,(0,0,255), p12, 10 )

        tombul_parmak4 = hand.landmark[4]
        x2 = int(tombul_parmak4.x * 800)
        y2 = int(tombul_parmak4.y * 600)
        p2 = (x2,y2)
        pygame.draw.circle(screen, (0, 0, 255), p2, 10)

        l1 = math.hypot(x1-x2, y1-y2)
        bilek = hand.landmark[0]
        x3 = int(bilek.x * 800)
        y3 = int(bilek.y * 600)
        p3 = (x3,y3)
        orta_barnak1 = hand.landmark[9]
        x4 = int(orta_barnak1.x * 800)
        y4 = int(orta_barnak1.y * 600)
        p4 = (x4,y4)
        orta_barnak4 = hand.landmark[12]
        x5 = int(orta_barnak4.x * 800)
        y5 = int(orta_barnak4.y * 600)
        p5 = (x5 , y5)
        pygame.draw.circle(screen, (0, 255, 0), p5, 10)

    
        referans_mesafe = math.hypot(x4-x3,y4-y3)

        if not referans_mesafe == 0:
            cimcik_orani = l1 / referans_mesafe
        
            if not is_pinching and cimcik_orani < 0.35:
                is_pinching = True
            elif is_pinching and cimcik_orani > 0.45:
                is_pinching = False
            if not is_ulting and y1 < y6  and y12 > y5 and y9 > y10 and y8 < y7:
                is_ulting = True
                for monster in monsters:
                    monster[2] = False
          
            pygame.display.set_caption("Save the world " + str(cimcik_orani) + str(is_pinching) + str(time2 - last_pinch_time) + str(is_attack) + str(health) + str(is_ulting))
                 
            
    else:
        is_pinching = False
        
    pygame.display.flip()
    clock.tick(60)

hands.close()
camera.release()
pygame.quit()
