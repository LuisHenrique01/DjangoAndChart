Highcharts.getJSON('https://raw.githubusercontent.com/IFPiaui/covid19-map/master/static_jsons/limites.json', function (geojson) {

    // Initiate the chart
    Highcharts.mapChart('map2', {
        chart: {
            map: geojson
        },

        title: {
            text: 'Casos no Piauí'
        },

        subtitle: {
            text: 'Última atualização 04/05/20'
        },

        mapNavigation: {
            enabled: true,
            buttonOptions: {
                verticalAlign: 'bottom'
            }
        },

        colorAxis: {
            min: 0,
            stops: [[0, '#F1EEF6'] , [0.01, '#71627E'], [0.50, '#4E3C5E'], [1, '#0F0C12']],
        },

        series: [{
            data: dataPiaui,
            keys: ['id', 'value'],
            joinBy: 'id',
            name: 'Confirmados',
            states: {
                hover: {
                    color: '#a4edba'
                }
            },
            dataLabels: {
                format: '{point.name}',
            }
        }]
    });
});