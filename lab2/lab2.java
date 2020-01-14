package lab2;

import java.util.ArrayList; 

class Interval { 
 int buy, sell; 
} 

class lab2 { 

 public static void main(String args[]) 
 {  
     int price[] = {80, 100, 110, 90, 65,70, 75, 90, 80, 70, 100, 80, 65, 60, 55, 50}; 
     
     int n = price.length;
     if (n == 1) 
         return; 

     int count = 0; 

     ArrayList<Interval> sol = new ArrayList<Interval>(); 

     int i = 0; 
     while (i < n - 1) { 

         while ((i < n - 1) && (price[i + 1] <= price[i])) 
             i++; 
         
         if (i == n - 1) 
             break; 

         Interval e = new Interval(); 
         e.buy = i++; 

         while ((i < n) && (price[i] >= price[i - 1])) 
             i++; 

         e.sell = i - 1; 
         sol.add(e); 

         count++; 
     } 

     if (count == 0) 
         System.out.println("No Profit"); 
     else
         for (int j = 0; j < count; j++) 
             System.out.println("Buy on day: " + sol.get(j).buy + " Sell on day : " 
         + sol.get(j).sell + " Profit : " + (price[sol.get(j).sell] - price[sol.get(j).buy]) );

 } 
} 