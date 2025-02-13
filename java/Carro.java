package Modelo;

public class Carro {
   private String modelo;
   private String placa;
   private int ano;
   private float valor;
   
   public String getModelo(){
       return modelo;
   }   
   public void setModelo(String modelo){
       this.modelo = modelo;
   }   
   public String getPlaca(){
       return placa;
   } 
   public void setPlaca(String placa){
       this.placa = placa;
   }  
   public int getAno(){
       return ano;
   }  
   public void setAno(int ano){
       this.ano = ano;
   }   
   public float getValor(){
       return valor;
   }  
   public void setValor(float valor){
       this.valor = valor;
   }
}
