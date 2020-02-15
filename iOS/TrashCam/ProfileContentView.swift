//
//  ProfileContentView.swift
//  TrashCam
//
//  Created by Hrishikesh Bhattu on 14/02/20.
//  Copyright © 2020 Hrishikesh Bhattu. All rights reserved.
//

import SwiftUI

struct ProfileContentView: View {
    @State private var action: Int? = 0
    var body: some View {
        VStack {
            
            ProfileMapView()
                .frame(height: 300)
                .edgesIgnoringSafeArea(.top)

            UserImageCircle()
                .offset(y: -130)
                .padding(.bottom, -130)
            
            VStack(alignment: .leading) {
                Text("Hrishikesh Bhattu")
                    .font(.title)
                HStack {
                    Text("User since Feb 2020")
                        .font(.subheadline)
                    Spacer()
                    Text("21 Posts")
                        .font(.subheadline)
                }
            }
            .padding()
            
            HStack {
                    Text("@hrishibhattu")
                        .fontWeight(.semibold)
                        .font(.subheadline)
                        .foregroundColor(Color.white)
                        .padding()
                
            }
            .background(Color.blue)
//            .padding()
//            .foregroundColor(Color.white)
            .cornerRadius(40)
            
                        
            Spacer()
        }
    }
    
}

struct ProfileContentView_Previews: PreviewProvider {
    static var previews: some View {
        ProfileContentView()
    }
}
