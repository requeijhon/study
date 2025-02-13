package Modelo;

public class Conta {
    protected String agencia;
    protected String numero;
    protected float saldo;   
    public void saque(float valor) {
        if (saldo < valor) {
            System.out.println("O saldo é insuficiente!");
        }else {
            saldo -= valor;
        System.out.println("Saque efetuado com sucesso!");      
        }
    } 
    public String getAgencia(){
        return agencia;
    }    
    public void setAgencia(String agencia) {
        this.agencia = agencia;
    }   
    public String getNumero() {
        return numero;
    }    
    public void setNumero(String numero) {
        this.numero = numero;
    }   
    public void deposito(float valor) {
        saldo += valor;
    }       
    public void saldo () {
        System.out.println("O saldo é " + saldo);
    }   
}
