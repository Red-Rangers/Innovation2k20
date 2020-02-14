//
//  UserImageCircle.swift
//  TrashCam
//
//  Created by Hrishikesh Bhattu on 14/02/20.
//  Copyright © 2020 Hrishikesh Bhattu. All rights reserved.
//

import SwiftUI

struct UserImageCircle: View {
    var body: some View {
        Image("UserImage")
            .clipShape(Circle())
        .overlay(
            Circle().stroke(Color.white, lineWidth: 4))
        .shadow(radius: 10)
        
    }
    
}

struct UserImageCircle_Previews: PreviewProvider {
    static var previews: some View {
        UserImageCircle()
    }
}
