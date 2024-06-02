document.addEventListener("DOMContentLoaded", function() {
    var dashboardUsage = window.dashboardUsage;
    var dataUsage = window.dataUsage;

    // Dashboard Usage Bar Chart
    var dashboardUsageChartEl = document.querySelector('#dashboardUsageChart'),
        dashboardUsageChartConfig = {
            series: [
                {
                    name: 'Dashboard Usage',
                    data: [
                        dashboardUsage.count_global_view,
                        dashboardUsage.count_global_map,
                        dashboardUsage.count_site_info,
                        dashboardUsage.count_employee,
                        dashboardUsage.count_country,
                        dashboardUsage.count_contract,
                        dashboardUsage.count_projectIDCard,
                        dashboardUsage.count_facilities,
                        dashboardUsage.count_supplierGIS
                    ]
                }
            ],
            chart: {
                height: 350,
                type: 'bar'
            },
            plotOptions: {
                bar: {
                    horizontal: false,
                    columnWidth: '55%',
                    endingShape: 'rounded',
                    distributed: true
                }
            },
            dataLabels: {
                enabled: false
            },
            stroke: {
                show: true,
                width: 2,
                colors: ['transparent']
            },
            xaxis: {
                categories: ['维修站点关键数据', '全球站点数据图', '员工信息', '场地管理', '站点地理信息系统（GIS）', '产品平台图', '项目详细信息', '设备分布图', '供应商GIS'],
            },
            yaxis: {
                title: {
                    text: '仪表板使用统计',
                  style: {
                  fontSize: '16px'  // 你可以根据需要调整字体大小
              }
                }
            },
            fill: {
                opacity: 1
            },
            tooltip: {
                y: {
                    formatter: function (val) {
                        return val + " uses"
                    }
                }
            },
            colors: ['#3678f4', '#4b90f4', '#527dff', '#004783', '#91d5f4', '#877ffd', '#007485', '#452eff', '#00a1de']
        };

    if (typeof dashboardUsageChartEl !== undefined && dashboardUsageChartEl !== null) {
        var dashboardUsageChart = new ApexCharts(dashboardUsageChartEl, dashboardUsageChartConfig);
        dashboardUsageChart.render();
    }

    // Data Usage Bar Chart
    var dataUsageChartEl = document.querySelector('#dataUsageChart'),
        dataUsageChartConfig = {
            series: [
                {
                    name: 'Data Usage',
                    data: [
                        dataUsage.count_footprint,
                        dataUsage.count_maintenance,
                        dataUsage.count_manufacturing,
                        dataUsage.count_manufacturing_CNC,
                        dataUsage.count_examine,
                        dataUsage.count_welding_image,
                        dataUsage.count_surface_image,
                        dataUsage.count_welding_data,
                        dataUsage.count_supplier
                    ]
                }
            ],
            chart: {
                height: 350,
                type: 'bar'
            },
            plotOptions: {
                bar: {
                    horizontal: false,
                    columnWidth: '55%',
                    endingShape: 'rounded',
                    distributed: true
                }
            },
            dataLabels: {
                enabled: false
            },
            stroke: {
                show: true,
                width: 2,
                colors: ['transparent']
            },
            xaxis: {
                categories: ['站点', '维修', '制造', 'CNC数据', '测试数据', '焊接缺陷图象', '表面缺陷', '焊接数据', '供应商数据'],
            },
            yaxis: {
                title: {
                    text: '数据使用情况',
                style: {
                  fontSize: '16px'  // 你可以根据需要调整字体大小
              }
                }
            },
            fill: {
                opacity: 1
            },
            tooltip: {
                y: {
                    formatter: function (val) {
                        return val + " uses"
                    }
                }
            },
            colors: ['#00754e', '#00a466', '#00bdbd', '#00ff18', '#047a00', '#65ff00', '#8cc500', '#ddff3c', '#678eff']
        };

    if (typeof dataUsageChartEl !== undefined && dataUsageChartEl !== null) {
        var dataUsageChart = new ApexCharts(dataUsageChartEl, dataUsageChartConfig);
        dataUsageChart.render();
    }

    // Dashboard Usage Donut Chart
    var dashboardUsageDonutChartEl = document.querySelector('#dashboardUsageDonutChart'),
        dashboardUsageDonutChartConfig = {
            chart: {
                height: 350,
                type: 'donut'
            },
            labels: ['维修站点关键数据', '全球站点数据图', '员工信息', '场地管理', '站点地理信息系统（GIS）', '产品平台图', '项目详细信息', '设备分布图', '供应商GIS'],
            series: [
                dashboardUsage.count_global_view,
                dashboardUsage.count_global_map,
                dashboardUsage.count_site_info,
                dashboardUsage.count_employee,
                dashboardUsage.count_country,
                dashboardUsage.count_contract,
                dashboardUsage.count_projectIDCard,
                dashboardUsage.count_facilities,
                dashboardUsage.count_supplierGIS
            ],
            colors: ['#3678f4', '#4b90f4', '#527dff', '#004783', '#91d5f4', '#877ffd', '#007485', '#452eff', '#00a1de'],
            stroke: {
                width: 5,
                colors: ['#ffffff']
            },
            dataLabels: {
                enabled: false
            },
            legend: {
                show: false
            },
            plotOptions: {
                pie: {
                    donut: {
                        size: '75%',
                        labels: {
                            show: true,
                            value: {
                                fontSize: '1.5rem',
                                fontFamily: 'Public Sans',
                                color: '#000000',
                                offsetY: -15
                            },
                            name: {
                                offsetY: 20,
                                fontFamily: 'Public Sans'
                            },
                            total: {
                                show: true,
                                fontSize: '0.8125rem',
                                color: '#000000',
                                label: '仪表盘使用总计',
                                formatter: function (w) {
                                    return w.globals.seriesTotals.reduce((a, b) => a + b, 0)
                                }
                            }
                        }
                    }
                }
            }
        };

    if (typeof dashboardUsageDonutChartEl !== undefined && dashboardUsageDonutChartEl !== null) {
        var dashboardUsageDonutChart = new ApexCharts(dashboardUsageDonutChartEl, dashboardUsageDonutChartConfig);
        dashboardUsageDonutChart.render();
    }

    // Data Usage Donut Chart
    var dataUsageDonutChartEl = document.querySelector('#dataUsageDonutChart'),
        dataUsageDonutChartConfig = {
            chart: {
                height: 350,
                type: 'donut'
            },
            labels: ['站点', '维修', '制造', 'CNC数据', '测试数据', '焊接缺陷图象', '表面缺陷', '焊接数据', '供应商数据'],
            series: [
                dataUsage.count_footprint,
                dataUsage.count_maintenance,
                dataUsage.count_manufacturing,
                dataUsage.count_manufacturing_CNC,
                dataUsage.count_examine,
                dataUsage.count_welding_image,
                dataUsage.count_surface_image,
                dataUsage.count_welding_data,
                dataUsage.count_supplier
            ],
            colors: ['#00754e', '#00a466', '#00bdbd', '#00ff18', '#047a00', '#65ff00', '#8cc500', '#ddff3c', '#678eff'],
            stroke: {
                width: 5,
                colors: ['#ffffff']
            },
            dataLabels: {
                enabled: false
            },
            legend: {
                show: false
            },
            plotOptions: {
                pie: {
                    donut: {
                        size: '75%',
                        labels: {
                            show: true,
                            value: {
                                fontSize: '1.5rem',
                                fontFamily: 'Public Sans',
                                color: '#000000',
                                offsetY: -15
                            },
                            name: {
                                offsetY: 20,
                                fontFamily: 'Public Sans'
                            },
                            total: {
                                show: true,
                                fontSize: '0.8125rem',
                                color: '#000000',
                                label: '数据使用总计',
                                formatter: function (w) {
                                    return w.globals.seriesTotals.reduce((a, b) => a + b, 0)
                                }
                            }
                        }
                    }
                }
            }
        };

    if (typeof dataUsageDonutChartEl !== undefined && dataUsageDonutChartEl !== null) {
        var dataUsageDonutChart = new ApexCharts(dataUsageDonutChartEl, dataUsageDonutChartConfig);
        dataUsageDonutChart.render();
    }
});
