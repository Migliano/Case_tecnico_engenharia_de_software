function enviarCadastro(event) {
    event.preventDefault()

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
    .then(fedback => fedback.json())
    .then(data => {
        console.log(data.mensagem)
    })

    return false
}