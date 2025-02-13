package Modelo;

public class Aluno extends Pessoa {
    
    private String registroAcademico;
    private String curso;
    private float mensalidade;
    
    public String getRegistroAcademico() {
        return registroAcademico;
    }
    
    public void setRegistroAcademico(String registroAcademico){
        this.registroAcademico = registroAcademico;
    }
    
    public String getCurso() {
        return curso;
    }
    
    public void setCurso(String curso){
        this.curso = curso;
    }
    
    public float getMensalidade() {
        return mensalidade;
    }
    
    public void setmMnsalidade(float mensalidade){
        this.mensalidade = mensalidade;
    }
    
}
