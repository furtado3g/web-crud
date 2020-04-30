async function abreProduto(id){
    const url = '/atualizar/';
    const params = id;
    const options = {
        method : "get"
    }

    await fetch(url+params,options)
    .then(response=>{
        return response.text()
    })
    .then(data=>{
        $("#modal-container").html(data)
        $("#EditarProduto").modal("show");
    })
    .catch(e=>{
        console.log(e)
    })
}

async function excluirProduto(id){
    const url = '/atualizar/';
    const params = id;
    const options = {
        method : "delete"
    }

    await fetch(url+params,options)
    .then(response=>{
        return response.text()
    })
    .then(data=>{
        //location.reload()
    })
    .catch(e=>{
        console.log(e)
    })
}