function enviarCadastro(event) {
    
    event.preventDefault() // sem isso aqui o form manda um GET/POST e recarrega a página, aí a página some

    let nome = document.getElementById('nome').value //pegar dados, depois posso fazer uma função disso talvez
    let cpf = document.getElementById('cpf').value
    let email = document.getElementById('email').value
    let data_nascimento = document.getElementById('data_nascimento').value
    let cep = document.getElementById('cep').value
    let endereco = document.getElementById('endereco').value

    console.log(nome);
    console.log(cpf);
    console.log(email);
    console.log(data_nascimento);
    console.log(cep);
    console.log(endereco);

    if (sanitizarCampos()){ // condicional para verificar saude dos dados. Por enquanto verifica tamanho minimo e maximo
            fetch('http://127.0.0.1:5000/cadastro', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            nome: nome,
            cpf: cpf,
            email: email,
            data_nascimento: data_nascimento,
            cep: cep,
            endereco: endereco,
        })
    })
    // primeiro .then: o fetch devolve a resposta HTTP bruta (status, headers, body ainda fechado)
    // o .json() lê esse body e transforma em objeto
    .then(fedback => fedback.json())
    // segundo .then  recebe o objeto JS de verdade
    // chamei de data pq vi que no youtube que chamam assim, pelo visto podia ser outor nome
    .then(data => { //data é o nome padrão para mostarr na tela, vai ter que usar pro fedback do cep tmb
        // getElementById aqui retorna o elemento único com aquele id
        document.getElementById('resultado').innerHTML = 'Seu login: ' + data.login
    })

    return false
    }else {
        return false
    }


}

function sanitizarCampos(){

    let nome = document.getElementById('nome').value //pegar dados
    let cpf = document.getElementById('cpf').value
    let email = document.getElementById('email').value
    let data_nascimento = document.getElementById('data_nascimento').value
    let cep = document.getElementById('cep').value
    let endereco = document.getElementById('endereco').value

    if (nome === ''){ //depois vou fazer uma função pra isso, por enquanto ta bom
        alert("O campo 'nome' não pode estar vazio, por favor, verifique!")
        return false
    } else if (nome.length > 100){
        alert("O campo 'nome' não pode ter mais que 100 caracteres, por favor, verifique!")
        return false
    }

    const regexcpf = /^\d{11}$/; //regex padrão para conferencia de cpf de 11 numeros. talvez depois implementar máscara de input para inserir . e -
    if (cpf === ''){
        alert("O campo 'cpf' não pode estar vazio, por favor, verifique!")
        return false
    } else if (cpf.length > 11){
        alert("O campo 'cpf' não pode ter mais que 11 caracteres, por favor, verifique!")
        return false
    } else if (regexcpf.test(cpf) === false){
        alert("O campo 'cpf' não parece ser um cpf válido, por favor, verifique!")
        return false
    }


    const regexEmail = /^[^\s@]+@[^\s@]+\.[^\s@]+$/; //regex simples para conferencia do email
    if (email === ''){
        alert("O campo 'email' não pode estar vazio, por favor, verifique!")
        return false
    } else if (email.length > 100){
        alert("O campo 'email' não pode ter mais que 100 caracteres, por favor, verifique!")
        return false
    } else if (regexEmail.test(email) === false){
        alert("O campo 'email' não parece ser um endereço de e-mail válido, por favor, verifique!")
        return false
    }


    if (data_nascimento === ''){
        alert("O campo 'data_nascimento' não pode estar vazio, por favor, verifique!")
        return false
    } else if (data_nascimento.length > 100){
        alert("O campo 'data_nascimento' não pode ter mais que 100 caracteres, por favor, verifique!")
        return false
    }


    if (cep === ''){
        alert("O campo 'cep' não pode estar vazio, por favor, verifique!")
        return false
    } else if (cep.length > 20){
        alert("O campo 'cep' não pode ter mais que 20 caracteres, por favor, verifique!")
        return false
    }


    if (endereco === ''){
        alert("O campo 'endereco' não pode estar vazio, por favor, verifique!")
        return false
    } else if (endereco.length > 100){
        alert("O campo 'endereco' não pode ter mais que 100 caracteres, por favor, verifique!")
        return false
    }


    return true
}




function buscarLogradouro(cep) {

    let url = "https://viacep.com.br/ws/" + cep + "/json/" 

    fetch(url, {
    })
    // mesmo padrão de antes: primeiro converte a resposta HTTP crua em objeto JS
    .then(fedback => fedback.json())
    // depois pega o campo logradouro que a API do ViaCEP retorna dentro do JSON e bota no campo de endereço
    .then(data => {
        document.getElementById('endereco').value = data.logradouro
    })
}   