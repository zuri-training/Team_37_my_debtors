var xValues = ["Italy", "France", "Spain", "USA", "Argentina"];
var yValues = [75, 25];
var barColors = [
    "#b91d47",
    "#00aba9",
];

new Chart("myChart", {
    type: "doughnut",
    data: {
        datasets: [{
            backgroundColor: barColors,
            data: yValues
        }]
    },
    options: {
        title: {
            display: false,
            text: "World Wide Wine Production 2018"
        }
    }
});