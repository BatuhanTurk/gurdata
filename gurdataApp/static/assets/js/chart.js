$(function() {

    /*LIne-Chart */
    var ctx = document.getElementById("chartLine");
    if (ctx){
    ctx = ctx.getContext('2d');
    var myChart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: ["Sun", "Mon", "Tus", "Wed", "Thu", "Fri", "Sat"],
            datasets: [{
                label: 'Profits',
                data: [100, 420, 210, 420, 210, 320, 350],
                borderWidth: 2,
                backgroundColor: 'transparent',
                borderColor: '#6c5ffc',
                borderWidth: 3,
                pointBackgroundColor: '#ffffff',
                pointRadius: 2
            }, {
                label: 'Expenses',
                data: [450, 200, 350, 250, 480, 200, 400],
                borderWidth: 2,
                backgroundColor: 'transparent',
                borderColor: '#05c3fb',
                borderWidth: 3,
                pointBackgroundColor: '#ffffff',
                pointRadius: 2
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,

            scales: {
                xAxes: [{
                    ticks: {
                        fontColor: "#9ba6b5",
                    },
                    display: true,
                    gridLines: {
                        color: 'rgba(119, 119, 142, 0.2)'
                    }
                }],
                yAxes: [{
                    ticks: {
                        fontColor: "#9ba6b5",
                    },
                    display: true,
                    gridLines: {
                        color: 'rgba(119, 119, 142, 0.2)'
                    },
                    scaleLabel: {
                        display: false,
                        labelString: 'Thousands',
                        fontColor: 'rgba(119, 119, 142, 0.2)'
                    }
                }]
            },
            legend: {
                labels: {
                    fontColor: "#9ba6b5"
                },
            },
        }
    });
    }

    /* Bar-Chart1 */
    var ctx = document.getElementById("chartBar1");
    if (ctx){
        ctx = ctx.getContext('2d');
    var myChart = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep"],
            datasets: [{
                label: 'Sales',
                data: [200, 450, 290, 367, 256, 543, 345, 290, 367],
                borderWidth: 2,
                backgroundColor: '#6c5ffc',
                borderColor: '#6c5ffc',
                borderWidth: 2.0,
                pointBackgroundColor: '#ffffff',

            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            legend: {
                display: true
            },
            scales: {
                yAxes: [{
                    ticks: {
                        beginAtZero: true,
                        stepSize: 150,
                        fontColor: "#9ba6b5",
                    },
                    gridLines: {
                        color: 'rgba(119, 119, 142, 0.2)'
                    }
                }],
                xAxes: [{
                    barPercentage: 0.4,
                    barValueSpacing: 0,
                    barDatasetSpacing: 0,
                    barRadius: 0,
                    ticks: {
                        display: true,
                        fontColor: "#9ba6b5",
                    },
                    gridLines: {
                        display: false,
                        color: 'rgba(119, 119, 142, 0.2)'
                    }
                }]
            },
            legend: {
                labels: {
                    fontColor: "#9ba6b5"
                },
            },
        }
    });
    }

    /* Bar-Chart2*/
    var ctx = document.getElementById("chartBar2");
    if (ctx){
    var myChart = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul"],
            datasets: [{
                label: "Data1",
                data: [65, 59, 80, 81, 56, 55, 40],
                borderColor: "#6c5ffc",
                borderWidth: "0",
                backgroundColor: "#6c5ffc"
            }, {
                label: "Data2",
                data: [28, 48, 40, 19, 86, 27, 90],
                borderColor: "#05c3fb",
                borderWidth: "0",
                backgroundColor: "#05c3fb"
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            scales: {
                xAxes: [{
                    barPercentage: 0.4,
                    barValueSpacing: 0,
                    barDatasetSpacing: 0,
                    barRadius: 0,
                    ticks: {
                        fontColor: "#9ba6b5",
                    },
                    gridLines: {
                        color: 'rgba(119, 119, 142, 0.2)'
                    }
                }],
                yAxes: [{
                    ticks: {
                        beginAtZero: true,
                        fontColor: "#9ba6b5",
                    },
                    gridLines: {
                        color: 'rgba(119, 119, 142, 0.2)'
                    },
                }]
            },
            legend: {
                labels: {
                    fontColor: "#9ba6b5"
                },
            },
        }
    });
    }

    /* Area Chart*/
    var ctx = document.getElementById("chartArea");
    if (ctx){
    var myChart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: ["Jan", "Feb", "Mar", "Apr"],
            datasets: [{
                label: "Data1",
                borderColor: "#FA5087",
                borderWidth: "3",
                backgroundColor: "rgba(250, 80, 135, .64)",
                data: [67,22, 44, 43]
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            tooltips: {
                mode: 'index',
                intersect: false
            },
            hover: {
                mode: 'nearest',
                intersect: true
            },
            scales: {
                xAxes: [{
                    display: false,

                }],
                yAxes: [{
                    display: false,

                }]
                // xAxes: [{
                //     ticks: {
                //         fontColor: "#9ba6b5",
                //     },
                //     gridLines: {
                //         color: 'rgba(119, 119, 142, 0.2)'
                //     }
                // }],
                // yAxes: [{
                //     ticks: {
                //         beginAtZero: true,
                //         fontColor: "#9ba6b5",
                //     },
                //     gridLines: {
                //         color: 'rgba(119, 119, 142, 0.2)'
                //     },
                // }]
            },
            legend: {
                display:false,
            },
        }
    });
    }

    /* Pie Chart*/
    var datapie = {
        labels: ['Jan', 'Feb', 'Mar', 'Apr', 'May'],
        datasets: [{
            data: [20, 20, 30, 5, 25],
            backgroundColor: ['#6c5ffc', '#05c3fb', '#09ad95', '#1170e4', '#e82646']
        }]
    };
    var optionpie = {
        maintainAspectRatio: false,
        responsive: true,
        legend: {
            display: false,
        },
        animation: {
            animateScale: true,
            animateRotate: true
        }
    };

    /* Doughbut Chart*/
    var ctx6 = document.getElementById('chartPie');
    if (ctx6) {
        var myPieChart6 = new Chart(ctx6, {
            type: 'doughnut',
            data: datapie,
            options: optionpie
        });
    }

    /* Pie Chart*/
    var ctx7 = document.getElementById('chartDonut');
    if (ctx7) {
        var myPieChart7 = new Chart(ctx7, {
            type: 'pie',
            data: datapie,
            options: optionpie
        });
    }

    /* Radar chart*/
    var ctx = document.getElementById("chartRadar");
    if (ctx) {
        var myChart = new Chart(ctx, {
            type: 'radar',
            data: {
                labels: [

                    ["Eating", "Dinner"],
                    ["Drinking", "Water"], "Sleeping", ["Designing", "Graphics"], "Coding", "Cycling", "Running",

                ],
                datasets: [{

                    label: "Data1",
                    data: [65, 59, 66, 45, 56, 55, 40],
                    borderColor: "rgba(108, 95, 252, .8)",
                    borderWidth: "1",
                    backgroundColor: "rgba(108, 95, 252, .4)"
                }, {
                    label: "Data2",
                    data: [28, 12, 40, 19, 63, 27, 87],
                    borderColor: "rgba(5, 195, 251,0.8)",
                    borderWidth: "1",
                    backgroundColor: "rgba(5, 195, 251,0.4)"
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                legend: {
                    display: false
                },
                scale: {
                    angleLines: {color: '#9ba6b5'},
                    gridLines: {
                        color: 'rgba(119, 119, 142, 0.2)'
                    },
                    ticks: {
                        beginAtZero: true,
                    },
                    pointLabels: {
                        fontColor: '#9ba6b5',
                    },
                },

            }
        });
    }
    /* polar chart */
    var ctx = document.getElementById("chartPolar");
    if (ctx) {
        var myChart = new Chart(ctx, {
            type: 'polarArea',
            data: {
                datasets: [{
                    data: [18, 15, 9, 6, 19],
                    backgroundColor: ['#6c5ffc', '#05c3fb', '#09ad95', '#1170e4', '#e82646'],
                    hoverBackgroundColor: ['#6c5ffc', '#05c3fb', '#09ad95', '#1170e4', '#e82646'],
                    borderColor: 'transparent',
                }],
                labels: ["Data1", "Data2", "Data3", "Data4"]
            },
            options: {
                scale: {
                    gridLines: {
                        color: 'rgba(119, 119, 142, 0.2)'
                    }
                },
                responsive: true,
                maintainAspectRatio: false,
                legend: {
                    labels: {
                        fontColor: "#9ba6b5"
                    },
                },
            }
        });
    }
});