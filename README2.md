# Nnamdi-Brachistochrone Algorithm 

1. **Set the First Point (Starting Point)**:
   - Let’s call this point \( P_1(x_1, y_1) \).

2. **Set the Second Point (Ending Point)**:
   - This is point \( P_2(x_2, y_2) \).

3. **Connect Points to Form a Triangle**:
   - Draw a line segment between \( P_1 \) and \( P_2 \) as the hypotenuse of a triangle.
   - Form either a right triangle or another type by choosing a third point, perhaps on the horizontal or vertical line passing through either \( P_1 \) or \( P_2 \).

   In the best case, you wil have a right angle.

4. **Determine if the Triangle is a Right Angle**:
   - Check if the triangle is a right triangle at the point where the two lines meet.
   - You might use the dot product to verify orthogonality if it's necessary to confirm a right angle.


5. **Weighted Average and Sine Calculation**:
   - Calculate the weighted average (centroid) of the points. For three points \( A(x_1, y_1) \), \( B(x_2, y_2) \), and \( C(x_3, y_3) \), this would be:
   ```tex
     \[
     \text{Centroid } G = \left( \frac{x_1 + x_2 + x_3}{3}, \frac{y_1 + y_2 + y_3}{3} \right)
     \]
     ```
   - Multiply by the trigonometric sine of the target angle. For an angle \(\theta\), you would calculate:
   ```tex
     \[
     G \cdot \sin(\theta)
     \]
     ```
   This will give you a result incorporating the weighted influence of each point relative to the angle.


