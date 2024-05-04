// Initial data for the chart
const initialData = {
    labels: [],
    datasets: [{
        data: [],
        borderColor: "red",
        fill: false
    }]
};

// Initialize the chart
function createChart(chart_title) {
    title = chart_title;
    chart_title = chart_title.replace(/\s/g, '');
    console.log(chart_title);
    return new Chart(chart_title, {
        type: "line",
        data: {},
        options: {
            title: {
                display: true,
                text: title,
                fontSize: 14,
                fontColor: 'black',
                fontStyle: 'bold'
            },
            legend: {
                display: true,
                position: 'bottom', // Position of the legend. Possible values are 'top', 'bottom', 'left', 'right'
                labels: {
                    fontColor: 'black', // Color of the legend labels
                    fontSize: 11, // Font size of the legend labels
                    fontStyle: 'bold' // Font style of the legend labels
                }
            },
            scales: {
                yAxes: [{
                    ticks: {
                        beginAtZero: false, // Start ticks from non-zero value
                        precision: 5 // Set the precision for floats to 1 decimal place
                    }
                }],
            },
            // plugins: {
            //     zoom: {
            //       zoom: {
            //         wheel: {
            //           enabled: true,
            //         },
            //         pinch: {
            //           enabled: true
            //         },
            //         mode: 'xy',
            //       }}},
                //   annotation: {
                //     drawTime: 'afterDatasetsDraw', // Position the annotation after the datasets are drawn
                //     annotations: [{
                //         type: 'line',
                //         mode: 'horizontal',
                //         scaleID: 'y-axis-0', // Use the y-axis scale
                //         value: 0.4, // Value where the line will be drawn
                //         borderColor: 'red', // Color of the line
                //         borderWidth: 2, // Width of the line
                //         label: {
                //             enabled: true,x
                //             content: 'Data Limit' // Label text
                //         }
                //     }]
                // }
        }
    });
};


$(document).ready(function () {
    // Function to update the graph
    function updateGraph(animate = false, custom_chart, url) {
        $.ajax({
            url: url,
            success: function (data) {
                $('#loadIndicator').hide();
                function dataFilter(identifier) {
                    var ds = data;
                    var ds_arr = []
                    for (let i = 0; i < ds[identifier].length; i++) {
                        try {
                            var x = JSON.parse(ds[identifier][i]);
                            ds[identifier][i] = x;
                            ds_arr.push(ds[identifier][i]);
                        } catch (error) {
                            console.log("An error has occured");
                            return ds;
                        };

                    }
                    return ds_arr;
                };

                custom_chart.data.datasets = dataFilter('datasets');
                custom_chart.data.labels = data['labels'];

                console.log(dataFilter('datasets'));

                if (animate) {
                    custom_chart.update();
                } else {
                    custom_chart.update('none');
                }
                console.log('Data Updated');

            },
            error: function (xhr, status, error) {
                console.error('Error fetching data:', error);
            }
        });
    }

    // Update graph using setInterval in minutes
    let mins_interval = 3;
    mins_interval = (1000 * 60) * mins_interval;

    // transformerPercentLoad = createChart(chart_title = "Transformer Percent Loading");

    // threePhaseCurrentGraph = createChart(chart_title = "Three Phase Current Graph");

    // updateGraph(animate = true, custom_chart = threePhaseCurrentGraph, url = '/dashboard/get_data/ThreePhaseCurrent/');
    // updateGraph(animate = true, custom_chart = transformerPercentLoad, url = '/dashboard/get_data/LoadCurve/');
    
    // setInterval(function(){
    //     updateGraph(animate = false, custom_chart = threePhaseCurrentGraph, url = '/dashboard/get_data/ThreePhaseCurrent/');
    //     updateGraph(animate = false, custom_chart = transformerPercentLoad, url = '/dashboard/get_data/LoadCurve/');
    // }, (1000) * mins_interval);


    threePhaseVoltageGraph = createChart(chart_title = "Three Phase Voltage Graph");

    threePhaseCurrentGraph = createChart(chart_title = "Three Phase Current Graph");

    updateGraph(animate = true, custom_chart = threePhaseCurrentGraph, url = '/dashboard/get_data/ThreePhaseCurrent/');
    updateGraph(animate = true, custom_chart = threePhaseVoltageGraph, url = '/dashboard/get_data/LoadCurve/');
    
    setInterval(function(){
        updateGraph(animate = false, custom_chart = threePhaseCurrentGraph, url = '/dashboard/get_data/ThreePhaseCurrent/');
        updateGraph(animate = false, custom_chart = threePhaseVoltageGraph, url = '/dashboard/get_data/LoadCurve/');
    }, mins_interval);
});