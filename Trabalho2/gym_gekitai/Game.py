#from curses import window
#from locale import LC_MESSAGES
from genericpath import getsize
from turtle import window_height, window_width
import pygame
import numpy as np
import random
import copy

class tree:
    def __init__(self,player1,player2,board,boardSize,currentPlayer,depth):
        self.player1Piece = player1
        self.player2Piece = player2
        self.boardSize = boardSize
        self.depth = depth
        self.board = board
        self.currentPlayer = currentPlayer
        self.terminal=0
        self.j = -1
        self.i = -1
        self.heuristica=0
        self.tree = []
    

    #getters e setters
    def setPlayer1Piece(self,player):
        self.setPlayer1Piece=player

    def setPlayer2Piece(self,player):
        self.setPlayer2Piece=player

    def setI(self,coordenada_i):
        self.i=coordenada_i

    def setJ(self,coordenada_j):
        self.i=coordenada_j

    def setBoard(self, jogo):
        self.algo=jogo
    def setBoardSize(self, size):
        self.boardSize=size

    def getI(self):
        return self.i
    
    def getJ(self):
        return self.j

    def getBoard(self):
        return self.board
    
    def getBoardSize(self):
        return self.boardSize

    def getPlayer1Piece(self):
        return self.player1Piece

    def getPlayer2Piece(self):
        return self.player2Piece
    
    def printBoard(self):
        print(self.Board)

    #heuristica
    def numberPiecesPlayerHeuristic(self):
        return self.getPlayer1Piece()-self.getPlayer1Piece()
    
    def numberPiecesDouble(self):
        return self.numberPiecesDoubleCalc(1)-self.numberPiecesDoubleCalc(2)
    
    def numberPiecesDoubleCalc(self, player):
        aux = 0
        if player == 2:
            for i in range(self.boardSize):
                for j in range(self.boardSize):
                    if not (self.board[i][j] == 'x')and not(self.board[i][j]==' '):
                        if j+1 != self.boardSize and self.board[i][j]==self.board[i][j+1]:
                            aux += 1
                        if j+1 != self.boardSize and i+1 != self.boardSize and self.board[i][j]==self.board[i+1][j+1]:
                            aux +=1
                        if j+1 != self.boardSize and i-1 != -1 and self.board[i][j]==self.board[i-1][j+1]:
                            aux +=1
                        if i+1 != self.boardSize and self.board[i][j]==self.board[i+1][j]:
                            aux += 1
        elif player ==1:
            for i in range(self.boardSize):
                for j in range(self.boardSize):
                    if not (self.board[i][j] == 'o')and not(self.board[i][j]==' '):
                        if j+1 != self.boardSize and self.board[i][j]==self.board[i][j+1]:
                            aux += 1
                        if j+1 != self.boardSize and i+1 != self.boardSize and self.board[i][j]==self.board[i+1][j+1]:
                            aux +=1
                        if j+1 != self.boardSize and i-1 != -1 and self.board[i][j]==self.board[i-1][j+1]:
                            aux +=1
                        if i+1 != self.boardSize and self.board[i][j]==self.board[i+1][j]:
                            aux += 1
        return aux 

    def setHeuristic(self, n):
        if self.terminal != 0:
            if self.terminal == 2:
                self.heuristica=100
            else:
                self.heuristica=-100

        self.heuristica += self.valuePieceHeuristic()+ 2 * self.numberPiecesDouble()
    
    def valuePieceHeuristic(self):
        return self.valuePieceHeuristicCalc(1)-self.valuePieceHeuristicCalc(2)
    
    def  valuePieceHeuristicCalc(self, player):
        value = [[1,1,1,1,1,1],[1,2,2,2,2,1],[1,2,3,3,2,1],[1,2,3,3,2,1],[1,2,2,2,2,1],[1,1,1,1,1,1]];
        aux=0
        for i in range(self.boardSize):
            for j in range(self.boardSize):
                if player==1:
                    if self.board[i][j] == 2:
                        aux += value[i][j]
                else:
                    if self.board[i][j]==1:
                        aux += value[i][j]
        return aux

    def setHeuristicMax(self):
        aux = self.tree[0].heuristica
        treeLength = self.getSize()
        for i in range(1,treeLength):
            aux = max(aux,self.tree[i].heuristica)
        self.heuristica = aux

    def getSize(self):
        count = 0
        for i in self.tree:
            count +=1
        return count

    def setHeuristicMin(self):
        aux = self.tree[0].heuristica
        treeLength = self.getSize()
        for i in range(1,treeLength):
            aux = min(aux,self.tree[i].heuristica)
        self.heuristica = aux
    
    def pieceExist(self,x,y):
        if x > self.boardSize-1 or x < 0 or y > self.boardSize-1 or y < 0 or self.board[x][y] == 0 :
            return False
        else:
            return True

    def putPiece(self,player,x,y):
        if(player==1):
            self.board[x][y]=1
            self.player1Piece-=1
            
        else:
            self.board[x][y]=2
            self.player2Piece-=1
    
    def setCurrentPlayer(self,player):
        if player == 1:
            self.currentPlayer=2
        elif player == 2:
            self.currentPlayer=1

    def deletePiece(self,x,y):
        if self.board[x][y]==1 :
            self.board[x][y]=0
            self.player1Piece+=1
            return 1
        else:
            self.board[x][y]=0
            self.player2Piece+=1
            return 2

    def atualizar(self,x,y):
        if self.pieceExist(x+1,y) == True and self.pieceExist(x+2,y) == False:
            aux = self.deletePiece(x+1,y)
            if (x+2 < self.boardSize and x+2 > -1) and (y<self.boardSize and y>-1):
                self.putPiece(aux,x+2,y)
        
        if self.pieceExist(x+1,y+1) == True and self.pieceExist(x+2,y+2) == False:
            aux = self.deletePiece(x+1,y+1)
            if (x+2 < self.boardSize and x+2 > -1) and (y+2<self.boardSize and y+2>-1):
                self.putPiece(aux,x+2,y+2)
    
        if self.pieceExist(x,y+1) == True and self.pieceExist(x,y+2) == False:
            aux = self.deletePiece(x,y+1)
            if (x < self.boardSize and x > -1) and (y+2<self.boardSize and y+2>-1):
                self.putPiece(aux,x,y+2)

        if self.pieceExist(x-1,y+1) == True and self.pieceExist(x-2,y+2) == False:
            aux = self.deletePiece(x-1,y+1)
            if (x-2 < self.boardSize and x-2 > -1) and (y+2<self.boardSize and y+2>-1):
                self.putPiece(aux,x-2,y+2)

        if self.pieceExist(x-1,y) == True and self.pieceExist(x-2,y) == False:
            aux = self.deletePiece(x-1,y)
            if(x-2 < self.boardSize and x-2 > -1) and (y < self.boardSize and y>-1):
                self.putPiece(aux,x-2,y)

        if self.pieceExist(x-1,y-1) == True and self.pieceExist(x-2,y-2) == False:
            aux = self.deletePiece(x-1,y-1)
            if (x-2 < self.boardSize and x-2 > -1) and (y-2 < self.boardSize and y-2 > -1):
                self.putPiece(aux,x-2,y-2)

        if self.pieceExist(x,y-1) == True and self.pieceExist(x,y-2) == False:
            aux = self.deletePiece(x,y-1)
            if (x < self.boardSize and x > -1) and (y-2 < self.boardSize and y-2>-1):
                self.putPiece(aux,x,y-2)

        if self.pieceExist(x+1,y-1) == True and self.pieceExist(x+2,y-2) == False:
            aux = self.deletePiece(x+1,y-1)
            if (x+2 < self.boardSize and x+2 > -1) and (y-2 < self.boardSize and y-2>-1):
                self.putPiece(aux,x+2,y-2)

    def verifyWinner(self) :
        aux1 = 0
        aux2 = 0
        # aux1-winner by 8 pieces on board aux2-winner by 3 in a row on board
        if (self.player1Piece == 0) :
            aux1 = 1
        elif(self.player2Piece == 0) :
            aux1 = 2
            
        for i in range(self.boardSize):
            for j in range(self.boardSize):
                if (self.board[i][j] != 0) :
                    if (self.pieceExist(i + 1, j) == True and self.pieceExist(i + 2, j) == True) :
                        if (self.board[i][j] == self.board[i + 1][j] and self.board[i][j] == self.board[i + 2][j]) :
                            if (self.board[i][j] == 1) :
                                aux2 = 1
                            else :
                                aux2 = 2
                    if (self.pieceExist(i + 1, j + 1) == True and self.pieceExist(i + 2, j + 2) == True) :
                        if (self.board[i][j] == self.board[i + 1][j + 1] and self.board[i][j] == self.board[i + 2][j + 2]) :
                            if (self.board[i][j] == 1) :
                                aux2 = 1
                            else :
                                aux2 = 2
                    if (self.pieceExist(i - 1, j + 1) == True and self.pieceExist(i - 2, j + 2) == True) :
                        if (self.board[i][j] == self.board[i - 1][j + 1] and self.board[i][j] == self.board[i - 2][j + 2]) :
                            if (self.board[i][j] == 1) :
                                aux2 = 1
                            else :
                                aux2 = 2
                    if (self.pieceExist(i - 1, j) == True and self.pieceExist(i - 2, j) == True) :
                        if (self.board[i][j] == self.board[i - 1][j] and self.board[i][j] == self.board[i - 2][j]) :
                            if (self.board[i][j] == 1) :
                                aux2 = 1
                            else :
                                aux2 = 2
                    if (self.pieceExist(i - 1, j - 1) == True and self.pieceExist(i - 2, j - 2) == True) :
                        if (self.board[i][j] == self.board[i - 1][j - 2] and self.board[i][j] == self.board[i - 2][j - 2]) :
                            if (self.board[i][j] == 1) :
                                aux2 = 1
                            else :
                                aux2 = 2
                    if (self.pieceExist(i, j - 1) == True and self.pieceExist(i, j - 2) == True) :
                        if (self.board[i][j] == self.board[i][j - 1] and self.board[i][j] == self.board[i][j - 2]) :
                            if (self.board[i][j] == 1) :
                                aux2 = 1
                            else :
                                aux2 = 2
                    if (self.pieceExist(i + 1, j - 1) == True and self.pieceExist(i + 2, j - 2) == True) :
                        if (self.board[i][j] == self.board[i + 1][j - 1] and self.board[i][j] == self.board[i + 2][j - 2]) :
                            if (self.board[i][j] == 1) :
                                aux2 = 1
                            else :
                                aux2 = 2
                    if (self.pieceExist(i, j + 1) == True and self.pieceExist(i, j + 2) == True) :
                        if (self.board[i][j] == self.board[i][j + 1] and self.board[i][j] == self.board[i][j + 2]) :
                            if (self.board[i][j] == 1) :
                                aux2 = 1
                            else :
                                aux2 = 2
        # win(player int),draw=3,continue=0
        if (aux1 != 0) :
            if (aux2 != 0) :
                return 3
            return aux1
        elif(aux2 != 0) :
            return aux2
        else :
            return 0

    def getIJ(self):
        for i in range (0,self.getSize()):
            if self.heuristica==self.tree[i].heuristica:
                return [self.tree[i].i,self.tree[i].j]




    def expande(self,depth,n):
        if depth >= 0:
            for i in range(self.boardSize):
                for j in range(self.boardSize):
                    if self.pieceExist(i,j) == False:
                        node = tree(copy.deepcopy(self.player1Piece),copy.deepcopy(self.player2Piece),copy.deepcopy(self.board),copy.deepcopy(self.boardSize),copy.deepcopy(self.currentPlayer),copy.deepcopy(self.depth))
                        node.putPiece(self.currentPlayer,i,j)
                        node.i=i
                        node.j=j
                        node.setCurrentPlayer(self.currentPlayer)
                        node.atualizar(i,j)
                        if(node.verifyWinner()==1):
                            node.terminal=1
                        if(node.verifyWinner()==2):
                            node.terminal=2
                        self.tree.append(node)
                        if(node.terminal==0):
                            node.expande(depth-1,n)
                        if depth==0 or node.terminal != 0:
                            node.setHeuristic(n)
                        
            if self.currentPlayer==1:
                self.setHeuristicMin()
            else:
                self.setHeuristicMax()

                        

  



class Game:    
    
    def __init__(self, board_size, game_mode, difficulty) :
        self.player1 = 8
        self.player2 = 8
        self.currentPlayer = 1
        #self.gameMode = self.main_menu()
        self.game_mode = game_mode
        #self.board_size = self.menu_size_board()
        self.board_size = board_size
        self.difficulty = difficulty
        self.board = [[0] * (self.board_size) for _ in range(self.board_size)] 
        self.gekitai_gui()
        #self.play()
    
    def gekitai_gui(self):
        pygame.init()
        self.quit = False
        window_width = 840
        window_height= 800
        self.window = pygame.display.set_mode((window_width,window_height))
        self.buttons = [[i for i in range(self.board_size)] for j in range(self.board_size)]
        #for i in range(len(self.board)):
        #    for j in range(len(self.board[i])):
        #        self.buttons[i][j] = pygame.draw.rect(self.window, ((i+j)%2*255, (i+j)%2*255, (i+j)%2*255), (20+j*100, 20+i*100, 100, 100))
        
    def display(self):
        self.draw()
        
    #desenha o tabuleiro e chama a funcao que inicia o jogo baseado no tipo de jogo escolhido    
    #def play(self):
        #self.active_player = random.randint(1,2)
        #print(self.active_player)
        #self.quit = False
        #for i in range(len(self.board)):
        #    for j in range(len(self.board[i])):
        #        self.buttons[i][j] = pygame.draw.rect(self.window, ((i+j)%2*255, (i+j)%2*255, (i+j)%2*255), (20+j*100, 20+i*100, 100, 100))
        #self.draw()
        #if gameType == 1:
        #    self.playPVP()
        #elif gameType == 2:
        #    self.playPVE()
        #elif gameType == 3:
        #    return
        
    #Jogo humano contra humano    
    def playPVP(self):
        #while (self.verifyWinner() == 0 or self.quit==False):
        self.gameControl()
        
    #funcao que desenha o menu principal
    def main_menu(self):
        self.font = pygame.font.SysFont("arial", 72)
        self.window.fill((60,50,20))
        self.menu_buttons = [0,0,0]
        i=0
        #desenha botoes
        for i in range(3):
            self.menu_buttons[i]=pygame.draw.rect(self.window, (255,255,255), (270, 200+i*120, 300, 100))
        
        #escreve texto nofmins botoes
        text = self.font.render("P x P", True, (0, 0, 0))
        self.window.blit(text, (355, 210))
        text = self.font.render("P x C", True, (0, 0, 0))
        self.window.blit(text, (355, 330))
        text = self.font.render("C x C", True, (0, 0, 0))
        self.window.blit(text, (355, 450))
        pygame.display.flip()
        while True:
            for event in pygame.event.get():
                #fechando a janela
                if event.type == pygame.QUIT:
                    self.quit = True
                    return
                #teclado
                elif event.type == pygame.KEYDOWN:
                    #carregar na tecla r
                    if event.key == pygame.K_r:
                        self.play()
                    #carragear na tecla m
                    elif event.key == pygame.K_m:
                        self.__init__()
                #botoes
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    pos = pygame.mouse.get_pos()
                    for i in range(len(self.menu_buttons)):
                        if self.menu_buttons[i].collidepoint(pos):
                            y_pos=pos[1]
                            difficulty=0
                            #botao Humano X Humano
                            if y_pos<=300 and y_pos>=200:
                                return [1, difficulty]
                            elif y_pos<=420 and y_pos>=320:
                                return [2,1] #set dificult
                            elif y_pos<=540 and y_pos>=420:
                                return [3,1] #set dificult
    
    #Funcao que desenha o menu de escolha do tamanho do tabuleiro
    def menu_size_board(self):
        if self.quit:
            return
        self.font = pygame.font.SysFont("arial", 72)
        self.window.fill((60,50,20))
        self.menu_buttons = [0,0,0,0]
        
        i = 0
        for i in range(2):
            self.menu_buttons[i] = pygame.draw.rect(self.window, (255, 255, 255), (270, 200+i*120, 300, 100))  
        
        text = self.font.render("Board size", True, (0, 0, 0))
        self.window.blit(text, (280, 100))
        text = self.font.render("4x4", True, (0, 0, 0))
        self.window.blit(text, (370, 210))
        text = self.font.render("6x6", True, (0, 0, 0))
        self.window.blit(text, (370, 330))
        pygame.display.flip()
        while not self.quit:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.quit = True
                    return
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        self.play()
                    elif event.key == pygame.K_t:
                        self.tip()
                    elif event.key == pygame.K_m:
                        self.__init__()
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    pos = pygame.mouse.get_pos()
                    for i in range(len(self.menu_buttons)):
                            if self.menu_buttons[i].collidepoint(pos):
                                y_pos=pos[1]
                                if y_pos<=300 and y_pos>=200:
                                    return 4
                                elif y_pos<=420 and y_pos>=320:
                                    return 6
    
    #funcao que desenha o tabuleiro (chamada a cada mudança)
    def draw(self):
        self.window.fill((60,50,20))
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                pygame.draw.rect(self.window, ((i+j)%2*255, (i+j)%2*255, (i+j)%2*255), (20+j*100, 20+i*100, 100, 100))
                if self.board[i][j] == 1:
                    pygame.draw.circle(self.window, (200,0,0), ((70+j*100, 70+i*100)), 45)
                elif self.board[i][j] == 2:
                    pygame.draw.circle(self.window, (0,0,200), (70+j*100, 70+i*100), 45)
        pygame.display.flip()
    
    #processa os cliques no ecra como jogadas e controla o flow do jogo
    def gameControl(self):
        while (self.verifyWinner() == 0):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.quit = True
                    return False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    #when the mouse button is pressed get it's position
                    pointerPosition = pygame.mouse.get_pos()
                    #check which button was pressed
                    for i in range(len(self.buttons)):
                        for j in range(len(self.buttons[i])):
                            if self.buttons[i][j].collidepoint(pointerPosition):
                                if(i < 0 or i>self.board_size-1 or j<0 or j>self.board_size-1 or self.pieceExist(i,j)==True):
                                    print("Coordenada nao valida.")
                                else:    
                                    self.putPiece(self.currentPlayer, i, j)
                                    self.atualizar(i,j)
                                    self.setCurrentPlayer(self.currentPlayer)
                                    self.draw()
                                    #return True
                                
        self.gameOverScreen(self.verifyWinner())
    
    def playPVE(self):
        self.gameControlVsBot()

    def gameControlVsBot(self):
        while (self.verifyWinner() == 0):
            self.draw()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.quit = True
                    return False
                elif self.currentPlayer == 1:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        #when the mouse button is pressed get it's position
                        pointerPosition = pygame.mouse.get_pos()
                        #check which button was pressed
                        for i in range(len(self.buttons)):
                            for j in range(len(self.buttons[i])):
                                if self.buttons[i][j].collidepoint(pointerPosition):
                                    if(i < 0 or i>self.board_size-1 or j<0 or j>self.board_size-1 or self.pieceExist(i,j)==True):
                                        print("Coordenada nao valida.")
                                    else:    
                                        self.putPiece(self.currentPlayer, i, j)
                                        self.atualizar(i,j)
                                        self.setCurrentPlayer(self.currentPlayer)
                                        self.draw()
                                    #return True
                elif self.currentPlayer==2:
                    self.draw()
                    jogado = False
                    jogada = self.minMaxAlgortihm()
                    self.putPiece(self.currentPlayer, jogada[0], jogada[1])
                    self.atualizar(jogada[0], jogada[1])
                    self.setCurrentPlayer(self.currentPlayer)
                    self.draw()
                                
        self.gameOverScreen(self.verifyWinner())
    
    def minMaxAlgortihm(self):
        #aqui
        #selfCopy.putPiece(selfCopy.currentPlayer,1,2)
        algo1 = tree(copy.deepcopy(self.player1),copy.deepcopy(self.player2),copy.deepcopy(self.board),copy.deepcopy(self.board_size),copy.deepcopy(self.currentPlayer),2)
        algo1.expande(2,1)
        teste = algo1.getIJ()
        del algo1
        return [teste[0],teste[1]]
        #return [algo1.getI,algo1.getJ]


    #desenha o ecrã de game over   
    def gameOverScreen(self, winner):
        self.font = pygame.font.SysFont("arial", 72)
        pygame.draw.rect(self.window, (82,255,123), (150, 200, 600, 400))
        text = self.font.render("Game Over", True, (0, 0, 0))
        self.window.blit(text, (295, 220))
        text = self.font.render("Player " + str(winner) +" wins", True, (0, 0, 0))
        self.window.blit(text, (275, 330))
        text = pygame.font.SysFont("arial", 50).render("Press M to return to the menu", True, (0, 0, 0))
        self.window.blit(text, (175, 440))
        text = pygame.font.SysFont("arial", 50).render("or esc to quit", True, (0, 0, 0))
        self.window.blit(text, (320, 520))
        
        pygame.display.flip()
        while self.quit==False:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.quit = True
                    return
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_m:
                        self.__init__()
                    elif event.key == pygame.K_ESCAPE:
                        self.quit=True
                        return
                        
    def  toString(self) :
        aux = " |0|1|2|3|4|5|\n"
        for i in range(6):
            aux += str(i) + "|"
            for j in range(6):
                aux += self.board[i][j] + "|"
            aux += "\n"
        return aux
    
    #devolve o estado atual da board
    def getBoard(self) :
        return self.board
    
    #devolve o nr de pecas do player1
    def getPlayer1(self) :
        return self.player1
    
    #devolve o nr de pecas do player2
    def getPlayer2(self) :
        return self.player2
    
    #verifica se as coordenadas indicadas são válidas no estado atual do tabuleiro
    def pieceExist(self, x,  y) :
        if (x > self.board_size-1 or x < 0 or y > self.board_size-1 or y < 0 or self.board[x][y] == 0) :
            return False
        else :
            return True
        
    
    def putPiece(self, player,  x,  y) :
        if (player == 1) :
            self.board[x][y] = 1
            self.player1 -= 1
        else :
            self.board[x][y] = 2
            self.player2 -= 1
            
    def deletePiece(self, x,  y) :
        if (self.board[x][y] == 1) :
            self.board[x][y] = 0
            self.player1 += 1
            return 1
        else :
            self.board[x][y] = 0
            self.player2 += 1
            return 2
        
    def atualizar(self, x,  y) :
        if (self.pieceExist(x + 1, y) == True and self.pieceExist(x + 2, y) == False) :
            aux = self.deletePiece(x + 1, y)
            if ((x + 2 < self.board_size and x + 2 > -1) and (y < self.board_size and y > -1)) :
                self.putPiece(aux, x + 2, y)
        if (self.pieceExist(x + 1, y + 1) == True and self.pieceExist(x + 2, y + 2) == False) :
            aux = self.deletePiece(x + 1, y + 1)
            if ((x + 2 < self.board_size and x + 2 > -1) and (y + 2 < self.board_size and y + 2 > -1)) :
                self.putPiece(aux, x + 2, y + 2)
        if (self.pieceExist(x, y + 1) == True and self.pieceExist(x, y + 2) == False) :
            aux = self.deletePiece(x, y + 1)
            if ((x < self.board_size and x > -1) and (y + 2 < self.board_size and y + 2 > -1)) :
                self.putPiece(aux, x, y + 2)
        if (self.pieceExist(x - 1, y + 1) == True and self.pieceExist(x - 2, y + 2) == False) :
            aux = self.deletePiece(x - 1, y + 1)
            if ((x - 2 < self.board_size and x - 2 > -1) and (y + 2 < self.board_size and y + 2 > -1)) :
                self.putPiece(aux, x - 2, y + 2)
        if (self.pieceExist(x - 1, y) == True and self.pieceExist(x - 2, y) == False) :
            aux = self.deletePiece(x - 1, y)
            if ((x - 2 < self.board_size and x - 2 > -1) and (y < self.board_size and y > -1)) :
                self.putPiece(aux, x - 2, y)
        if (self.pieceExist(x - 1, y - 1) == True and self.pieceExist(x - 2, y - 2) == False) :
            aux = self.deletePiece(x - 1, y - 1)
            if ((x - 2 < self.board_size and x - 2 > -1) and (y - 2 < self.board_size and y - 2 > -1)) :
                self.putPiece(aux, x - 2, y - 2)
        if (self.pieceExist(x, y - 1) == True and self.pieceExist(x, y - 2) == False) :
            aux = self.deletePiece(x, y - 1)
            if ((x < self.board_size and x > -1) and (y - 2 < self.board_size and y - 2 > -1)) :
                self.putPiece(aux, x, y - 2)
        if (self.pieceExist(x + 1, y - 1) == True and self.pieceExist(x + 2, y - 2) == False) :
            aux = self.deletePiece(x + 1, y - 1)
            if ((x + 2 < self.board_size and x + 2 > -1) and (y - 2 < self.board_size and y - 2 > -1)) :
                self.putPiece(aux, x + 2, y - 2)
                
    def verifyWinner(self) :
        aux1 = 0
        aux2 = 0
        # aux1-winner by 8 pieces on board aux2-winner by 3 in a row on board
        if (self.player1 == 0) :
            aux1 = 1
        elif(self.player2 == 0) :
            aux1 = 2
            
        for i in range(self.board_size):
            for j in range(self.board_size):
                if (self.board[i][j] != 0) :
                    if (self.pieceExist(i + 1, j) == True and self.pieceExist(i + 2, j) == True) :
                        if (self.board[i][j] == self.board[i + 1][j] and self.board[i][j] == self.board[i + 2][j]) :
                            if (self.board[i][j] == 1) :
                                aux2 = 1
                            else :
                                aux2 = 2
                    if (self.pieceExist(i + 1, j + 1) == True and self.pieceExist(i + 2, j + 2) == True) :
                        if (self.board[i][j] == self.board[i + 1][j + 1] and self.board[i][j] == self.board[i + 2][j + 2]) :
                            if (self.board[i][j] == 1) :
                                aux2 = 1
                            else :
                                aux2 = 2
                    if (self.pieceExist(i - 1, j + 1) == True and self.pieceExist(i - 2, j + 2) == True) :
                        if (self.board[i][j] == self.board[i - 1][j + 1] and self.board[i][j] == self.board[i - 2][j + 2]) :
                            if (self.board[i][j] == 1) :
                                aux2 = 1
                            else :
                                aux2 = 2
                    if (self.pieceExist(i - 1, j) == True and self.pieceExist(i - 2, j) == True) :
                        if (self.board[i][j] == self.board[i - 1][j] and self.board[i][j] == self.board[i - 2][j]) :
                            if (self.board[i][j] == 1) :
                                aux2 = 1
                            else :
                                aux2 = 2
                    if (self.pieceExist(i - 1, j - 1) == True and self.pieceExist(i - 2, j - 2) == True) :
                        if (self.board[i][j] == self.board[i - 1][j - 2] and self.board[i][j] == self.board[i - 2][j - 2]) :
                            if (self.board[i][j] == 1) :
                                aux2 = 1
                            else :
                                aux2 = 2
                    if (self.pieceExist(i, j - 1) == True and self.pieceExist(i, j - 2) == True) :
                        if (self.board[i][j] == self.board[i][j - 1] and self.board[i][j] == self.board[i][j - 2]) :
                            if (self.board[i][j] == 1) :
                                aux2 = 1
                            else :
                                aux2 = 2
                    if (self.pieceExist(i + 1, j - 1) == True and self.pieceExist(i + 2, j - 2) == True) :
                        if (self.board[i][j] == self.board[i + 1][j - 1] and self.board[i][j] == self.board[i + 2][j - 2]) :
                            if (self.board[i][j] == 1) :
                                aux2 = 1
                            else :
                                aux2 = 2
                    if (self.pieceExist(i, j + 1) == True and self.pieceExist(i, j + 2) == True) :
                        if (self.board[i][j] == self.board[i][j + 1] and self.board[i][j] == self.board[i][j + 2]) :
                            if (self.board[i][j] == 1) :
                                aux2 = 1
                            else :
                                aux2 = 2
        # win(player int),draw=3,continue=0
        if (aux1 != 0) :
            if (aux2 != 0) :
                return 3
            return aux1
        elif(aux2 != 0) :
            return aux2
        else :
            return 0
        
    def setBoard(self, i) :
        self.board = i
        
    def setCurrentPlayer(self, i) :
        if (i == 1) :
            self.currentPlayer = 2
        else :
            self.currentPlayer = 1

Game(4, 2, 2)