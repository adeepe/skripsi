document.addEventListener('DOMContentLoaded', (event) => {
    const ctx = document.getElementById('salesChart').getContext('2d');

    // Dummy data for initial chart
    const initialData = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0];
    
    // Function to generate month labels starting from June 2024
    function generateMonthLabels(startMonth, startYear, length) {
        const months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"];
        let labels = [];
        let currentMonth = startMonth;
        let currentYear = startYear;

        for (let i = 0; i < length; i++) {
            labels.push(`${months[currentMonth]} ${currentYear}`);
            currentMonth++;
            if (currentMonth > 11) {
                currentMonth = 0;
                currentYear++;
            }
        }
        return labels;
    }

    // Initialize the chart
    const monthLabels = generateMonthLabels(5, 2024, initialData.length); // 5 is June (0-based index)
    const salesChart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: monthLabels,
            datasets: [{
                label: 'Penjualan Energi (GWh)',
                data: initialData,
                backgroundColor: 'rgba(0, 0, 0, 0.1)',
                borderColor: 'rgba(0, 0, 0, 1)',
                borderWidth: 2
            }]
        },
        options: {
            scales: {
                x: {
                    title: {
                        display: true,
                        text: 'Tanggal',
                        font: {
                            family: 'Times New Roman',
                            size: 16
                        }
                    },
                    ticks: {
                        font: {
                            family: 'Times New Roman',
                            size: 12
                        }
                    }
                },
                y: {
                    title: {
                        display: true,
                        text: 'Penjualan Energi (GWh)',
                        font: {
                            family: 'Times New Roman',
                            size: 16
                        }
                    },
                    ticks: {
                        font: {
                            family: 'Times New Roman',
                            size: 12
                        },
                        beginAtZero: true
                    }
                }
            },
            plugins: {
                legend: {
                    position: 'bottom',
                    align: 'end',
                    labels: {
                        font: {
                            family: 'Times New Roman',
                            size: 14
                        }
                    }
                }
            }
        }
    });

    // Function to update chart data and labels
    function updateChart(predictions, startMonth, startYear) {
        const newLabels = generateMonthLabels(startMonth, startYear, predictions.length);
        salesChart.data.labels = newLabels;
        salesChart.data.datasets[0].data = predictions;
        salesChart.update();
    }

    // Event listener for month picker
    const monthPicker = document.getElementById('monthPicker');
    monthPicker.addEventListener('change', (event) => {
        const [year, month] = event.target.value.split('-').map(Number);
        const startMonth = 5; // June (0-based index)
        const startYear = 2024;
        
        // Calculate months ahead from June 2024
        const monthsAhead = (year - startYear) * 12 + (month - 1 - startMonth);

        // Send POST request to the server
        fetch('http://localhost:5000/predict', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ months_ahead: monthsAhead })
        })
        .then(response => response.json())
        .then(data => {
            if (data.predictions) {
                updateChart(data.predictions, startMonth, startYear);
            } else {
                console.error('Invalid response from server:', data);
            }
        })
        .catch(error => {
            console.error('Error fetching prediction:', error);
        });
    });

    // Set default value to June 2024
    monthPicker.value = '2024-06';
});
