# Problem: Clock hands
Write a function that returns the acute angle between two clock hands,
with two integers for the number of hours and number of minutes.  

E.g. For 3:00, the acute angle would be 90°. For 6:00, it would be 180°.


# Notes
Each minute on the clock would be 6 degrees (360 / 60).  
Each hour can be multiplied by 5 to get the minutes it lines up with.  
Multiplying the minutes and converted hours by 6 will give the degrees of each hand.  
Taking the absolute value of the difference will give the angle between the two.
If the angle is larger than 180 degress (obtuse), subtract it from 360 to get the acute angle.  
