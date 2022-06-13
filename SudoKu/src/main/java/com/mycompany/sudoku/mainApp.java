/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.mycompany.sudoku;

import com.mycompany.sudoku.classes.SudoKuStructure;
import java.io.FileNotFoundException;
import java.io.FileWriter;
import java.io.IOException;
import java.io.PrintWriter;
import java.io.Writer;
import java.security.SecureRandom;
import java.util.ArrayList;
import java.util.List;

/**
 *
 * @author Michau
 */
public class mainApp {
    public static void main(String[] args){

        SudoKuStructure sudoku = new SudoKuStructure();
/* for one solution */
        try (PrintWriter writer = new PrintWriter("sudoku.csv")) {

            StringBuilder sb = new StringBuilder();
            sb.append("quizzes");
            sb.append(',');
            sb.append("solutions");
            sb.append('\n');

            for (String[] temp : dataLines) {
                sb.append(temp[0]);
                sb.append(',');
                sb.append(temp[1]);
                sb.append('\n');
            }

            writer.write(sb.toString());

            System.out.println("done!");

        } catch (FileNotFoundException e) {
            System.out.println(e.getMessage());
        }
        
/* for many solutions */
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
