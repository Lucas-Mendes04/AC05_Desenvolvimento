function validar(){
    let idade = parseInt(document.getElementById("idadeNum").value);
    let alt = parseFloat(document.getElementById("altNum").value);
    let peso = parseFloat(document.getElementById("pesoNum").value);
    if(isNaN(idade)){
        alert("O campo idade não pode estar vazio!");
    }    
    else if(isNaN(alt)){
        alert("O campo altura não pode estar vazio!");
    }    
    else if(isNaN(peso)){
        alert("O campo peso não pode estar vazio!");
    }
}


