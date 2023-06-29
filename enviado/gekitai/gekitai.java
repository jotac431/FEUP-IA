import java.util.*;

class Game{
  String board[][];
  int player1;
  int player2;
  int currentPlayer;
  Game(){
    this.board = new String[6][6];
    for (int i=0;i<6;i++){
      for (int j=0;j<6;j++){
        board[i][j] = " ";
      }
    }
    player1=8;
    player2=8;
    currentPlayer=0;
  }
  Game(String[][] board, int player1, int player2){
    this.board = new String[6][6];
    for (int i=0;i<6;i++){
      for (int j=0;j<6;j++){
        this.board[i][j] = board[i][j];
      }
    }
    this.player1=player1;
    this.player2=player2;
  }
  public String toString(){
    String aux = " |0|1|2|3|4|5|\n";
    for (int i=0;i<6;i++){
      aux += i+"|";
      for (int j=0;j<6;j++){
        aux += board[i][j] + "|";
      }
      aux+="\n";
    }
    return aux;
  }
  public String[][] getBoard(){ return board;}
  public int getPlayer1(){ return player1;}
  public int getPlayer2(){ return player2;}
  public boolean pieceExist(int x,int y){
    if(x > 5 || x < 0 || y>5||y<0||board[x][y] == " "){
      return false;
    }
    else{
      return true;
    }
  }
  public void putPiece(int player,int x,int y){
    if(player==1){
      this.board[x][y]="x";
      this.player1--;
    }
    else{
      this.board[x][y]="o";
      this.player2--;
    }
  }
  public int deletePiece(int x,int y){
    if(board[x][y]=="x"){
      board[x][y]=" ";
      player1++;
      return 1;
    }
    else{
      board[x][y]=" ";
      player2++;
      return 2;
    }
  }
  public void atualizar(int x,int y){
    if(pieceExist(x+1,y)==true&& pieceExist(x+2,y) == false){
      int aux = deletePiece(x+1,y);
      if((x+2 < 6 && x+2 > -1) && (y<6&&y>-1)){
        putPiece(aux,x+2,y);
      }
    }
    if(pieceExist(x+1,y+1)==true&& pieceExist(x+2,y+2) == false){
      int aux = deletePiece(x+1,y+1);
      if((x+2 < 6 && x+2 > -1) && (y+2<6&&y+2>-1)){
        putPiece(aux,x+2,y+2);
      }
    }
    if(pieceExist(x,y+1)==true&& pieceExist(x,y+2) == false){
      int aux = deletePiece(x,y+1);
      if((x < 6 && x > -1) && (y+2<6&&y+2>-1)){
        putPiece(aux,x,y+2);
      }
    }
    if(pieceExist(x-1,y+1)==true&& pieceExist(x-2,y+2) == false){
      int aux = deletePiece(x-1,y+1);
      if((x-2 < 6 && x-2 > -1) && (y+2<6&&y+2>-1)){
        putPiece(aux,x-2,y+2);
      }
    }
    if(pieceExist(x-1,y)==true&& pieceExist(x-2,y) == false){
      int aux = deletePiece(x-1,y);
      if((x-2 < 6 && x-2 > -1) && (y<6&&y>-1)){
        putPiece(aux,x-2,y);
      }
    }
    if(pieceExist(x-1,y-1)==true&& pieceExist(x-2,y-2) == false){
      int aux = deletePiece(x-1,y-1);
      if((x-2 < 6 && x-2 > -1) && (y-2<6&&y-2>-1)){
        putPiece(aux,x-2,y-2);
      }
    }
    if(pieceExist(x,y-1)==true&& pieceExist(x,y-2) == false){
      int aux = deletePiece(x,y-1);
      if((x < 6 && x > -1) && (y-2<6&&y-2>-1)){
        putPiece(aux,x,y-2);
      }
    }
    if(pieceExist(x+1,y-1)==true&& pieceExist(x+2,y-2) == false){
      int aux = deletePiece(x+1,y-1);
      if((x+2 < 6 && x+2 > -1) && (y-2<6&&y-2>-1)){
        putPiece(aux,x+2,y-2);
      }
    }
  }
  public int verifyWinner(){
    int aux1=0;
    int aux2=0; //aux1-winner by 8 pieces on board aux2-winner by 3 in a row on board
    if(player1==0){
      aux1=1;
    }
    else if(player2==0){
      aux1=2;
    }
    for(int i=0;i<6;i++){
      for(int j=0;j<6;j++){
        if(board[i][j]!=" "){
          if(pieceExist(i+1,j)==true&&pieceExist(i+2,j)==true){
            if(board[i][j]==board[i+1][j]&&board[i][j]==board[i+2][j]){
              if(board[i][j]=="x"){
                aux2=1;
              }
              else{
                aux2=2;
              }
            }
          }

          if(pieceExist(i+1,j+1)==true&&pieceExist(i+2,j+2)==true){
            if(board[i][j]==board[i+1][j+1]&&board[i][j]==board[i+2][j+2]){
              if(board[i][j]=="x"){
                aux2=1;
              }
              else{
                aux2=2;
              }
            }
          }

          if(pieceExist(i-1,j+1)==true&&pieceExist(i-2,j+2)==true){
            if(board[i][j]==board[i-1][j+1]&&board[i][j]==board[i-2][j+2]){
              if(board[i][j]=="x"){
                aux2=1;
              }
              else{
                aux2=2;
              }
            }
          }

          if(pieceExist(i-1,j)==true&&pieceExist(i-2,j)==true){
            if(board[i][j]==board[i-1][j]&&board[i][j]==board[i-2][j]){
              if(board[i][j]=="x"){
                aux2=1;
              }
              else{
                aux2=2;
              }
            }
          }

          if(pieceExist(i-1,j-1)==true&&pieceExist(i-2,j-2)==true){
            if(board[i][j]==board[i-1][j-2]&&board[i][j]==board[i-2][j-2]){
              if(board[i][j]=="x"){
                aux2=1;
              }
              else{
                aux2=2;
              }
            }
          }

          if(pieceExist(i,j-1)==true&&pieceExist(i,j-2)==true){
            if(board[i][j]==board[i][j-1]&&board[i][j]==board[i][j-2]){
              if(board[i][j]=="x"){
                aux2=1;
              }
              else{
                aux2=2;
              }
            }
          }

          if(pieceExist(i+1,j-1)==true&&pieceExist(i+2,j-2)==true){
            if(board[i][j]==board[i+1][j-1]&&board[i][j]==board[i+2][j-2]){
              if(board[i][j]=="x"){
                aux2=1;
              }
              else{
                aux2=2;
              }
            }
          }

          if(pieceExist(i,j+1)==true&&pieceExist(i,j+2)==true){
            if(board[i][j]==board[i][j+1]&&board[i][j]==board[i][j+2]){
              if(board[i][j]=="x"){
                aux2=1;
              }
              else{
                aux2=2;
              }
            }
          }
        }
      }
    }
    //win(player int),draw=3,continue=0
    if(aux1!=0){
      if(aux2!=0){
        return 3;
      }
      return aux1;
    }
    else if(aux2!=0){
      return aux2;
    }
    else{
      return 0;
    }
  }
  public void setBoard(String[][] i){
    this.board=i;
  }
  public void setCurrentPlayer(int i){
    if(i==1){
      currentPlayer=2;
    }
    else{
      currentPlayer=1;
    }
  }
}

class MinMaxTree{
  Game state;
  List<MinMaxTree> nodeList; 
  int heuristica;
  int terminal;
  MinMaxTree(Game dadState){
    state = new Game(dadState.getBoard(),dadState.getPlayer1(),dadState.getPlayer2());
    nodeList = new ArrayList<>();
    terminal = 0;
  }
  public int numberPiecesPlayerHeuristic(){
    return state.getPlayer1()-state.getPlayer2();
  }
  public int numberPiecesDouble(){
    return numberPiecesDoubleCalc(1)-numberPiecesDoubleCalc(2);
  }
  public int numberPiecesDoubleCalc(int jogador){
    int aux=0;
    if(jogador==2){
      for(int i=0;i<6;i++){
        for(int j=0;j<6;j++){
          if(!state.board[i][j].equals("x")&&!state.board[i][j].equals(" ")){
            if(j+1!=6 &&state.board[i][j].equals(state.board[i][j+1])){
              aux++;
            }
            if(j+1!=6 && i+1!=6 &&state.board[i][j].equals(state.board[i+1][j+1])){
              aux++;
            }
            if(j+1!=6 && i-1!=-1 &&state.board[i][j].equals(state.board[i-1][j+1])){
              aux++;
            }
            if(i+1!=6 && state.board[i][j].equals(state.board[i+1][j])){
              aux++;
            }
          }
        }
      }
    }
    else{
      for(int i=0;i<6;i++){
        for(int j=0;j<6;j++){
          if(!state.board[i][j].equals("o")&&!state.board[i][j].equals(" ")){
            if(j+1!=6 && state.board[i][j].equals(state.board[i][j+1])){
              aux++;
            }
            if(j+1!=6 && i+1!=6 && state.board[i][j].equals(state.board[i+1][j+1])){
              aux++;
            }
            if(j+1!=6 && i-1!=-1 &&state.board[i][j].equals(state.board[i-1][j+1])){
              aux++;
            }
            if(i+1!=6 && state.board[i][j].equals(state.board[i+1][j])){
              aux++;
            }
          }
        }
      }
    }
    return aux;
  }
  public void expande(int depth){
    if(depth>=0){
      for(int i =0;i<6;i++){
        for(int j = 0;j<6;j++){
          if(!this.state.pieceExist(i,j)){
            MinMaxTree node = new MinMaxTree(this.state);
            node.state.putPiece(this.state.currentPlayer,i,j);
            node.state.setCurrentPlayer(this.state.currentPlayer);
            node.state.atualizar(i, j);
            if(node.state.verifyWinner()==1){
              node.terminal=1;
            }
            if(node.state.verifyWinner()==2){
              node.terminal=2;
            }
            this.nodeList.add(node);
            //System.out.println(node.state);
            //System.out.println(node.heuristica);
            if(node.terminal==0){
              node.expande(depth-1);
            }
            if(depth==0||node.terminal!=0){
              node.setHeuristic();
            }
          }
        }
      }
      if(this.state.currentPlayer==1){
        setHeuristicMin();
      }
      else
        setHeuristicMax();
      }
    }    
  public void setHeuristic(){
    if(terminal!=0){
      if(terminal==2)
        heuristica = 100;
      else
        heuristica = -100;
    }
    //heuristica += numberPiecesPlayerHeuristic()+ 2 * numberPiecesDouble();
    heuristica += valuePieceHeuristic()+ 2 * numberPiecesDouble();
  }
  public int valuePieceHeuristicCalc(int player){
    int value[][] = {{1,1,1,1,1,1},{1,2,2,2,2,1},{1,2,3,3,2,1},{1,2,3,3,2,1},{1,2,2,2,2,1},{1,1,1,1,1,1}};
    int aux=0;
    for(int i=0;i<6;i++){
      for(int j=0;j<6;j++){
        if(player==1){
          if(state.board[i][j].equals("o")){
            aux+=value[i][j];
          }
        }
        else{
          if(state.board[i][j].equals("x")){
            aux+=value[i][j];
          }
        }
      }
    }
    return aux;
  }
  public int valuePieceHeuristic(){
    return valuePieceHeuristicCalc(1)-valuePieceHeuristicCalc(2);
  }
  public void setHeuristicMax(){
    int aux = nodeList.get(0).heuristica;
    for(int i=1;i<nodeList.size();i++){
      aux = Math.max(aux,nodeList.get(i).heuristica);
    }
    this.heuristica = aux;
  }
  public void setHeuristicMin(){
    int aux = nodeList.get(0).heuristica;
    for(int i=1;i<nodeList.size();i++){
      aux = Math.min(aux,nodeList.get(i).heuristica);
    }
    this.heuristica = aux;
  }
}
public class gekitai{
  public static void main(String[] args){
    Scanner keyboard = new Scanner(System.in);
    int aux;
    while(true){
      System.out.print("\033[H\033[2J");
      System.out.println("   GEKITAI\n");
      System.out.println("Escolha o modo de jogo");
      System.out.println("1) Player vs Player");
      System.out.println("2) Player vs Computer");
      aux = keyboard.nextInt();
      if(aux==1)
        PlayerVsPlayer(keyboard);
      else if(aux==2)
        PlayerVsComputer(keyboard);
      else{
        System.out.print("\033[H\033[2J");
        System.out.println("   GEKITAI\n");
        System.out.println("Escolha o modo de jogo");
        System.out.println("1) Player vs Player");
        System.out.println("2) Player vs Computer");
        System.out.println("Escolha uma opção valida");
        aux = keyboard.nextInt();
      }
    }
  }

  public static void PlayerVsComputer(Scanner keyboard){
    System.out.print("\033[H\033[2J");
    System.out.println("   GEKITAI\n");
    System.out.println("Nivel de dificuldade");
    System.out.println("1) Easy");
    System.out.println("3) Hard");
    int dificuldade;
    dificuldade = keyboard.nextInt();
    if(dificuldade!=1 && dificuldade!=3){
      System.out.print("\033[H\033[2J");
      System.out.println("   GEKITAI\n");
      System.out.println("Nivel de dificuldade");
      System.out.println("1) Easy");
      System.out.println("3) Hard");
      System.out.println("Só pode ser 1 ou 3");
      dificuldade = keyboard.nextInt();
    }
    Game um = new Game();
    int x,y;
    Random ran = new Random();
    MinMaxTree dois;
    um.setCurrentPlayer(ran.nextInt(2)+1);
    while(um.verifyWinner()==0){
      if(um.currentPlayer==1){
        printGame(um);
        System.out.println("\nJoga o jogador "+um.currentPlayer);
        System.out.println("Em que coordenadas (x y) quer meter a peça?");
        x=keyboard.nextInt();
        y=keyboard.nextInt();
        while(x<0||x>5||y<0||y>5||um.pieceExist(x,y)==true){
          printGame(um);
          System.out.println("as coordenadas("+x+","+y+") não existem ou podem conter um peça");
          System.out.println("insira coordenadas validas");
          x=keyboard.nextInt();
          y=keyboard.nextInt();
        }
        um.putPiece(um.currentPlayer,x,y);
        um.atualizar(x,y);
        um.setCurrentPlayer(um.currentPlayer);
      }
      else{
        printGame(um);
        System.out.println("\nJoga o jogador "+um.currentPlayer);
        dois = new MinMaxTree(um);
        dois.state.setCurrentPlayer(1);
        dois.setHeuristic();
        dois.expande(dificuldade);
        List<Game> GameList = new ArrayList<Game>(); 
        for(int i=0;i<dois.nodeList.size();i++){
          if(dois.heuristica==dois.nodeList.get(i).heuristica){
            GameList.add(dois.nodeList.get(i).state);
          }
        }
        um=GameList.get(ran.nextInt(GameList.size()));
        printGame(um);
        keyboard.nextLine();
      }

    }
    printGame(um);
    switch (um.verifyWinner()) {
      case 1:
        System.out.println("O jogador 1 ganhou");
        break;
      case 2:
        System.out.println("O jogador 2 ganhou");
        break;
      case 3:
        System.out.println("O jogo empatou");
        break;
      default:
        break;
    }
    System.out.println("press Enter");
    keyboard.nextLine();
  }

  public static void PlayerVsPlayer(Scanner keyboard){
    Game um = new Game();
    int x,y;
    Random ran = new Random();
    um.setCurrentPlayer(ran.nextInt(2)+1);
    while(um.verifyWinner()==0){
      printGame(um);
      System.out.println("\nJoga o jogador "+um.currentPlayer);
      System.out.println("Em que coordenadas (x y) quer meter a peça?");
      x=keyboard.nextInt();
      y=keyboard.nextInt();
      while(x<0||x>5||y<0||y>5||um.pieceExist(x,y)==true){
        printGame(um);
        System.out.println("as coordenadas("+x+","+y+") não existem ou podem conter um peça");
        System.out.println("insira coordenadas validas");
        x=keyboard.nextInt();
        y=keyboard.nextInt();
      }
      um.putPiece(um.currentPlayer,x,y);
      um.atualizar(x,y);
      um.setCurrentPlayer(um.currentPlayer);
    }
    printGame(um); 
    switch (um.verifyWinner()) {
      case 1:
        System.out.println("O jogador 1 ganhou");
        break;
      case 2:
        System.out.println("O jogador 2 ganhou");
        break;
      case 3:
        System.out.println("O jogo empatou");
        break;
      default:
        break;
    }
    System.out.println("press Enter");
    keyboard.nextLine();
  }

  public static void printGame(Game um){
    System.out.print("\033[H\033[2J");
      System.out.println("   GEKITAI\n");
      System.out.print(um); 
      System.out.println("numero de peças:"); 
      System.out.println("jogador 1: " +um.getPlayer1()+"  jogador 2: "+ um.getPlayer2()); 
  }
}