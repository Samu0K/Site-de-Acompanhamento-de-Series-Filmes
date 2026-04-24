
const botao_abrir = document.querySelector('#abrir')
const botao_fechar = document.querySelector('#fechar')
const menu_lateral = document.querySelector('#menu_lateral')
const botao_overlay = document.querySelector('#overlay')
const a = document.querySelector('#a')
const b = document.querySelector('#b') 

botao_abrir.addEventListener('click', () => {
    menu_lateral.classList.add('ativo');
    botao_overlay.classList.add('ativo');
    a.classList.add('ativo')
    b.classList.add('ativo')
});

const fechar = () => {
    b.classList.remove('ativo')
    a.classList.remove('ativo')
    menu_lateral.classList.remove ('ativo')
    botao_overlay.classList.remove ('ativo')
};

botao_fechar.addEventListener('click', fechar)
botao_overlay.addEventListener('click', fechar)