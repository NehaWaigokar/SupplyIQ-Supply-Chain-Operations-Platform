alert("app.js loaded");

document.addEventListener("DOMContentLoaded", function () {

    // Animated counters
    function animateValue(id, start, end, duration) {
        let range = end - start;
        let current = start;
        let increment = end > start ? 1 : -1;
        let stepTime = Math.abs(Math.floor(duration / range));

        let timer = setInterval(function () {
            current += increment;
            document.getElementById(id).innerText = current;

            if (current == end) {
                clearInterval(timer);
            }
        }, stepTime);
    }

    animateValue("totalProducts", 0, 240, 1200);
    animateValue("lowStock", 0, 15, 1000);

    // Search functionality
    const searchInput = document.getElementById("searchInput");
    const tableRows = document.querySelectorAll("#productTable tbody tr");

    searchInput.addEventListener("keyup", function () {
        const value = this.value.toLowerCase();

        tableRows.forEach(row => {
            const text = row.textContent.toLowerCase();
            row.style.display = text.includes(value) ? "" : "none";
        });
    });

});

    // Chart.js
    const ctx = document.getElementById("stockChart");

    if (ctx) {
        new Chart(ctx, {
            type: "doughnut",
            data: {
                labels: [
                    "Electronics",
                    "Accessories",
                    "Office",
                    "Others"
                ],
                datasets: [{
                    data: [45, 180, 25, 10],
                    backgroundColor: [
                        "#7c3aed",
                        "#2563eb",
                        "#06b6d4",
                        "#f43f5e"
                    ],
                    borderWidth: 0
                }]
            },
            options: {
    responsive: true,
    maintainAspectRatio: false,
    cutout: "65%",
    layout: {
        padding: 20
    },
    plugins: {
        legend: {
            position: "bottom",
            labels: {
                color: "#ffffff",
                font: {
                    size: 16,
                    weight: "600"
                },
                boxWidth: 14,
                padding: 22,
                usePointStyle: true,
                pointStyle: "circle"
            }
        }
    }
}