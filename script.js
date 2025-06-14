
const ctx = document.getElementById('grafico').getContext('2d');

const chart = new Chart(ctx, {
  type: 'bar',
  data: {
    labels: ['Player', 'Banker', 'Empate'],
    datasets: [{
      label: 'Probabilidade (%)',
      data: [0, 0, 0],
      backgroundColor: ['#4ade80', '#60a5fa', '#facc15']
    }]
  },
  options: {
    animation: false,
    scales: {
      y: {
        beginAtZero: true,
        max: 100
      }
    }
  }
});

function gerarProbabilidades() {
  const player = Math.floor(Math.random() * 100);
  const banker = Math.floor(Math.random() * (100 - player));
  const empate = 100 - player - banker;

  return { Player: player, Banker: banker, Empate: empate };
}

function atualizarGrafico() {
  const data = gerarProbabilidades();

  chart.data.datasets[0].data = [
    data.Player,
    data.Banker,
    data.Empate
  ];
  chart.update();

  const maior = Object.keys(data).reduce((a, b) => data[a] > data[b] ? a : b);
  document.getElementById('sugestao').textContent = `Sugerido: ${maior}`;
}

window.onload = () => {
  atualizarGrafico();
  setInterval(atualizarGrafico, 10000);
};
