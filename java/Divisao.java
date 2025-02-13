package Modelo;

public class Divisao {
    private int num1;
    private int num2;
    
    public void divisao() {
        System.out.println("A divisão é: " + (num1 / num2));
    }
    
    public int getNum1() {
        return num1;
    }
    
    public void setNum1(int num1) {
        this.num1 =  num1;
    }
    
    public int getNum2() {
        return num2;
    }
    
    public void setNum2(int num2) {
        if (num2 == 0) {
            num2 = 1;
        } else {
            this.num2 = num2;
        }
    }
}
