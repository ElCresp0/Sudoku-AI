/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.mycompany.sudoku;

import com.mycompany.sudoku.classes.SudoKuStructure;
import java.io.FileWriter;
import java.io.IOException;
import java.io.Writer;

/**
 *
 * @author Michau
 */
public class mainApp {
    public static void main(String[] args){

        SudoKuStructure sudoku = new SudoKuStructure();

        sudoku.makeBoard();
        sudoku.remove_numbers(60);

        System.out.println(sudoku);
        
        try {
            Writer writer = new FileWriter("output.txt");
            for(int i=0;i<300;i++){
                sudoku = new SudoKuStructure();
                sudoku.makeBoard();
                sudoku.remove_numbers(60);
                writer.write(sudoku.toString()+'\n');
            }
            writer.close();
        } catch (IOException e) {   
        }
    }
}
