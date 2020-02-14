//
//  ProfileMapView.swift
//  TrashCam
//
//  Created by Hrishikesh Bhattu on 14/02/20.
//  Copyright © 2020 Hrishikesh Bhattu. All rights reserved.
//

import SwiftUI
import MapKit

struct ProfileMapView: UIViewRepresentable {
    func makeUIView(context: Context) -> MKMapView {
        MKMapView(frame: .zero)
    }

    func updateUIView(_ view: MKMapView, context: Context) {
        let coordinate = CLLocationCoordinate2D(
            latitude: 18.486831, longitude: 73.816434)
        let span = MKCoordinateSpan(latitudeDelta: 2.0, longitudeDelta: 2.0)
        let region = MKCoordinateRegion(center: coordinate, span: span)
        view.setRegion(region, animated: true)
    }
}

struct ProfileMapView_Previews: PreviewProvider {
    static var previews: some View {
        ProfileMapView()
    }
}
