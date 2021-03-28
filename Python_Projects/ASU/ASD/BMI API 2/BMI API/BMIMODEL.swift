//
//  BMIMODEL.swift
//  BMI API
//
//  Created by Ram on 11/14/20.
//

import Foundation
struct bmiResults: Decodable {
    let bmi: Float
    let more: [String]
    let risk: String
}
