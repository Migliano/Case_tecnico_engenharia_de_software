function enviarCadastro(event) {
    
    event.preventDefault() // sem isso aqui o form manda um GET/POST e recarrega a página, aí a página some

    let nome = document.getElementById('nome').value
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