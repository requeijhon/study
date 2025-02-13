package Modelo;
import java.util.Date;
public class Empresa {
    
    private String nome;
    private String cnpj;
    private String endereco;
    private Date dataFundacao;
    private float faturamento;
    
    public void imprimir() {
        System.out.println("Nome: " + nome);
        System.out.println("CNPJ: " + cnpj);
        System.out.println("Endereço: " + endereco);
        System.out.println("Data de fundação: " + dataFundacao);
    }
    
    public String getNome(){
        return nome;
    }
    public void setNome(String nome) {
        this.nome = nome;
    }
    public String getCnpj(){
        return cnpj;
    }
    public void setCnpj(String cnpj){
        this.cnpj = cnpj;
    }
    public String getEndereco(){
        return endereco;
    }
    public void setEndereco(String endereco){
        this.endereco = endereco;
    }
    public Date getDataFundacao(){
        return dataFundacao;
    }
    public void setDataFundacao(Date dataFundacao){
        this.dataFundacao = dataFundacao;
    }
    public float getFaturamento() {
        return faturamento;
    }
    public void setFaturamento(float faturamento){
        this.faturamento = faturamento;
    }
}
