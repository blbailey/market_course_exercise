\ENCODING=ISO-8859-1
\Problem name: 

Minimize
 obj: Highest_x
Subject To
 coalition1110: - x_G1 - x_G2 - x_D1 - Highest_x <= -2720
 coalition1101: - x_G1 - x_G2 - x_D2 - Highest_x <= -1150
 coalition1011: - x_G1 - x_D1 - x_D2 - Highest_x <= -2520
 coalition0111: - x_G2 - x_D1 - x_D2 - Highest_x <= -1600
 coalition1100: - x_G1 - x_G2 - Highest_x <= 0
 coalition1010: - x_G1 - x_D1 - Highest_x <= -2520
 coalition1001: - x_G1 - x_D2 - Highest_x <= -1150
 coalition0110: - x_G2 - x_D1 - Highest_x <= -1600
 coalition0101: - x_G2 - x_D2 - Highest_x <= -750
 coalition0011: - x_D1 - x_D2 - Highest_x <= 0
 coalition1000: - x_G1 - Highest_x <= 0
 coalition0100: - x_G2 - Highest_x <= 0
 coalition0010: - x_D1 - Highest_x <= 0
 coalition0001: - x_D2 - Highest_x <= 0
 balance:       x_G1 + x_G2 + x_D1 + x_D2  = 3470
Bounds
      Highest_x Free
End
