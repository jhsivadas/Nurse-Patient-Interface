
//
//  ViewController.swift
//  PatientInterface
//
//  Created by Max Chou on 5/16/21.
//

import UIKit

class ViewController: UIViewController {
    
    @IBOutlet var notes: UIButton!
    @IBOutlet var meds: UIButton!
    @IBOutlet var scale: UIButton!
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        notes.backgroundColor = UIColor(ciColor: .green)
        notes.layer.cornerRadius = 8
        notes.setTitleColor(UIColor.black, for: .normal)
        
        meds.backgroundColor = UIColor(ciColor: .green)
        meds.layer.cornerRadius = 8
        meds.setTitleColor(UIColor.black, for: .normal)
        
        scale.backgroundColor = UIColor(ciColor: .green)
        scale.layer.cornerRadius = 8
        scale.setTitleColor(UIColor.black, for: .normal)
    }
}
