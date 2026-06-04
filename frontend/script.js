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
    .then(fedback => {
        if (!fedback.ok) { //negativa do ok pra apontar erro que chegou no backend! OPOSTO DE 400
            return fedback.json().then(data => { //abrir o erro que veio
            document.getElementById('resultado').innerText = 'Erro:' + data.erro //mostra o erro pelo ID
        })
    }
        return fedback.json() //se nao deu erro, segue pro porximo .then

    })
    .then(data => { //data é o nome padrão para mostarr na tela, vai ter que usar pro fedback do CEP tmb
        // getElementById aqui retorna o elemento único com aquele id
        document.getElementById('resultado').innerHTML = 'Seu login: ' + data.login //innetHTML mostra na tela o login
    })

    return false
    }else {
        return false
    }
}

function sanitizarCampos(){ //aqui é o cerebro das validações de campo. No geral, faz a consulta de tamanho minimo e maimo de caracteres de cada campo + verificações especificas se necessário

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
    } else if (validaCPF(cpf) === false){ //regras de validação matemática do cpf
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
    } else if (validarData_Nascimento(data_nascimento)){ //checa se data de nascimento é futura
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

//daqui pra baixo são so as funções que validam especificidades de campos especificos: email, cpf, data, cep

function validarData_Nascimento(data_nascimento){ //checa se data de nascimento é futura, se for, retorna false

    const data_Atual = new Date()
    const Nascimento = new Date(data_nascimento)

    if(Nascimento > data_Atual){
        alert("A data em 'Data de Nascimento' não pode ser futura, por favor, verifique!")
        return true

    } else{
        return false
    }
}


function validaCPF(cpf){ //depois procurar um jeito de isso ficar menos bagunçado

    //verificar se todos os numeros sao iguais
    const digitos_Separados = cpf.split('') // aqui é pra investicar os casos de todos os numeros iguais. Essa array serve para dividir os digitos

    if (digitos_Separados.every(digito => digito === digitos_Separados[0])){ // digito === digitos_separados[0] é o teste de fato. compara sempre com o primeiro
        alert("O campo 'cpf' está invalido, por favor, verifique!")
        return false
    }


    //verificar regras de construção do numero de cpf (de acordo com somatematica)
    let peso = 10 //peso de cada digito, a regra consiste em multiplicar os digitos do cpf individualmente por um numero de peso máximo 10. o segundo peso 9... e assim por diante. esta variavel servirá para armazenar o "peso" que estamos adicionando a cada volta de um laço
    let total = 0 //variavel para armazenar total da soma entre os caracteres * o peso de cada

    for (i = 0; i <= 8; i++){ //laço para somar todos os digitos + a multiplicação do peso de cada

        total += (parseInt(cpf[i])*peso)
        peso = peso - 1 //serve para decair o peso, dãã
    }

    let resto = (total * 10) % 11 //aqui iniciaremos o calculo de verificação do primeiro. esta é a regra final
    if (resto === 10){ //é por causa da regra de verificação de cpf. quando o resto da divisão é 10, deve-se considerar que o primeiro digito verificador é 0
        resto = 0
    }

    if (resto === parseInt(cpf[9])){ //aqui termina a verificação do primeiro digito e se inicia a verificação do *segundo*
        total = 0 //zerar a variável para refazer a somatoria
        peso = 11 //a regra é a mesma mas começa com 11 e leva com conta o primeiro digito. então renomeamos o peso inicial e fazemos a mesma coisa que fizemos pro primeiro
        
        for (i = 0; i <= 9; i++){ //mesma coisa de antes, mas agora vamos até o elemento 10
            total += (parseInt(cpf[i])*peso)
            peso = peso - 1 
        }
        resto = (total * 10) % 11
        if (resto === 10){ //é por causa da regra de verificação de cpf. quando o resto da divisão é 10, deve-se considerar que o primeiro digito verificador é 0
            resto = 0
    
        }
        if (resto === parseInt(cpf[10])){
            return true

        }else { // else do *segundo* digito
            alert("O campo 'cpf' está invalido, por favor, verifique!")
            return false
        }

    } else { // else do primeiro digito
            alert("O campo 'cpf' está invalido, por favor, verifique!")
            return false
    } 

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
