const apiURL = "http://127.0.0.1:5000";

function fetchGrupos() {
    fetch(`${apiURL}/grupo`)
        .then(response => response.json())
        .then(data => {
            let resultDiv = document.getElementById("grupoResult");
            let html = "<ul><h3>Grupos:</h3>"
            data.forEach(grupo =>{
                html += `<li>ID:${grupo.grupo_id}, Nome: ${grupo.grupo_name}</li>`;
            });
            html += "</ul>"
            resultDiv.innerHTML = html;
        })
        .catch(error => console.error("Erro ao listar grupos:", error));
}

function addGrupo(event){
    event.preventDefault();
    const grupoId = document.getElementById("grupo_id").value;
    const grupoName = document.getElementById("grupo_name").value;
    
    fetch(`${apiURL}/grupo`, {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({grupo_id: parseInt(grupoId), grupo_name: grupoName}),
    })
        .then(response => {
            if (response.ok) {
                alert("Grupo adicionado com sucesso!");
                fetchGrupos();
            } else {
                alert("Erro ao adicionar grupo.");
            }
        })
        .catch(error => console.error("Error ao adicionar grupo", error))
}


function fetchParticipantes() {
    const grupoId = document.getElementById("grupo_id_part").value;

    fetch(`${apiURL}/participante/${grupoId}`)
        .then(response => response.json())
        .then(data => {
            let resultDiv = document.getElementById("participanteResult");
            let html = `<ul><h3>Participantes do grupo ${grupoId}:</h3>`
            data.forEach(participante => {
                html += `<li>ID: ${participante.part_id}, Nome: ${participante.part_name}<br></li>`;
            });
            html += "</ul>"
            resultDiv.innerHTML = html;
        })
        .catch(error => console.error("Erro ao listar participantes:", error));
}

function addParticipante(event){
    event.preventDefault();
    const partId = document.getElementById("part_id").value;
    const partName = document.getElementById("part_name").value;
    const grupoId = document.getElementById("grupo_id_part_form").value;

    fetch(`${apiURL}/participante/${grupoId}`, {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({part_id: parseInt(partId), part_name: partName, grupo_id: parseInt(grupoId)}),
    })
        .then(response => {
            if (response.ok) {
                alert("Participante adicionado com sucesso!");
                fetchParticipantes();
            } else {
                alert("Erro ao adicionar participante.")
            }
        })
        .catch(error => console.error("Erro ao adicionar participante", error))
}

function sorteioAmigoSecreto() {
    const grupoId = document.getElementById("grupo_id_sorteio").value;

    fetch(`${apiURL}/sorteio/${grupoId}`)
    .then(response => response.json())
    .then( data => {
        let resultDiv = document.getElementById("sorteioResult");
        let html = `<ul><h3>Sorteio do Grupo ${grupoId}:</h3>`
        data["Amigo secreto"].forEach(par => {
            html += `<li>${par.parceiro_1.part_name} -> ${par.parceiro_2.part_name}</li>`
        });
        html += "</ul>"
        resultDiv.innerHTML = html
    })
    .catch(error => console.error("Error ao realizar sorteio:", error))
}