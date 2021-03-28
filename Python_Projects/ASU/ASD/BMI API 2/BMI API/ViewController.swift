//
//  ViewController.swift
//  BMI API
//
//  Created by Ram on 11/14/20.
//

import UIKit

class ViewController: UIViewController {
   
    //MARK: Properties
    
    @IBOutlet var landingView: UIView!
    
    @IBOutlet weak var heightFeild: UITextField!
    
    @IBOutlet weak var weightField: UITextField!
        
    @IBOutlet weak var riskValue: UILabel!
    
    @IBOutlet weak var bmiValue: UILabel!
    
    var educateLinks = [String]()
    override func viewDidLoad() {
        super.viewDidLoad()        // Do any additional setup after loading the view.
    }

    @IBAction func calculateBmi(_ sender: UIButton) {
        let heightValue = heightFeild.text!
        let weightValue = weightField.text!
    
        let restUrl = "http://webstrar99.fulton.asu.edu/page3/Service1.svc/calculateBMI?height=\(heightValue)&weight=\(weightValue)"

        let url = URL(string: restUrl)!

        let jsonQuery = URLSession.shared.dataTask(with: url, completionHandler: { data, response, error -> Void in
            if (error != nil) {
            print(error!.localizedDescription)
            }
            let decoder = JSONDecoder()
            let jsonResult = try! decoder.decode(bmiResults.self, from: data!)

            let bmi = jsonResult.bmi
            let more = jsonResult.more
            let risk = jsonResult.risk
            //self.links = more

            DispatchQueue.main.async {
                self.bmiValue.text = String(format: "%.2f", bmi)
                self.riskValue.text = risk
                self.riskValue.textColor = self.getColor(bmi : bmi)
                self.educateLinks = more
            }

        })
        jsonQuery.resume()
    }
    
    @IBAction func educateMe(_ sender: UIButton) {
        if (self.educateLinks.count > 0) {
                    
            guard let url = URL(string: self.educateLinks[0]) else {return}
                    UIApplication.shared.open(url)
                }
        else{
            let restUrl = "http://webstrar99.fulton.asu.edu/page3/Service1.svc/calculateBMI?height=10&weight=10"

            let url = URL(string: restUrl)!
            let jsonQuery = URLSession.shared.dataTask(with: url, completionHandler: { data, response, error -> Void in
                if (error != nil) {
                print(error!.localizedDescription)
                }
                let decoder = JSONDecoder()
                let jsonResult = try! decoder.decode(bmiResults.self, from: data!)
                dump(jsonResult)
                let more = jsonResult.more

                DispatchQueue.main.async {
                    self.educateLinks = more
                    guard let url = URL(string: self.educateLinks[0]) else {return}
                            UIApplication.shared.open(url)                }

            })
            jsonQuery.resume()

        }
        
    }
    
    func getColor(bmi: Float) -> UIColor {
        
        if (bmi < 18) {
            return UIColor.blue
        }
        else if (bmi >= 18 && bmi < 25) {
            return UIColor.green
        }
        else if (bmi >= 25 && bmi < 30) {
            return UIColor.purple
        }
        else { // if (bmi > 30) {
            return UIColor.red
        }
    }
    
}

