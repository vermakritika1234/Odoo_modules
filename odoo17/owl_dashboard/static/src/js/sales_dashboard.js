/** @odoo-module **/

import { registry } from "@web/core/registry";
// import { Component } from "@odoo/owl";
import { Component, onWillStart, useRef, onMounted } from "@odoo/owl";
import { useService } from "@web/core/utils/hooks";
import { loadJS } from "@web/core/assets";

// importing onwillstart will help to load the js 
// importing useRef will help to select the canvas from the template
// importing onMounted will help rendering the chart
const actionRegistry = registry.category("actions");

class CrmDashboard extends Component {
    setup() {
        console.log("====sales dashboard line 16==============");
        this.chartRef = useRef("chart")
        this.chartRef2 = useRef("secondChart")

        onWillStart(async()=>{
            await loadJS("https://cdnjs.cloudflare.com/ajax/libs/Chart.js/4.4.1/chart.umd.min.js")
        })

        onMounted(async()=>{
            const data = [
                { year: 2010, count: 10 },
                { year: 2011, count: 20 },
                { year: 2012, count: 15 },
                { year: 2013, count: 25 },
                { year: 2014, count: 22 },
                { year: 2015, count: 30 },
                { year: 2016, count: 28 },
              ];
            
              new Chart(
                this.chartRef.el,
                {
                  type: 'doughnut',
                  data: {
                    labels: [
                        'Red',
                        'Blue',
                        'Yellow'
                      ],
                      datasets: [
                        {
                        label: 'My First Dataset',
                        data: [300, 50, 100],
                        backgroundColor: [
                          'rgb(255, 99, 132)',
                          'rgb(54, 162, 235)',
                          'rgb(255, 205, 86)'
                        ],
                        hoverOffset: 4,
                     },
                    ]
                  }
                }
              );

              
        })
    }

    renderChart(){
        new Chart(
            this.chartRef.el,
            {
              type: 'doughnut',
              data: {
                labels: [
                    'Red',
                    'Blue',
                    'Yellow'
                  ],
                  datasets: [
                    {
                    label: 'My First Dataset',
                    data: [300, 50, 100],
                    backgroundColor: [
                      'rgb(255, 99, 132)',
                      'rgb(54, 162, 235)',
                      'rgb(255, 205, 86)'
                    ],
                    hoverOffset: 4,
                 },
                ]
              }
            }
          );
    }
        // super.setup();
        // this.orm = useService('orm');
        // this.state = {
        //     partnersCount: 0,
        //     loading: true
        // };
        // this.fetchData();
    }

 

CrmDashboard.template = "owl_dashboard.CrmDashboard";
// CrmDashboard.components = { chart_render };

actionRegistry.add("Sales_order_dashboard", CrmDashboard);
