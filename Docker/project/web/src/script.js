// Buscando e referenciando o botão 'request-button'
const requestButton = document.getElementById('request-button');

// Adicionando um evento de click para ele
requestButton.addEventListener('click', function () {
    // Buscando e referenciando o valor do método selecionado
    const method = document.getElementById('methods').value;
    // Definindo a URL da API
    const apiUrl = 'http://localhost:8001/api/';
    // Definindo a função 'call' passando o método e a URL da API
    const call = async (method, apiUrl) => {
        // Utilizando o método fetch para fazer a requisição
        fetch(
            // A requisição é feita para a URL da API
            apiUrl,
            {
                // Passando o método da requisição
                method: method,
                // Passando o cabeçalho da requisição
                headers: {
                    // Definindo o tipo de conteúdo da requisição, neste caso, JSON
                    'Content-Type': 'application/json'
                }
            }
        )
            // Então
            .then(response => {
                // Se a requisição for bem sucedida
                if (response.ok) {
                    // Retornar a resposta em formato JSON
                    response.json().then(data => {
                        // Buscando e referenciando o elemento 'responses'
                        const responses = document.querySelector('.responses');
                        // Criando um novo elemento 'div'
                        const responseElement = document.createElement('div');
                        // Definindo o conteúdo do elemento 'div' com a resposta da requisição
                        responseElement.innerHTML = JSON.stringify(data.message);
                        // Adicionando o elemento 'div' ao elemento 'responses'
                        responses.appendChild(responseElement);
                    });
                };
            })
            // Capturando o erro
            .catch(error => console.log(error));
    };

    // Chamando a função 'call' passando o método e a URL da API
    call(method, apiUrl);
});