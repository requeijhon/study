package Modelo;
import java.util.ArrayList;
import java.util.Date;
import java.util.List;

public class Pessoa {   
    private String nome;
    private String endereco;
    private String telefone;
    private Date dataNascimento;   
    //Relacionamento com a classe Carro    
    protected List<Carro> carros = new ArrayList<>();
        
    public String getNome(){
        return nome;
    }  
    public void setNome(String nome){
        this.nome = nome;
    }   
    public String getEndereco(){
        return endereco;
    }   
    public void setEndereco(String endereco){
        this.endereco = endereco;
    }   
    public String getTelefone(){
        return telefone;
    }   
    public void setTelefone(String telefone){
        this.telefone = telefone;
    }   
    public Date getDataNascimento(){
        return dataNascimento;
    }   
    public void setDataNascimento(Date dataNascimento) {
        this.dataNascimento = dataNascimento;
    }   
    public List<Carro> getCarros() {
        return carros;
    }  
    public void setCarros(List<Carro> carros) {
        this.carros = carros;
    }
}
