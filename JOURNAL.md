---
title: "Mini SkidSteer"
author: "Rehan Shaik"
description: "Am creating a mini rc skidsteer for desktop to cure boredom"
created_at: "2025-07-2"
---

# July 8-9th: Started on CAD

Recently I have come accross many videos of rc construction toys. And one cought my eye. It was a skidsteer by professorBoots on yt! I thought it would be perfect to kill bordom on my desk. I started CADing creating the design that revolved around a similar design as professerBoots. I changed most of the functionality to reduce the complexity. Started with the body which for right now houses 2 N20 motors. The skidsteer will be driven as a tank drive so the motors will be mounted in the back and the front wheels will be mounted to 5x11x4mm bearing. The back cover and the cab are going to be screwed in together so they can swing open for easy access. I am really happy on the cad so far because this is my first time cading something that doesnt look entierly like a Box! I think the main body of the skidsteer is complete and all thats left to do is add the arm along with servo mounting points. After Cad is done I will have to start working on a costom PCB that can fit inside the small body!

![image](https://github.com/user-attachments/assets/10123f5b-dbb2-42f9-9553-c3368596de30)

Front Axel: The axel goes through bearings and cliped down to the body with a C-clip
![image](https://github.com/user-attachments/assets/9d56ee91-61a5-47ea-b958-e6619cce615b)

[Time spent this session: 8Hrs]


# July 26-27: Finished CADing!!

I finally finished the CADing on my skidstear. I added the two arms and the bucket!. Both the arm and the bucket are powerd by 2 sg90 motors. I was consernced if the servo would be able to move the weight of the arm + the load so I added gears to increase the torque. The servo is connected to a 10 teeth gear wich drives a 22 teeth servo. 2.2 : 1 gear ratio. At the bucket, the connected servo controles the tilt of the bucket! The bucket is connect with 2M screws. The Right arm is connect with another C-clips, just like the axils in the front and the Left arm is connected with 2M screws which screw to the gear. Now that I have finished the CAD I am going to start on a PCB which will house the ESP-32, the motor dirvers and the battery! I am also considering on using LEDs to add a little more ummph to the Skidstear. After finishing the PCB I might also change the cab of the skid stear to inlude the tradintional holes that the actual skidsteers have.

Full design!
<img width="706" height="496" alt="image" src="https://github.com/user-attachments/assets/95a5e1d3-10ae-45a7-99f8-d78691c77583" />

Bucket!
<img width="814" height="481" alt="image" src="https://github.com/user-attachments/assets/e39de069-14d0-4ef6-ac34-d495d1a62c02" />

The Gears on the Arm!
<img width="1048" height="608" alt="image" src="https://github.com/user-attachments/assets/da62aa97-323c-4354-b4cf-c2c984030307" />

The Right arm with the C-clip!
<img width="916" height="498" alt="image" src="https://github.com/user-attachments/assets/7e540490-00fa-44e9-9698-6e4ff330d02d" />


[Time spent this session: 4Hrs]

# July 30th: Finished PCB!

After long delay I finally finished my PCB!! I defenetly should not have pracasinated this long but I did! My PCB is 40mm x 48mm, I gave it a great amount of tolarace to I dont even have to think of it not fitting into my tiny tiny RC skidsteer! The brain of my RC skidsteer is a xiao esp32, with a drv8833 H Bridge for my my 2 n20 motors and a 5v buck converter. All of this is powerd by a TATTU 7.4v 300mAh 2S Lipo Battery. This is great for the small and compact size of this thing. During this process I struggled a lot on getting the right driver symboles and footprints for my drv8833 H Bridge so I got help from my cousin where we created custom footprint for it. Creating this PCB felt like hell because half the stuff I wanted, there were no footprints avalable or it was very difficly to find. But after a good hour of trying to find all the parts, I took a while looking up how to wire up the connesnts. This was second time ever creating a PCB so I felt very lost! But I did manage to get it done. I am still gonna go over and look at the pcb for any improvements or mistatakes to make sure this PCB turns out close to perfect as possible!

After creating the PCB I spent Some time on cleaning up my CAD design, like adding the holes in the cab to make it look cooler, adding the teeth to the bucket and changing the screw hole sides which I had all mixed up. I made the screw holes 1.7mm in diameter so I could simply screw them in with friction rather then heatsets. I felt doing it this way because from my last experiece in creating my macropad, the heatsets did not go so well and I thought it might ruin the skid steer. And after all that I think the CAD is offically complete so tmrw I can focus specifically on PCB and submitting!

PCB: 
<img width="975" height="1145" alt="image" src="https://github.com/user-attachments/assets/26d69707-0904-4ea5-8114-a71cc1b55466" />

<img width="1280" height="780" alt="image" src="https://github.com/user-attachments/assets/a332eb17-174c-495c-a29b-aa072fe8ed4e" />

CAD:
<img width="838" height="580" alt="image" src="https://github.com/user-attachments/assets/cd4d070a-d3d2-4333-b42e-e2c9282b1734" />

[Time spent this session: 5Hrs]











