/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.mycompany.sudoku.classes;

import java.security.SecureRandom;

/**
 *
 * @author Michau
 */
public class SudoKuStructure {
    private final int[][] board = new int[][] {
                {1,2,3,  4,5,6,  7,8,9},
                {4,5,6,  7,8,9,  1,2,3},
                {7,8,9,  1,2,3,  4,5,6},

                {2,3,1,  5,6,4,  8,9,7},
                {5,6,4,  8,9,7,  2,3,1},
                {8,9,7,  2,3,1,  5,6,4},

                {3,1,2,  6,4,5,  9,7,8},
                {6,4,5,  9,7,8,  3,1,2},
                {9,7,8,  3,1,2,  6,4,5}
        };
    private final SecureRandom random = new SecureRandom();
    
    
    public SudoKuStructure(){
        
    }
    
    private void shuffleNumbers() {
        for (int i = 1; i <= 9; i++) {
            int ranNum = random.nextInt(9) + 1;
            swapNumbers(i, ranNum);
        }
    }

    private void swapNumbers(int n1, int n2) {
        for (int y = 0; y<9; y++) {
            for (int x = 0; x<9; x++) {
                if (board[x][y] == n1) {
                    board[x][y] = n2;
                } else if (board[x][y] == n2) {
                    board[x][y] = n1;
                }
            }
        }
    }
    
    private void shuffleRows() {
        int blockNumber;

        for (int i = 0; i < 9; i++) {
            int ranNum = random.nextInt(3);
            blockNumber = i / 3;
            swapRows(i, blockNumber * 3 + ranNum);
        }
    }

    private void swapRows(int r1, int r2) {
            int[] row = board[r1];
            board[r1] = board[r2];
            board[r2] = row;
    }
    
    private void shuffleCols() {
        int blockNumber;

        for (int i = 0; i < 9; i++) {
            int ranNum = random.nextInt(3);
            blockNumber = i / 3;
            swapCols(i, blockNumber * 3 + ranNum);
        }
    }
    
    private void swapCols(int c1, int c2) {
        int colVal;
        for (int i = 0; i < 9; i++){
            colVal = board[i][c1];
            board[i][c1] = board[i][c2];
            board[i][c2] = colVal;
        }
    }
    
    private void shuffle3X3Rows() {

        for (int i = 0; i < 3; i++) {
            int ranNum = random.nextInt(3);
            swap3X3Rows(i, ranNum);
        }
    }

    private void swap3X3Rows(int r1, int r2) {
        for (int i = 0; i < 3; i++) {
            swapRows(r1 * 3 + i, r2 * 3 + i);
        }
    }
    
    private void shuffle3X3Cols() {

        for (int i = 0; i < 3; i++) {
            int ranNum = random.nextInt(3);
            swap3X3Cols(i, ranNum);
        }
    }
    
    private void swap3X3Cols(int c1, int c2) {
        for (int i = 0; i < 3; i++) {
            swapCols(c1 * 3 + i, c2 * 3 + i);
        }
    }
    
     public void remove_numbers(int count){
        int val;
        
        for(int i =0;i<count;i++){
            val = random.nextInt(81);
            while(board[val/9][val%9]==0){
                val = random.nextInt(81);
            }
            board[val/9][val%9]= 0;
        }
    }
    
    
    public void makeBoard(){
        //this.board = Arrays.copyOf(board_re,81);
        this.shuffleNumbers();
        this.shuffleCols();
        this.shuffleRows();
        this.shuffle3X3Cols();
        this.shuffle3X3Rows();
    }
    
    @Override
    public String toString() {
        String table_description = "";
        for(int i =0;i<9;i++){
            for(int j=0;j<9;j++){
                table_description+=board[i][j];
            }
                table_description+='\n';
        }
//        int  counter ;
//        for(int i=0;i<9;i++){
//            for(int j=0;j<9;j++){
//                if(board[i][j]==0 && i<9){
//                    counter = 0;
//                    
//                    while(i<9 && j<9 && board[i][j] == 0){
//                        counter++;
//                        if(j<9)j++;
//                        else{
//                            i++;
//                            j=0;
//                        }
//                    }
//                    
//                    if(j>0)j--;
//                    else if (i>0){
//                        j=8;
//                        i--;
//                    }
//                    table_description+="0"+counter;
//                }
//                else{
//                    table_description+=board[i][j];
//                }
//            }
//        }
        return table_description;
    }
}
