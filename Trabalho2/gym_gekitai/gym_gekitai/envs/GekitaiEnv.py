
from typing import Tuple
import gym
from gym import error, spaces, utils, logger
from gym.utils import seeding
import Game
import numpy as np

class GekitaiEasyEnv(gym.Env):

    def __init__(self, board_size=4, game_mode=2, difficulty=2, player=1):
        self.board_size = board_size
        self.player = player
        self.game_mode = game_mode
        self.difficulty = difficulty
        # numero de casas onde se pode colocar uma peça
        self.action_space = spaces.Discrete(board_size*board_size)
        # Tamanho = tamanho da board
        # 0 => Espaço vazio
        # 1 => Peça azul
        # 2 => Peça vermelha
        self.observation_space = gym.spaces.Box(low=0, high=2, shape=(self.board_size, self.board_size), dtype=np.int32)
        
        self.game = Game(board_size, game_mode, difficulty)
    
    
    def reset(self):
        self.game = Game(self.board_size, self.game_mode, self.difficulty)
        
        if self.game.currentPlayer != self.player:
            #chama ou o minimax ou uma jogada random para o adversario do agente
            self.minimax_play()
        
        #para a q table ser capaz de ler (mas ainda nao sei bem como)
        return self.encode_board()
        

    def step(self, action):
        
        #agente joga
        if self.game.currentPlayer==self.player:
            x,y=self.pos_to_coordinates(action)
            self.game.putPiece(self.game.currentPlayer, x, y)
            self.game.atualizar(x,y)
            self.game.setCurrentPlayer(self.game.currentPlayer)
            #ver se o jogo acabou com a jogada
            status = self.game_over_check(self, self.game.board)
            
        #bot joga
        else:
            self.opponent_play()
            self.game.setCurrentPlayer(self.game.currentPlayer)
            #ver se o jogo acabou com a jogada
            status = self.game_over_check(self, self.game.board)
        
        #verifica se alguem ganhou e distribui as rewards
        if status >= 0:
            if status in [1,2]:
                self.done = True
                reward = 1 if status == 1 else -1
            else:
                self.done=False
                reward = 0
            
        return self.encode_board, reward, self.done,{}
    
    #desenha o tabuleiro
    def render(self):
        self.game.display()
        
    def coordinates_to_pos(board_size, x, y):
        return board_size * x + y

    def pos_to_coordinates(board_size, action):
        return action/board_size, action%board_size
        
    def encode_board(self):
        ind = 0

        for i in range(len(self.game.board)):
            for j in range(len(self.game.board[i])):
                ind += self.game.board[i][j].value

        return ind
    
    def minimax_play(self):
        coords=self.game.minMaxAlgortihm()
        self.game.putPiece(self.game.currentPlayer, coords[0], coords[1])
        self.game.atualizar(coords[0], coords[1])
        self.game.setCurrentPlayer(self.game.currentPlayer)        
            
    def game_over_check(self, board):
        if(self.game.player1 == 0):
            return 1
        elif(self.game.player2 == 0):
            return 2
        else:
            return self.verify_winner_by_pieces_in_line(board)
    
    def pieceExist(self, x,  y) :
        if (x > self.board_size-1 or x < 0 or y > self.board_size-1 or y < 0 or self.game.board[x][y] == 0) :
            return False
        else :
            return True
     
    def verify_winner_by_pieces_in_line(self, board):
        aux1=0 
        aux2=0
        
        for i in range(len(board)):
            for j in range(len(board)):
                    if (board[i][j] != 0):
                        if (self.pieceExist(self, i + 1, j) == True and self.pieceExist(self, i + 2, j) == True) :
                            if (board[i][j] == board[i + 1][j] and board[i][j] == board[i + 2][j]) :
                                if (board[i][j] == 1) :
                                    aux2 = 1
                                else :
                                    aux2 = 2
                        if (self.pieceExist(self, i + 1, j + 1) == True and self.pieceExist(self, i + 2, j + 2) == True) :
                            if (board[i][j] == board[i + 1][j + 1] and board[i][j] == board[i + 2][j + 2]) :
                                if (board[i][j] == 1) :
                                    aux2 = 1
                                else :
                                    aux2 = 2
                        if (self.pieceExist(self, i - 1, j + 1) == True and self.pieceExist(self, i - 2, j + 2) == True) :
                            if (board[i][j] == board[i - 1][j + 1] and board[i][j] == board[i - 2][j + 2]) :
                                if (board[i][j] == 1) :
                                    aux2 = 1
                                else :
                                    aux2 = 2
                        if (self.pieceExist(self, i - 1, j) == True and self.pieceExist(self, i - 2, j) == True) :
                            if (board[i][j] == board[i - 1][j] and board[i][j] == board[i - 2][j]) :
                                if (board[i][j] == 1) :
                                    aux2 = 1
                                else :
                                    aux2 = 2
                        if (self.pieceExist(self, i - 1, j - 1) == True and self.pieceExist(self, i - 2, j - 2) == True) :
                            if (board[i][j] == board[i - 1][j - 2] and board[i][j] == self.board[i - 2][j - 2]) :
                                if (board[i][j] == 1) :
                                    aux2 = 1
                                else :
                                    aux2 = 2
                        if (self.pieceExist(self, i, j - 1) == True and self.pieceExist(self, i, j - 2) == True) :
                            if (board[i][j] == board[i][j - 1] and board[i][j] == board[i][j - 2]) :
                                if (board[i][j] == 1) :
                                    aux2 = 1
                                else :
                                    aux2 = 2
                        if (self.pieceExist(self, i + 1, j - 1) == True and self.pieceExist(self, i + 2, j - 2) == True) :
                            if (board[i][j] == board[i + 1][j - 1] and board[i][j] == board[i + 2][j - 2]) :
                                if (board[i][j] == 1) :
                                    aux2 = 1
                                else :
                                    aux2 = 2
                        if (self.pieceExist(self, i, j + 1) == True and self.pieceExist(self, i, j + 2) == True) :
                            if (board[i][j] == board[i][j + 1] and board[i][j] == board[i][j + 2]) :
                                if (board[i][j] == 1) :
                                    aux2 = 1
                                else :
                                    aux2 = 2
            if (aux1!=0):
                if(aux2!=0):
                    return 3
                else:
                    return aux1
            elif(aux2!=0):
                return aux2
            else:
                return 0    