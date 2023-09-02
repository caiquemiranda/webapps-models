// static/scripts.js
document.addEventListener("DOMContentLoaded", () => {
    fetch('/data')
        .then(response => response.json())
        .then(data => {
            const ctx = document.getElementById('stockChart').getContext('2d');

            new Chart(ctx, {
                type: 'line',
                data: {
                    labels: data.labels,
                    datasets: [{
                        label: 'Preço de Fechamento (R$)',
                        data: data.values,
                        borderColor: 'rgb(75, 192, 192)',
                        borderWidth: 2,
                    }]
                },
                options: {
                    scales: {
                        x: {
                            type: 'time',
                            time: {
                                unit: 'month'
                            }
                        },
                        y: {
                            beginAtZero: false
                        }
                    }
                }
            });
        })
        .catch(error => console.error('Erro ao buscar dados:', error));
});
