// Opciones comunes para los gráficos
const opcionesGrafico = {
    type: 'line',
    options: {
        responsive: true,
        scales: {
            x: { title: { display: true, text: 'Fecha' } },
            y: { title: { display: true, text: 'Valor' } }
        }
    }
};

// Datos de ejemplo
const fechas = ['2023-11-01', '2023-11-02', '2023-11-03', '2023-11-04'];

// Gráfico del Acelerómetro (x_cor, y_cor, z_cor)
const graficoAcelerometro = new Chart(
    document.getElementById('graficoAcelerometro').getContext('2d'),
    {
        ...opcionesGrafico,
        data: {
            labels: fechas,
            datasets: [
                {
                    label: 'X_Cor',
                    data: [0.2, 0.3, 0.5, 0.4],
                    borderColor: '#ff7043',
                    backgroundColor: 'rgba(255, 112, 67, 0.2)',
                    fill: true,
                },
                {
                    label: 'Y_Cor',
                    data: [0.6, 0.7, 0.8, 0.6],
                    borderColor: '#4CAF50',
                    backgroundColor: 'rgba(76, 175, 80, 0.2)',
                    fill: true,
                },
                {
                    label: 'Z_Cor',
                    data: [0.9, 0.8, 0.7, 0.5],
                    borderColor: '#42A5F5',
                    backgroundColor: 'rgba(66, 165, 245, 0.2)',
                    fill: true,
                }
            ]
        }
    }
);

// Gráfico del Sensor ADC (voltaje y valor_analogico)
const graficoADC = new Chart(
    document.getElementById('graficoADC').getContext('2d'),
    {
        ...opcionesGrafico,
        data: {
            labels: fechas,
            datasets: [
                {
                    label: 'Voltaje',
                    data: [3.3, 3.1, 3.5, 3.2],
                    borderColor: '#ff7043',
                    backgroundColor: 'rgba(255, 112, 67, 0.2)',
                    fill: true,
                },
                {
                    label: 'Valor Analógico',
                    data: [1023, 980, 1020, 1010],
                    borderColor: '#4CAF50',
                    backgroundColor: 'rgba(76, 175, 80, 0.2)',
                    fill: true,
                }
            ]
        }
    }
);

// Gráfico del Sensor BME (temp, presion, altitud)
const graficoBME = new Chart(
    document.getElementById('graficoBME').getContext('2d'),
    {
        ...opcionesGrafico,
        data: {
            labels: fechas,
            datasets: [
                {
                    label: 'Temperatura (°C)',
                    data: [22, 23, 21, 22.5],
                    borderColor: '#ff7043',
                    backgroundColor: 'rgba(255, 112, 67, 0.2)',
                    fill: true,
                },
                {
                    label: 'Presión (hPa)',
                    data: [1013, 1015, 1012, 1011],
                    borderColor: '#42A5F5',
                    backgroundColor: 'rgba(66, 165, 245, 0.2)',
                    fill: true,
                },
                {
                    label: 'Altitud (m)',
                    data: [50, 52, 49, 51],
                    borderColor: '#FFEB3B',
                    backgroundColor: 'rgba(255, 235, 59, 0.2)',
                    fill: true,
                }
            ]
        }
    }
);

// Gráfico del Sensor de Distancia (dist_cm)
const graficoDistancia = new Chart(
    document.getElementById('graficoDistancia').getContext('2d'),
    {
        ...opcionesGrafico,
        data: {
            labels: fechas,
            datasets: [
                {
                    label: 'Distancia (cm)',
                    data: [20, 22, 19, 21],
                    borderColor: '#ff7043',
                    backgroundColor: 'rgba(255, 112, 67, 0.2)',
                    fill: true,
                }
            ]
        }
    }
);