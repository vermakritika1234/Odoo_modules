import { registry } from "@web/core/registry";
import { Component, onWillStart, useRef, onMounted } from "@odoo/owl";
import { loadJS } from "@web/core/assets";

// import { ChartR } from "./chart_renderer/chart_renderer"

import Chart from "chart.js/auto";

const actionRegistry = registry.category("actions");

class ChartRender extends Component {
    setup() {
        console.log("====sales dashboard line 16==============");
        this.chartRef = useRef("chart");
        this.chartRef2 = useRef("secondChart");

        onWillStart(async () => {
            await loadJS("https://cdnjs.cloudflare.com/ajax/libs/Chart.js/4.4.1/chart.umd.min.js");
        });

        onMounted(async () => {
            this.renderChart();
        });
    }

    renderChart() {
        new Chart(
            this.chartRef.el,
            {
                type: 'doughnut',
                data: {
                    labels: ['Red', 'Blue', 'Yellow'],
                    datasets: [
                        {
                            label: 'My First Dataset',
                            data: [300, 50, 100],
                            backgroundColor: ['rgb(255, 99, 132)', 'rgb(54, 162, 235)', 'rgb(255, 205, 86)'],
                            hoverOffset: 4,
                        },
                    ],
                },
            }
        );
    }
}

ChartRender.template = "owl_dashboard.ChartRender";
// actionRegistry.add("Sales_order_dashboard", ChartRender);
