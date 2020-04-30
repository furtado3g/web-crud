async function abreProduto(id){
    const url = '/atualizar/';
    const param = id;
    const options = {
        method : "get"
    }

    await fetch(url+params,options)
    .then(response=>{
        return response.text()
    })
    .then(data=>{
        document.querySelector("#modal-container").removeChild()
        document.querySelector("#modal-container").innerHTML = data
    })
    .catch(e=>{
        console.log(e)
    })
}

async function excluirProduto(id){
    const url = '/atualizar/';
    const param = id;
    const options = {
        method : "delete"
    }

    await fetch(url+params,options)
    .then(response=>{
        return response.text()
    })
    .then(data=>{
        location.reload()
    })
    .catch(e=>{
        console.log(e)
    })
}