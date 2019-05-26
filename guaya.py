import random

numero1 = random.randint(1,6)
numero2 = random.randint(1,6)
player_1 = []
player_2 = []
plata1 = 1000
plata2 = 500
mesa = 100
balance1 = 0
balance2 = 0

while plata1 > 0:
    player_1.append(random.randint(1,6))
    if


# while len(player_1) != 2:
#     player_1.append(random.randint(1,6))
#     if player_1[0] == 1 or player_1[0] == 6:
#         plata1 -= 100
#         mesa += 100
#         print(player_1)
#
#     elif player_1[0] >= 2 and player_1[0] <= 5:
#         print(player_1)
#         juego = str(input('juega j o se queda'))
#         if juego == 'j':
#             player_1.append(random.randint(1,6))
#             if player_1[0] >= player_1[1]:
#                 balance1 = plata1 - mesa
#                 mesa = 0
#                 print(player_1, 'Perdio')
#             else:
#                 print(player_1, 'Gano')
#         else:
#             mesa += 100
#             print('Dinero en la mesa', mesa)
#
#     player_2.append(random.randint(1,6))
#     if player_1[0] == 1 or player_1[0] == 6:
#         plata1 -= 100
#         mesa += 100




# while mesa == 0:
#     player_1.append(random.randint(1,6))
#     if player_1[0] == 1 or player_1[0] == 6:
#         player_2.append(random.randint(1,6))
#         plata1 -= 100
#         mesa += 100
#         print(player_1, 'J1 Pone 100')
#         if player_2[0] == 1 or player_2[0] == 6:
#             player_1.pop()
#             player_2.append(random.randint(1, 6))
#             plata2 -= 100
#             mesa += 100
#             print(player_2, 'J2 Pone 100')
#             player_2.pop()
#
# while mesa > 0:
#
#     if player_1[0] >= 2 and player_1[0] <= 5:
#         print(player_1)
#         juego = str(input('juega j o se queda'))
#         if juego == 'j':
#             player_1.append(random.randint(1,6))
#             if player_1[0] >= player_1[1]:
#                 balance1 = plata1 - mesa
#                 print(player_1, 'Perdio y ahora tiene', balance1)
#             else:
#                 balance1 = plata1 + mesa
#                 print(player_1, 'Gano y ahora tiene', balance1)
#         else:
#             player_2.append(random.randint(1,6))
#             if player_2[0] >= player_2[1]:
#                 balance2 = plata2 - mesa
#                 print(player_2, 'Perdio y ahora tiene', balance2)
#             else:
#                 balance1 = plata1 + mesa
#                 print(player_2, 'Gano y ahora tiene', balance2)


# while mesa != 0:
#     player_1.append(random.randint(1,6))
#     print(player_1)
#     if player_1[0] == 1 or player_1[0] == 6:
#         plata1 -= 100
#         mesa += 100
#         player_2.append(random.randint(1,6))
#     elif player_1[0] >= 2 and player_1[0] <= 5:
#         pedir = str(input('apostar o pasar'))
#         if pedir == 'apostar':
#             player_1.append(random.randint(1,6))
#             if player_1[0] >= player_1[1]:
#                 balance1 = plata1 - mesa
#                 print('Perdiste', player_1, 'te queda', balance1)
#             elif player_1[0] < player_1[1]:
#                 balance1 = plata1 + mesa
#                 print('Ganaste', player_1, 'ahora tienes', balance1)
#         else:
#             player_2.append(random.randint(1,6))
#             if player_2[0] == 1 or player_2[0] == 6:
#                 plata2 -= 100
#                 mesa += 100
#                 player_1.append(random.randint(1,6))
#             elif player_2[0] >= 2 and player_2[0] <= 5:
#                 pedir = str(input('apostar o pasar'))
#                 player_2.append(random.randint(1,6))
#                 if player_2[0] >= player_2[1]:
#                     balance2 = plata2 - mesa
#                     print('Perdiste', player_2, 'te queda', balance2)
#                 elif player_2[0] < player_2[1]:
#                     balance2 = plata2 + mesa
#                     print('Ganaste', player_2, 'ahora tienes', balance2)





# while len(player_1) != 2:
#     player_1.append(random.randint(1,6))
#     if player_1[0] == 1 or player_1[0] == 6:
#         plata1 -= 100
#         mesa += 100
#         print('Pone 100', 'su juego', player_1, 'su dinero', plata1, 'y en la mesa hay', mesa)
#     break
#
# while len(player_2) != 2:
#     player_2.append(random.randint(1,6))
#     if player_2[0] == 1 or player_2[0] == 6:
#         balance = plata2 - 100
#         mesa += 100
#         print('Pone 100', 'su juego', balance2)
#     break
#
# if player_1[0] >= 2 and player_1[0] <= 5:
#     pedir = str(input('apostar o pasar'))
#     if pedir == 'apostar':
#         player_1.append(random.randint(1,6))
#         if player_1[0] >= player_1[1]:
#             nuevo_balance = balance - mesa
#             print('Perdio, su juego', player_1, 'usted tiene', nuevo_balance)
#         elif player_1[0] < player_1[1]:
#             nuevo_balance = balance + mesa
#             print('Jugador 1 Ganaste, tu juego', player_1, 'tienes', nuevo_balance)
#
#     else:
#         print('Este es el dinero de la mesa', mesa)
#         if player_2[0] >= 2 and player_2[0] <= 5:
#             pedir = str(input('apostar o pasar'))
#             if pedir == 'apostar':
#                 player_2.append(random.randint(1,6))
#                 if player_2[0] >= player_2[1]:
#                     nuevo_balance2 = balance2 - mesa
#                     print('Perdio, su juego', player_2, 'usted tiene', nuevo_balance2)
#                 elif player_2[0] < player_2[1]:
#                     nuevo_balance2 = balance2 + mesa
#                     print('Jugador 2 Ganaste, tu juego', player_2, 'tienes', nuevo_balance2)
