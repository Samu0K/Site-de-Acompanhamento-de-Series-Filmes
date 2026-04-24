const usuarios = ["samuel", "paulo", "ana"];
const arrobas = usuarios.map(nome => "@" + nome);
alert(arrobas)

let temperatura = [25, 32, 18, 40]
let filtro = temperatura.filter(x=> x > 30)
alert(filtro)


const precosSujos = [10, null, 30, 45, null];

let limpos = precosSujos.filter(x => x !== null)
alert(limpos)