//
//  PainTwoViewController.swift
//  PatientInterface
//
//  Created by Max Chou on 5/16/21.
//

import Charts
import UIKit

class PainTwoViewController: UIViewController, ChartViewDelegate {
    
    var barChart = BarChartView()

    override func viewDidLoad() {
        super.viewDidLoad()
        barChart.delegate = self

    }
    
    override func viewDidLayoutSubviews() {
        super.viewDidLayoutSubviews()
        
        barChart.frame = CGRect(x: 0, y: 0,
                                width: self.view.frame.size.width,
                                height: self.view.frame.size.width)
        barChart.center = view.center
        view.addSubview(barChart)
        
        var entries = [BarChartDataEntry]()
        
        for x in 0..<5 {
            entries.append(BarChartDataEntry(x: Double(x),
                                             y: Double(x % 3)))
        }
        
        let set = BarChartDataSet(entries: entries)
        
        set.colors = ChartColorTemplates.joyful()
        
        let data = BarChartData(dataSet: set)
        
        barChart.data = data
        barChart.leftAxis.axisMinimum = 0
        barChart.leftAxis.axisMaximum = 10
        barChart.xAxis.labelPosition = .bottom
        barChart.legend.enabled = false
        barChart.xAxis.drawGridLinesEnabled = false
        barChart.leftAxis.drawGridLinesEnabled = false
        barChart.rightAxis.enabled = false
        
        
        let days = ["Mon", "Tues", "Wed", "Thurs", "Fri"]
        barChart.xAxis.valueFormatter = IndexAxisValueFormatter(values: days)
        barChart.xAxis.granularity = 1
    }
}
