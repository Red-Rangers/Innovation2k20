//
//  ProfileSceneViewController.swift
//  TrashCam
//
//  Created by Hrishikesh Bhattu on 15/02/20.
//  Copyright © 2020 Hrishikesh Bhattu. All rights reserved.
//

import UIKit
import SwiftUI

class ProfileSceneViewController: UIViewController {

    override func viewDidLoad() {
        super.viewDidLoad()

        // Do any additional setup after loading the view.
    }
    
    @IBSegueAction func showProfile(_ coder: NSCoder) -> UIViewController? {
        
        let rootView = ProfileContentView()
        return UIHostingController(coder: coder, rootView: rootView)
    }
    
    

}
