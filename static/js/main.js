let socket;
let chart;
let chartData = { labels: [], datasets: [{ label: 'Loudness (dB)', data: [], backgroundColor: '#4f8cff' }] };

function initChart() {
    const ctx = document.getElementById('loudnessChart').getContext('2d');
    chart = new Chart(ctx, {
        type: 'bar',
        data: chartData,
        options: {
            responsive: true,
            animation: false,
            scales: {
                x: { title: { display: true, text: 'Time (s)' } },
                y: { title: { display: true, text: 'Loudness (dB)' }, min: 0, max: 90 }
            }
        }
    });
}

function updateChart(time, dB) {
    chartData.labels.push(time);
    chartData.datasets[0].data.push(dB);
    chart.update();
}

document.addEventListener('DOMContentLoaded', () => {
    initChart();
    socket = io();
    socket.on('loudness_data', (data) => {
        updateChart(data.time, data.dB);
    });
    socket.on('loudness_all', (allData) => {
        window.loudnessData = allData; // Store for sync
    });

    document.getElementById('uploadForm').onsubmit = function(e) {
        e.preventDefault();
        const formData = new FormData(this);
        fetch('/upload', { method: 'POST', body: formData })
            .then(res => res.json())
            .then(data => {
                if (data.success) {
                    document.getElementById('audioPlayer').src = data.url;
                    chartData.labels = [];
                    chartData.datasets[0].data = [];
                    chart.update();
                    // Start real-time analysis
                    socket.emit('start_analysis', { url: data.url });
                }
            });
    };

    const audio = document.getElementById('audioPlayer');
    audio.ontimeupdate = function() {
        if (window.loudnessData) {
            const sec = Math.floor(audio.currentTime);
            if (window.loudnessData[sec]) {
                // Only update if new second
                if (chartData.labels.length <= sec) {
                    chartData.labels.push(window.loudnessData[sec].time);
                    chartData.datasets[0].data.push(window.loudnessData[sec].dB);
                    chart.update();
                }
            }
        }
    };

    const fileInput = document.getElementById('mp3file');
    const fileNameSpan = document.getElementById('selectedFileName');
    document.querySelector('.custom-file-label').onclick = () => fileInput.click();
    fileInput.onchange = () => {
        fileNameSpan.textContent = fileInput.files[0] ? fileInput.files[0].name : 'No file chosen';
    };
});
