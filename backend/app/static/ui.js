let loginGerado = ''  // variavel para guardar o login (usado apenas na função de toggle o login)
let loginVisivel = false  // controla se está mostrando ou escondendo


function irParaCadastro(){
    document.getElementById('tela_boasvindas').style.display = 'none'
    document.getElementById('tela_cadastro').style.display = 'block'

}

function mostrarLogin(login){

    if (loginVisivel == false){
        document.getElementById('login_texto').innerHTML = loginGerado
    } else {
        document.getElementById('login_texto').innerHTML = '*******'

    }loginVisivel = !loginVisivel //inverter o estado do botão, se nao nuca troca por isso dava problema dããã

}