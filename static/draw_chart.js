// Draw a line graph in flask html script
function drawChart(chartType, chartLabel) {

    // Initialise chart figure
    Chart.defaults.global.animationSteps = 50;
    Chart.defaults.global.tooltipYPadding = 16;
    Chart.defaults.global.tooltipCornerRadius = 0;
    Chart.defaults.global.tooltipTitleFontStyle = "normal";
    Chart.defaults.global.tooltipFillColor = "rgba(0,0,0,0.8)";
    Chart.defaults.global.animationEasing = "easeOutBounce";
    Chart.defaults.global.responsive = false;
    Chart.defaults.global.scaleLineColor = "black";
    Chart.defaults.global.scaleFontSize = 16;

    // get bar chart canvas
    var mychart = document.getElementById(chartType).getContext("2d");
    steps = 10;
    max = 17000;

    // draw bar chart
    var lineChart = new Chart(mychart, {
        type: "line",
        data: barData,
        options: {
            title: {
                display: true,
                text: chartLabel + " line graph"
            },
            scales: {
                yAxes: [{
                    scaleLabel: {
                        display: true,
                        labelString: chartLabel
                    }
                }],
                xAxes: [{
                    scaleLabel: {
                        display: true,
                        labelString: 'Timestamp'
                    }
                }]
            }
        },
        scaleOverride: true,
        scaleSteps: steps,
        scaleStepWidth: Math.ceil(max / steps),
        scaleStartValue: 0,
        scaleShowVerticalLines: true,
        scaleShowGridLines: true,
        barShowStroke: true,
        scaleShowLabels: true,
        bezierCurve: false,
    });

}

