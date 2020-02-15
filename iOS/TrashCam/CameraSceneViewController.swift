//
//  CameraSceneViewController.swift
//  TrashCam
//
//  Created by Hrishikesh Bhattu on 15/02/20.
//  Copyright © 2020 Hrishikesh Bhattu. All rights reserved.
//

import UIKit
import MapKit


class CameraSceneViewController: UIViewController, CLLocationManagerDelegate, UIImagePickerControllerDelegate, UINavigationControllerDelegate {

    @IBOutlet weak var myImage: UIImageView!
    
    
    var locationManager = CLLocationManager()
    
    @IBAction func getLocationCoordinates(_ sender: UIButton) {
        
        if UIImagePickerController.isSourceTypeAvailable(UIImagePickerController.SourceType.camera) {
            let imagePicker = UIImagePickerController()
            imagePicker.delegate = self
            imagePicker.sourceType = UIImagePickerController.SourceType.camera
            imagePicker.allowsEditing = false
            self.present(imagePicker, animated: true, completion: nil)
        }
        
        if CLLocationManager.locationServicesEnabled() {
            locationManager.delegate = self
            locationManager.desiredAccuracy = kCLLocationAccuracyNearestTenMeters
            locationManager.startUpdatingLocation()
        }
        
    }
    
    func locationManager(_ manager: CLLocationManager, didUpdateLocations locations: [CLLocation]) {
        let locValue:CLLocationCoordinate2D = manager.location!.coordinate
        
        print("Location: [\(locValue.latitude), \(locValue.longitude)]")
    }
    
    override func viewDidLoad() {
        super.viewDidLoad()

        self.locationManager.requestWhenInUseAuthorization()
        // Do any additional setup after loading the view.
    }
    
    func imagePickerController(_ picker: UIImagePickerController, didFinishPickingMediaWithInfo info: [UIImagePickerController.InfoKey : Any]) {
        if (info[UIImagePickerController.InfoKey.editedImage] as? UIImage) != nil {

        } else if let image = (info[UIImagePickerController.InfoKey.originalImage] as? UIImage) {
            myImage.contentMode = .scaleToFill
            myImage.image = image
        } else {
            print("Something went wrong")
        }
    }
    

    /*
    // MARK: - Navigation

    // In a storyboard-based application, you will often want to do a little preparation before navigation
    override func prepare(for segue: UIStoryboardSegue, sender: Any?) {
        // Get the new view controller using segue.destination.
        // Pass the selected object to the new view controller.
    }
    */

}
