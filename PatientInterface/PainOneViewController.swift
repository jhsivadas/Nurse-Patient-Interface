//
//  PainOneViewController.swift
//  PatientInterface
//
//  Created by Max Chou on 5/16/21.
//

import UIKit

class PainOneViewController: UIViewController {

    @IBOutlet var painField: UITextField!
    @IBOutlet var textView: UITextView!
    
    override func viewDidLoad() {
        super.viewDidLoad()

        painField.delegate = self
    }
    
    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
    }
    
    @IBAction func enterTapped(_ sender: Any) {
        textView.text = "Today's Pain Level Submitted\nPain Level: \(painField.text!)\n"
    }
    
    override func touchesBegan(_ touches: Set<UITouch>, with event: UIEvent?) {
        painField.resignFirstResponder()
    }
}

extension PainOneViewController : UITextFieldDelegate {
    
    func textFieldShouldReturn(_ textField: UITextField) -> Bool {
        textField.resignFirstResponder()
        return true
    }
}
