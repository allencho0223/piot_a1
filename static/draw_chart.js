function drawChart(chartType) {
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
    var LineChartDemo = new Chart(mychart, {
        type: "line",
        data: barData,
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

    // LineChartDemo.destroy();
}

